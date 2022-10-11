from OZEngine.dress_chekcers import UniformChecker
from OZEngine.lib.utils import *
from OZEngine.lib.defines import *
from OZEngine.lib.ocr import OCR
from OZEngine.dress_classifier import classification2


# 샘브레이 검사
class NavyServiceUniformChecker(UniformChecker):
    def __init__(self):
        # hyperparameter
        filter = {
            'uniform': {
                'lower': (30, 20, 0),
                'upper': (255, 255, 255)
            },
            'class_tag': {
                'lower': (0, 150, 90),
                'upper': (255, 255, 255)
            }
        }

    

    def getClasses(self, img, hsv_img, contour):
        box_position, class_name, masked_img = None, None, None
        if contour is None:
            return box_position, class_name, masked_img

        box_position = cv2.boundingRect(contour)
        x, y, w, h = box_position
        roi = img[y:y+h, x:x+w]
        hsv_roi = hsv_img[y:y+h, x:x+w]

        contours, masked_img = self.getMaskedContours(
            img=roi, hsv_img=hsv_roi, kmeans=True, kind='classes')

        classes_n = 0
        for contour in contours:
            if 100 < cv2.contourArea(contour):
                classes_n += 1

        if 1 <= classes_n <= 4:
            class_name = Classes.dic[classes_n]

        return box_position, class_name, masked_img

    def isInShirt(self, contour):
        # 샘브레이 영영 안쪽 && 모서리가 4~5 && 크기가 {hyperParameter} 이상 => (이름표 or 계급장)
        return 3 <= getVertexCnt(contour) <= 10 and cv2.contourArea(contour) > 300

    def checkUniform(self, org_img):
        img = org_img
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, w = img.shape[: 2]

        box_position_dic = {}
        component_dic = {}
        masked_img_dic = {}

        # 샘당 filter
        contours, hierarchy, masked_img_dic['shirt'] = self.getMaskedContours(
            img=img, hsv_img=hsv_img, kind='uniform', sort=True)

        # 이름표, 계급장 체크
        for i, (contour, lev) in enumerate(zip(contours, hierarchy)):
            is_class_tag = component_dic.get('class_tag')
            is_name_tag = component_dic.get('name_tag')

            if is_name_tag and is_class_tag:
                break

            cur_node, next_node, prev_node, first_child, parent = lev
            if i == 0:  # 셈브레이
                shirt_node = cur_node
                continue

            # 이름표 또는 계급장
            if parent == shirt_node and self.isInShirt(contour):
                box_position = cv2.boundingRect(contour)
                center_p = getContourCenterPosition(contour)

                # 파츠 분류
                # kind = model(img)
                position = 'left' if center_p[0] < (w//2) else 'right'

                # 이름표 체크
                if not is_name_tag and position == 'left' kind == 'name_tag':
                    # 이름표 OCR
                    if self.name_cache:
                        ox_position_dic['name_tag'] = cv2.boundingBox(
                            contour)
                        component_dic['name_tag'] = 'cached ' + self.name_cache
                    else:
                        ocr_list = OCR(img)
                        box_position_dic['name_tag'], component_dic['name_tag'] = self.getName(
                            contour, ocr_list)

                # 계급장 체크
                elif not is_class_tag and position == 'right' kind == 'class_tag':
                    box_position, component, masked_img = self.getClasses(
                        img, hsv_img, contour)
                    box_position_dic['class_tag'] = box_position
                    component_dic['class_tag'] = component
                    masked_img_dic['class_tag'] = masked_img

        return component_dic, box_position_dic, masked_img_dic
