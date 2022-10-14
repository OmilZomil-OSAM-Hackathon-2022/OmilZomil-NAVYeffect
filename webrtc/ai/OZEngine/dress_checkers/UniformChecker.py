import cv2
from OZEngine.lib.utils import *
from OZEngine.lib.defines import *
from OZEngine.lib.ocr import OCR
from OZEngine.dress_classifier import classification2
from OZEngine.parts_classifier import PartsClassifier

class UniformChecker:
    def __init__(self, filter, dress_kind):
        self.filter = filter
        self.parts_classifier = PartsClassifier(dress_kind)

    def getMaskedContours(self, img=None, hsv_img=None, kmeans=None, morph=None, kind=None, sort=False):
        lower, upper = self.filter[kind]['lower'], self.filter[kind]['upper']
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

        if ocr_list:
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
            img=roi, hsv_img=hsv_roi, kmeans=True, kind='class_tag')

        classes_n = 0
        for contour in contours:
            if 100 < cv2.contourArea(contour):
                classes_n += 1

        if 1 <= classes_n <= 4:
            class_name = Classes.dic[classes_n]

        return box_position, class_name, masked_img