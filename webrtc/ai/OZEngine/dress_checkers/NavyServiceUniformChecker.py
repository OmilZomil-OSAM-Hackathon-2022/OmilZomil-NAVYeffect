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
            }
            'class_tag': {
                'lower': (0, 150, 90),
                'upper': (255, 255, 255)
            }
        }

    def getMaskedContours(self, img=None, hsv_img=None, kmeans=None, morph=None, kind=None, sort=False):
        lower, upper = self.filter[kind]['lower'], self.uniform_filter[kind]['upper']
        mask = cv2.inRange(hsv_img, lower, upper)

        if kmeans:
            img_s = classification2(img, 10)
            img = classification2(img, 10)

        if morph == 'erode':
            org_mask = mask.copy()

            k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 2))
            mask = cv2.erode(org_mask, k, iterations=2)

            plt_imshow(['org_mask', 'maskk', 'm2'], [org_mask, mask])

        masked_img = cv2.bitwise_and(img, img, mask=mask)

        if sort:
            contours, hierarchy = cv2.findContours(
                mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
            sorted_contours, sorted_hierarchy = sortContoursByArea(
                contours, hierarchy)
            return sorted_contours, sorted_hierarchy, mask
        else:
            contours, _ = cv2.findContours(
                mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            return contours, masked_img

    def getName(self, contour, ocr_list=[]):
        max_xy, min_xy = np.max(contour, axis=0)[
            0], np.min(contour, axis=0)[0]

        box_position, name = None, None
        name_chrs = []

        if orc_list:
            for ocr_res in ocr_list:
                ocr_str, ocr_box = ocr_res['recognition_words'], ocr_res['boxes']
                ocr_center_xy = getRectCenterPosition(ocr_box)
                if isPointInBox(ocr_center_xy, (min_xy, max_xy)):
                    box_position = cv2.boundingRect(contour)
                    name_chrs.append(ocr_str[0])
                else:
                    pass

            name = ''.join(name_chrs)

        return box_position, name

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
