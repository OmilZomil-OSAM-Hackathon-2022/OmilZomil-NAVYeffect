from lib.utils import *
from lib.defines import *
from lib.ocr import OCR, draw_rectangle


# 샘브레이 검사
class NavyServiceUniformChecker():
    def __init__(self):
        # hyperparameter
        
        self.uniform_filter = {'lower': (30, 20, 0), 'upper': (255, 255, 255)}
        self.classes_filter = {
            'lower': (0, 150, 90), 'upper': (255, 255, 255)}

        self.debug_mode = False

    def getName(self, org_img):
        img = org_img.copy()
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        ocr_str, boxes = OCR(img)
        name = clean_text(ocr_str)
        print('name :', name)
        if len(boxes):
            for box in boxes:
                draw_rectangle(img, box[0], box[2], Color.RED, 1, 1)
            plt_imshow([f'name tag {name}'], [img])
            return name
        else:
            plt_imshow([f'name tag None'], [img])
            return None

    def getClasses(self, org_img):
        img = org_img.copy()
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # 샘당 계급장 filter
        lower, upper = self.classes_filter['lower'], self.classes_filter['upper']
        yellow_mask = cv2.inRange(hsv_img, lower, upper)

        morphed_mask = yellow_mask
        # morphed_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_CLOSE, (10, 1))
        masked_img = cv2.bitwise_and(img, img, mask=yellow_mask)
        contours, _ = cv2.findContours(
            morphed_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        classes_n = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if 10 < area:
                classes_n += 1
                cv2.drawContours(img, [contour], 0, Color.RED, -1)

        if 1 <= classes_n <= 4:
            plt_imshow(['yellow filter', 'morphed mask', 'masked img', f'img {Classes.dic[classes_n]}'], [
                       yellow_mask, morphed_mask, masked_img, img])
            return Classes.dic[classes_n]
        else:
            plt_imshow(['yellow filter', 'morphed mask', 'masked img', f'img None'], [
                       yellow_mask, morphed_mask, masked_img, img])
            return None

    def checkUniform(self, org_img):
        img = org_img.copy()
        # img = cv2.resize(img, (500,500))
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, w = img.shape[:2]

        # 샘당 filter
        lower, upper = self.uniform_filter['lower'], self.uniform_filter['upper']
        blue_mask = cv2.inRange(hsv_img, lower, upper)
        masked_img = cv2.bitwise_and(img, img, mask=blue_mask)

        contours, hierarchy = cv2.findContours(
            blue_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        sorted_contours, sorted_hierarchy = sortContoursByArea(
            contours, hierarchy)

        # 이름표 OCR
        ocr_str, ocr_boxes = OCR(img)
        print(ocr_str)
        contour_dic = {}
        component_dic = {}

        # 이름표, 계급장 체크
        name_tag_content, level_tag_content = None, None
        for i, (contour, lev) in enumerate(zip(sorted_contours, sorted_hierarchy)):
            cur_node, next_node, prev_node, first_child, parent = lev
            if i == 0:  # 셈브레이
                cv2.drawContours(img, [contour], 0, Color.RED, -1)
                shirt_node = cur_node
                continue

            # 샘브레이 영영 안쪽 && 모서리가 4~5 && 크기가 {hyperParameter} 이상 => (이름표 or 계급장)
            # 이름표 또는 계급장
            if parent == shirt_node and 3 <= getVertexCnt(contour) <= 10 and cv2.contourArea(contour) > 300:
                center_p = getContourCenterPosition(contour)
                drawPoint(img, center_p, Color.PURPLE, 30)
                max_xy, min_xy = np.max(contour, axis=0)[
                    0], np.min(contour, axis=0)[0]

                # 이름표 체크
                if center_p[0] < (w//2) and not component_dic.get('name_tag'):
                    for ocr_box in ocr_boxes:
                        ocr_center_xy = getRectCenterPosition(ocr_box)
                        if isPointInBox(ocr_center_xy, (min_xy, max_xy)):
                            x, y, w, h = cv2.boundingRect(contour)
                            roi = org_img[y:y+h, x:x+w]
                            plt_imshow('name tag', roi)
                            # name = self.getName(roi)
                            name = ocr_str
                            contour_dic['name_tag'] = contour
                            component_dic['name_tag'] = name
                            cv2.drawContours(img, [contour], 0, Color.RED, 2)
                            cv2.drawContours(
                                img, [contour], 0, Color.GREEN, -1)
                            drawPoint(img, center_p, Color.PURPLE, 30)
                            break

                # 계급장 체크
                elif center_p[0] > (w//2) and not component_dic.get('class_tag'):
                    x, y, w, h = cv2.boundingRect(contour)
                    roi = org_img[y:y+h, x:x+w]
                    classes = self.getClasses(roi)
                    if classes:
                        contour_dic['class_tag'] = contour
                        component_dic['class_tag'] = classes
                        cv2.drawContours(img, [contour], 0, Color.RED, 2)
                        cv2.drawContours(img, [contour], 0, Color.GREEN, -1)
                        drawPoint(img, center_p, Color.PURPLE, 30)
                        break

        half_line_p1, half_line_p2 = (w//2, 0), (w//2, h)
        cv2.line(img, half_line_p1, half_line_p2, Color.WHITE, 5)

        cv2.imwrite('./res/res05.jpg', masked_img)
        cv2.imwrite('./res/res06.jpg', img)
        plt_imshow(['blue filter', 'masked img (bitwise and)', 'img'], [
                   blue_mask, masked_img, img])
        return component_dic, contour_dic
