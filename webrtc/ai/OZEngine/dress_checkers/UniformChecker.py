import cv2
from OZEngine.lib.utils import *
from OZEngine.lib.defines import *
from OZEngine.lib.ocr import OCR
from OZEngine.dress_classifier import classification2
from OZEngine.parts_classifier import PartsClassifier

class UniformChecker:
    def __init__(self, filter, dress_kind, train_mode=False):
        self.filter = filter
        self.train_mode = train_mode
        self.name_tag_pattern = re.compile('[가-힣]+')
        if train_mode is False:
            self.parts_classifier = PartsClassifier(dress_kind)

    def name_tag_filter(self, string):
        filtered_list = self.name_tag_pattern.findall(string)
        res_string = ''.join(filtered_list)
        return res_string

    def getMaskedContours(self, img=None, hsv_img=None, kmeans=None, morph=None, kind=None, sort=False, reverse=False):
        lower, upper = self.filter[kind]['lower'], self.filter[kind]['upper']
        mask = cv2.inRange(hsv_img, lower, upper)

        if reverse:
            mask = cv2.bitwise_not(mask)

        if kmeans:
            img_s = classification2(img, 10)
            img = classification2(img, 10)

        if morph == 'erode':
            org_mask = mask.copy()

            k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 2))
            mask = cv2.erode(org_mask, k, iterations=2)

            plt_imshow(['org_mask', 'maskk', 'm2'], [org_mask, mask])

        if morph == 'erode2dilate':
            org_mask = mask.copy()

            k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 2))
            mask = cv2.erode(org_mask, k, iterations=2)
            k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 2))
            mask = cv2.dilate(mask, k)
            mask = cv2.dilate(mask, k)

            plt_imshow(['org_mask', 'maskk', 'm2'], [org_mask, mask])

        masked_img = cv2.bitwise_and(img, img, mask=mask)

        if sort:
            contours, hierarchy = cv2.findContours(
                mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
            if hierarchy is None:
                return None, None, None
            sorted_contours, sorted_hierarchy = sortContoursByArea(
                contours, hierarchy)
            return sorted_contours, sorted_hierarchy, mask
        else:
            contours, _ = cv2.findContours(
                mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            return contours, masked_img

    def getName(self, contour, ocr_list=[], is_strict=False):
        max_xy, min_xy = np.max(contour, axis=0)[
            0], np.min(contour, axis=0)[0]

        box_position, name = None, None
        ocr_min_x, ocr_min_y = 1e9, 1e9
        ocr_max_x, ocr_max_y = -1, -1
        name_chrs = []
        if ocr_list:
            sorted_orc_list = sorted(ocr_list, key=lambda ocr_res: ocr_res['boxes'][0][0])
            for ocr_res in sorted_orc_list:
                ocr_str_list, ocr_box = ocr_res['recognition_words'], ocr_res['boxes']
                if ocr_str_list:
                    ocr_str = ocr_str_list[0]
                else:
                    ocr_str = ''
                ocr_str = self.name_tag_filter(ocr_str)
                ocr_center_xy = getRectCenterPosition(ocr_box)
                if isPointInBox(ocr_center_xy, (min_xy, max_xy)):
                    p1, _, p3, _ = ocr_box
                    ocr_min_x, ocr_max_y = min(ocr_min_x, p1[0]), max(ocr_max_y, p1[1])
                    ocr_max_x, ocr_min_y = max(ocr_max_x, p3[0]), min(ocr_min_y, p3[1])
                    
                    
                    box_position = cv2.boundingRect(contour)
                    name_chrs.append(ocr_str)
                else:
                    pass

            name = ''.join(name_chrs)
        if is_strict:
            return (ocr_min_x, ocr_min_y, ocr_max_x - ocr_min_x, ocr_max_y - ocr_min_y), name
        else:
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
            img=roi, hsv_img=hsv_roi, kind='class_tag')

        classes_n = 0
        for contour in contours:
            if 100 < cv2.contourArea(contour):
                classes_n += 1

        if 1 <= classes_n <= 4:
            class_name = Classes.dic[classes_n]

        return box_position, class_name, masked_img