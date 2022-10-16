import sys
import numpy as np
import re
from OZEngine.dress_classifier import classification2
from OZEngine.lib.utils import sortContoursByArea, getVertexCnt, getContourCenterPosition, getRectCenterPosition, isPointInBox
from OZEngine.lib.defines import *
from OZEngine.lib.ocr import OCR
from OZEngine.lib.utils import plt_imshow

# (동)정복 검사


class FullDressUniformChecker():
    def __init__(self):
        # hyperparameter
        filter = {
            'uniform': {
                'lower': (12, 0, 0),
                'upper': (197, 255, 116)
            },
            'class_tag': {
                'lower': (140, 120, 50),
                'upper': (190, 255, 255)
            },
            'anchor': {
                'lower': (20, 100, 100),
                'upper': (30, 255, 255)
            },
            'mahura': {
                'lower': (140, 120, 50), 
                'upper': (190, 255, 255)
            }
        }

        self.name_tag_pattern = re.compile('[가-힣]+')

    def name_tag_filter(self, string):
        print('str', string)
        filtered_list = self.name_tag_pattern.findall(string)
        res_string = ''.join(filtered_list)
        return res_string

    def isNameTag(self, contour, position, kind):
        return position == 'left' and kind == 'name_tag' and cv2.contourArea(contour) > 100

    def isClassTag(self, contour, position, kind):
        return position == 'left' and kind == 'class_tag'

    def isAnchor(self, contour, position, kind):
        return kind == 'anchor' and cv2.contourArea(contour) > 100

    def isMahura(self, contour, position, kind):
        return kind == 'mahura'

    def isInShirt(self, contour):
        # 샘브레이 영영 안쪽 && 모서리가 4~5 && 크기가 {hyperParameter} 이상 => (이름표 or 계급장)
        return 3 <= getVertexCnt(contour) <= 10 and cv2.contourArea(contour) > 300

    def checkUniform(self, org_img):
        img = org_img
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        box_position_dic = {}
        component_dic = {}
        masked_img_dic = {}

        # 이름표 체크
        name = 'name'
        contours, sorted_hierarchy, masked_img_dic['shirt'] = self.getMaskedContours(
            img=img, hsv_img=hsv_img, kind='uniform', sort=True)
        box_position, component, masked_img = self.getName(
            img, contours, sorted_hierarchy)
            
        for i, (contour, lev) in enumerate(zip(contours, hierarchy)):
            if i == 0:  # 옷
                cur_node, next_node, prev_node, first_child, parent = lev
                shirt_node = cur_node
                continue

            if parent == shirt_node and self.isInShirt(contour):
                box_position = cv2.boundingRect(contour)
                center_p = getContourCenterPosition(contour)

                x,y,w,h = cv2.boundingRect(contour)
                parts_img = img[y:y+h, x:x+w]

                kind = self.parts_classifier.predict(parts_img)[1]

                position = 'left' if center_p[0] < (W//2) else 'right'
                if not is_name_tag and self.isNameTag(contour, position, kind):
                    # 이름표 OCR
                    if self.name_cache:
                        box_position = cv2.boundingRect(contour)
                        component = 'cached ' + self.name_cache
                    else:
                        ocr_list = OCR(img)
                        self.debug_cnt += 1
                        box_position, component = self.getName(contour, ocr_list)
                        self.name_cache = component

                    # return값에 반영
                    box_position_dic[name] = box_position
                    component_dic[name] = component
                    break

        box_position_dic[name] = component
        component_dic[name] = masked_img

        # 네카치프 / 네카치프링 체크
        name = 'anchor'
        contours, masked_img_dic[name] = self.getMaskedContours(
            img=img, hsv_img=hsv_img, kind=name)
        
        for contour in contours:
            center_p = getContourCenterPosition(contour)
            position = 'left' if center_p[0] < (W//2) else 'right'
            if self.isAnchor(contour, position, kind):
                box_position_dic[name] = cv2.boundingRect(contour)
                component_dic[name] = True
                break

        # 계급장 체크
        name = 'class_tag'
        contours, masked_img_dic[name] = self.getMaskedContours(
            img=img, hsv_img=hsv_img, kind=name)

        for contour in contours:
            center_p = getContourCenterPosition(contour)
            position = 'left' if center_p[0] < (W//2) else 'right'
            if self.isNameTag(contour, position, kind):
                box_position_dic[name] = cv2.boundingRect(contour)
                component_dic[name] = True
                break

        # 마후라 체크
        # name = 'mahura'
        # contours = self.getMaskedContours(
        #     img=img, hsv_img=hsv_img, kind=name, sort=False)
        # box_position_dic[name], component_dic[name] = self.getMahura(
        #     img, contours, None)

        return component_dic, box_position_dic, masked_img_dic
