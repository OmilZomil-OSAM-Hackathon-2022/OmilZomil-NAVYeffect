import sys
import numpy as np
from lib.utils import sortContoursByArea, getVertexCnt, getContourCenterPosition, getRectCenterPosition, isPointInBox
from lib.defines import *
from lib.ocr import OCR
from lib.utils import plt_imshow

# (동)정복 검사


class FullDressUniformChecker():
    def __init__(self):
        # hyperparameter
        self.uniform_filter = {'lower': (12, 0, 0), 'upper': (197, 255, 116)}
        self.anchor_filter = {'lower': (20, 100, 100), 'upper': (30, 255, 255)}
        self.classes_filter = {
            'lower': (140, 120, 50), 'upper': (190, 255, 255)}
        self.mahura_filter = {
            'lower': (140, 120, 50), 'upper': (190, 255, 255)}

    def getMaskedContours(self, img=None, hsv_img=None, morph=None, kind=None, sort=True):
        if hsv_img is None:
            hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        if kind == 'uniform':
            lower, upper = self.uniform_filter['lower'], self.uniform_filter['upper']
        elif kind == 'classes':
            lower, upper = self.classes_filter['lower'], self.classes_filter['upper']
        elif kind == 'anchor':
            lower, upper = self.anchor_filter['lower'], self.anchor_filter['upper']
        else:
            pass

        mask = cv2.inRange(hsv_img, lower, upper)

        if morph == 'erode':
            kernel = np.ones((3, 3), np.uint8)
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
            return sorted_contours, sorted_hierarchy, masked_img
        else:
            contours, _ = cv2.findContours(
                mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            return contours, masked_img

    def getName(self, img, contours, hierarchy):
        h, w = img.shape[:2]
        shirt_contour, res_box_position, res_content = None, None, None
        ocr_list = OCR(img)

        # 이름표
        shirt_node = None
        for i, (contour, lev) in enumerate(zip(contours, hierarchy)):
            cur_node, next_node, prev_node, first_child, parent = lev
            if i == 0:  # 정복
                shirt_contour = contour
                shirt_node = cur_node
                continue

            # 정복 영영 안쪽 && 모서리가 4~5 && 크기가 {hyperParameter} 이상 => (이름표)
            # 이름표 체크
            if not res_content and parent == shirt_node and 4 <= getVertexCnt(contour) <= 5 and cv2.contourArea(contour) > 300:
                center_p = getContourCenterPosition(contour)
                max_xy, min_xy = np.max(contour, axis=0)[
                    0], np.min(contour, axis=0)[0]

                # 이름표 체크
                if center_p[0] < (w//2):
                    name_chrs = []
                    for ocr_res in ocr_list:
                        ocr_str, ocr_box = ocr_res['recognition_words'], ocr_res['boxes']
                        p1, p2, p3, p4 = ocr_box
                        (x1, y1), (x2, y2) = p1, p3
                        if x2 < w//2:
                            roi = img[y1:y2, x1:x2]

                            ocr_center_xy = getRectCenterPosition(ocr_box)
                            if isPointInBox(ocr_center_xy, (min_xy, max_xy)):
                                name_chrs.append(ocr_str[0])
                                cv2.rectangle(img, p1, p3, Color.GREEN, 3)
                            else:
                                pass
                                # cv2.rectangle(img, p1, p3, Color.RED, 3)
                    res_box_position, res_content = cv2.boundingRect(
                        contour), ''.join(name_chrs)
        return cv2.boundingRect(shirt_contour), res_box_position, res_content

    def getClasses(self, masked_img, contours, hierarchy):
        h, w = masked_img.shape[:2]
        res_box_position, res_content, small_mask = None, None, None

        box_position = None
        for contour in contours:  # contours : 계급장이라 판별되는 contour
            if cv2.contourArea(contour) > 300:
                center_p = getContourCenterPosition(contour)
                if center_p[0] < (w//2) and not res_content:
                    box_position = cv2.boundingRect(contour)
                    x, y, w, h = box_position
                    roi = masked_img[y:y+h, x:x+w]

                    small_contours, small_mask = self.getMaskedContours(
                        img=roi, morph='erode', kind='classes', sort=False)

                    classes_n = 0
                    for small_contour in small_contours:
                        if 10 < cv2.contourArea(small_contour):
                            classes_n += 1
                            cv2.drawContours(
                                small_mask, [small_contour], 0, Color.BLUE, 1)

                    if 1 <= classes_n <= 4:
                        res_box_position, res_content = box_position, Classes.dic[classes_n]
        return res_box_position, res_content, small_mask

    def getAnchor(self, contours, hierarchy):
        res_box_position, res_content = None, None
        for contour in contours:
            if cv2.contourArea(contour) > 100:
                center_p = getContourCenterPosition(contour)
                if not res_content:
                    res_box_position, res_content = cv2.boundingRect(
                        contour), True
        return res_box_position, res_content

    def getMahura(self, contours, hierarchy):
        res_box_position, res_content = None, None
        for contour in contours:
            if cv2.contourArea(contour) > 300:
                center_p = getContourCenterPosition(contour)
                if not res_content:
                    res_box_position, res_content = cv2.boundingRect(
                        contour), True
        return res_box_position, res_content

    def checkUniform(self, org_img):
        img = org_img
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # half_line_p1, half_line_p2 = (w//2, 0), (w//2, h)
        # cv2.line(img, half_line_p1, half_line_p2, Color.WHITE, 5)

        box_position_dic = {}
        component_dic = {}
        masked_img = {}

        # 이름표 체크
        name = 'name'
        contours, sorted_hierarchy, masked_img[name] = self.getMaskedContours(
            img=img, hsv_img=hsv_img, kind='uniform', sort=True)
        box_position_dic['shirt'], box_position_dic[name], component_dic[name] = self.getName(
            img, contours, sorted_hierarchy)

        # 네카치프 / 네카치프링 체크
        name = 'anchor'
        contours, masked_img[name] = self.getMaskedContours(
            img=img, hsv_img=hsv_img, kind=name, sort=False)
        box_position_dic[name], component_dic[name] = self.getAnchor(
            contours, None)

        # 계급장 체크
        name = 'classes'
        contours, masked_img[name] = self.getMaskedContours(
            img=img, hsv_img=hsv_img, kind=name, sort=False)
        box_position_dic[name], component_dic[name], masked_img['classes_roi'] = self.getClasses(
            img, contours, None)

        # 마후라 체크
        # name = 'mahura'
        # contours = self.getMaskedContours(
        #     img=img, hsv_img=hsv_img, kind=name, sort=False)
        # box_position_dic[name], component_dic[name] = self.getMahura(
        #     img, contours, None)

        return component_dic, box_position_dic, masked_img
