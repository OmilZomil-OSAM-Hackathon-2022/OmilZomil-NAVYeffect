import sys
print(sys.path)
from lib.utils import *
from lib.defines import *
from lib.ocr import OCR, draw_rectangle

# (동)정복 검사
class FullDressUniformChecker():
    def __init__(self):
        # hyperparameter
        self.uniform_filter = {'lower': (12,0,0), 'upper': (197,255,116)}

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

        lower, upper = self.uniform_filter['lower'], self.uniform_filter['upper'] # 정복 filter 
        black_mask = cv2.inRange(hsv_img, lower, upper)
        masked_img = cv2.bitwise_and(img, img, mask=black_mask)

        contours, hierarchy = cv2.findContours(black_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        sorted_contours, sorted_hierarchy = sortContoursByArea(contours, hierarchy)

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
                shirt_node = cur_node
                continue

            # 정복 영영 안쪽 && 모서리가 4~5 && 크기가 {hyperParameter} 이상 => (이름표)
            if parent == shirt_node and 4 <= getVertexCnt(contour) <= 5 and cv2.contourArea(contour) > 300: # 이름표 또는 계급장
                center_p = getContourCenterPosition(contour)
                max_xy, min_xy = np.max(contour, axis=0)[0],np.min(contour, axis=0)[0]
                
                # 이름표 체크
                if center_p[0] < (w//2) and not component_dic.get('name_tag'):
                    for ocr_box in ocr_boxes:
                        ocr_center_xy = getRectCenterPosition(ocr_box)
                        if isPointInBox(ocr_center_xy, (min_xy, max_xy)):
                            x, y, w, h = cv2.boundingRect(contour)
                            roi = org_img[y:y+h, x:x+w]
                            name = self.getName(roi)
                            contour_dic['name_tag'] = contour
                            component_dic['name_tag'] = name
                            cv2.drawContours(img, [contour], 0, Color.RED, 2)
                            cv2.drawContours(img, [contour], 0, Color.GREEN, -1)
                            drawPoint(img, center_p, Color.PURPLE, 50)

        half_line_p1, half_line_p2 = (w//2, 0), (w//2, h)
        cv2.line(img, half_line_p1, half_line_p2, Color.WHITE, 5)

        
        cv2.imwrite('./res/res05.jpg', masked_img)
        cv2.imwrite('./res/res06.jpg', img)
        plt_imshow(['black_mask', 'masked img (bitwise and)', 'img'], [black_mask, masked_img, img])
        return component_dic, contour_dic