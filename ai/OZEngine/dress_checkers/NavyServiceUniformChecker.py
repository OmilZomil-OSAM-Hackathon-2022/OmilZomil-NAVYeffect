from .UniformChecker import UniformChecker
from OZEngine.lib.utils import *
from OZEngine.lib.defines import *
from OZEngine.lib.ocr import OCR
from OZEngine.dress_classifier import classification2


# 샘브레이 검사
class NavyServiceUniformChecker(UniformChecker):
    def __init__(self, train_mode):
        # hyperparameter
        filter = {
            'uniform': {
                'lower': (30, 20, 0),
                'upper': (255, 255, 255)
            },
            'rank_tag': {
                'lower': (0, 150, 90),
                'upper': (255, 255, 255)
            }
        }

        super().__init__(filter, 'navy_service_uniform', train_mode)
        self.name_cache = None
        self.debug_cnt = 0

        self.result_dic = {'component':{}, 'box_position':{}, 'masked_img':{}, 'probability':{}}


    def isNameTag(self, contour, position, kind):
        return position == 'left' and kind == 'name_tag'

    def isClassTag(self, contour, position, kind):
        return position == 'right' and kind == 'rank_tag'

    def isInShirt(self, contour):
        # 샘브레이 영영 안쪽 && 모서리가 4~5 && 크기가 {hyperParameter} 이상 => (이름표 or 계급장)
        return 3 <= getVertexCnt(contour) <= 10 and cv2.contourArea(contour) > 300

    def checkUniform(self, org_img):
        img = org_img
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        H, W = img.shape[: 2]

        self.result_dic = {'component':{}, 'box_position':{}, 'masked_img':{}, 'probability':{}} 
        # 샘당 filter
        contours, hierarchy, self.result_dic['masked_img']['shirt'] = self.getMaskedContours(
            img=img, hsv_img=hsv_img, kind='uniform', sort=True)

        # 이름표, 계급장 체크
        for i, (contour, lev) in enumerate(zip(contours, hierarchy)):
            is_rank_tag = self.result_dic['component'].get('rank_tag')
            is_name_tag = self.result_dic['component'].get('name_tag')

            if is_name_tag and is_rank_tag:
                break

            cur_node, next_node, prev_node, first_child, parent = lev
            if i == 0:  # 셈브레이
                shirt_node = cur_node
                continue

            # 파츠
            if parent == shirt_node and self.isInShirt(contour):
                box_position = cv2.boundingRect(contour)
                center_p = getContourCenterPosition(contour)

                # 파츠 분류
                
                x,y,w,h = cv2.boundingRect(contour)
                parts_img = img[y:y+h, x:x+w]

                
                kind = self.parts_classifier.predict(parts_img)[1]

                position = 'left' if center_p[0] < (W//2) else 'right'
                # 이름표 체크
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
                    self.result_dic['box_position']['name_tag'] = box_position
                    self.result_dic['component']['name_tag'] = component

                # 계급장 체크
                elif not is_rank_tag and self.isClassTag(contour, position, kind):
                    box_position, component, masked_img = self.getClasses(
                        img, hsv_img, contour)

                    # return값에 반영
                    self.result_dic['box_position']['rank_tag'] = box_position
                    self.result_dic['component']['rank_tag'] = component
                    self.result_dic['masked_img']['rank_tag'] = masked_img


        return self.result_dic

