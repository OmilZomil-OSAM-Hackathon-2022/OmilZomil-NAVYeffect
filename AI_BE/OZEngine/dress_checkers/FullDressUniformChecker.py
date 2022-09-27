import sys
from lib.utils import *
from lib.defines import *
from lib.ocr import OCR, draw_rectangle

# (동)정복 검사


class FullDressUniformChecker():
    def __init__(self):
        # hyperparameter
        self.uniform_filter = {'lower': (12, 0, 0), 'upper': (197, 255, 116)}
        self.anchor_filter = {'lower': (20, 100, 100), 'upper': (30, 255, 255)}
        self.classes_filter = {
            'lower': (140, 120, 50), 'upper': (190, 255, 255)}

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

    def getName(self, org_img):
        img = org_img.copy()
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        ocr_str, boxes = OCR(img)
        name = clean_text(ocr_str)

        if len(boxes):
            draw_rectangle(img, boxes[0], boxes[2], Color.RED, 1, 1)
            plt_imshow([f'name tag {name}'], [img])
            cv2.imwrite('./res/res_ocr.jpg', img)
            return name
        else:
            return None

    def checkUniform(self, org_img):
        img = org_img.copy()
        # img = cv2.resize(img, (500,500))
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, w = img.shape[:2]

        # 정복 filter
        lower, upper = self.uniform_filter['lower'], self.uniform_filter['upper']
        black_mask = cv2.inRange(hsv_img, lower, upper)
        masked_img = cv2.bitwise_and(img, img, mask=black_mask)

        contours, hierarchy = cv2.findContours(
            black_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        sorted_contours, sorted_hierarchy = sortContoursByArea(
            contours, hierarchy)

        ocr_str, ocr_boxes = OCR(img)
        print('ocr:', ocr_str, ocr_boxes)

        contour_dic = {}
        component_dic = {}

        # 이름표, 계급장 체크
        name_tag_content, level_tag_content = None, None
        for i, (contour, lev) in enumerate(zip(sorted_contours, sorted_hierarchy)):
            cur_node, next_node, prev_node, first_child, parent = lev
            if i == 0:  # 정복
                cv2.drawContours(img, [contour], 0, Color.RED, -1)
                contour_dic['shirt'] = contour
                shirt_node = cur_node
                continue

            # 정복 영영 안쪽 && 모서리가 4~5 && 크기가 {hyperParameter} 이상 => (이름표)
            # 이름표 또는 계급장
            if parent == shirt_node and 4 <= getVertexCnt(contour) <= 5 and cv2.contourArea(contour) > 300:
                center_p = getContourCenterPosition(contour)
                max_xy, min_xy = np.max(contour, axis=0)[
                    0], np.min(contour, axis=0)[0]

                # 이름표 체크
                if center_p[0] < (w//2) and not component_dic.get('name_tag'):
                    for ocr_box in ocr_boxes:
                        ocr_center_xy = getRectCenterPosition(ocr_box)
                        if isPointInBox(ocr_center_xy, (min_xy, max_xy)):
                            # name = self.getName(roi)
                            name = ocr_str
                            contour_dic['name_tag'] = contour
                            component_dic['name_tag'] = name
                            drawPoint(img, center_p, Color.PURPLE, 50)

        half_line_p1, half_line_p2 = (w//2, 0), (w//2, h)
        cv2.line(img, half_line_p1, half_line_p2, Color.WHITE, 5)

        cv2.imwrite('./res/res05.jpg', masked_img)
        cv2.imwrite('./res/res06.jpg', img)
        plt_imshow(['black_mask', 'masked img (bitwise and)', 'img'], [
                   black_mask, masked_img, img])

        # 네카치프 / 네카치프링 체크
        img2 = org_img.copy()

        lower, upper = self.anchor_filter['lower'], self.anchor_filter['upper']
        yellow_mask = cv2.inRange(hsv_img, lower, upper)
        anchor_masked_img = cv2.bitwise_and(org_img, org_img, mask=yellow_mask)

        contours, _ = cv2.findContours(
            yellow_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img2, contours, 0, Color.RED, 2)

        for contour in contours:
            if cv2.contourArea(contour) > 300:
                center_p = getContourCenterPosition(contour)
                if center_p[0] < (w//2) and not component_dic.get('anchor'):
                    contour_dic['anchor'] = contour
                    component_dic['anchor'] = True

        # 계급장 체크
        lower, upper = self.classes_filter['lower'], self.classes_filter['upper']
        red_mask = cv2.inRange(hsv_img, lower, upper)
        classes_masked_img = cv2.bitwise_and(org_img, org_img, mask=red_mask)

        contours, _ = cv2.findContours(
            red_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img2, contours, 0, Color.BLUE, 2)

        for contour in contours:
            if cv2.contourArea(contour) > 300:
                center_p = getContourCenterPosition(contour)
                if center_p[0] < (w//2) and not component_dic.get('classes_tag'):
                    contour_dic['classes_tag'] = contour
                    component_dic['classes_tag'] = True

        plt_imshow(['yellow masked', 'red_masked'], [
                   anchor_masked_img, classes_masked_img])

        x, y, w, h = cv2.boundingRect(contour_dic['anchor'])
        print(x,y,w,h)
        anchor_roi = org_img[y:y+h, x:x+w]

        x, y, w, h = cv2.boundingRect(contour_dic['classes_tag'])
        print(x,y,w,h)
        classes_roi = org_img[y:y+h, x:x+w]

        plt_imshow(['anchor', 'classes'], [anchor_roi, classes_roi])
        plt_imshow(['img2'], [img2])
        return component_dic, contour_dic
