import cv2

from .dress_checkers import FullDressUniformChecker, NavyServiceUniformChecker
from .dress_classifier import classificate
from .edge_detectors import HED, Morph, RCF
from .person_detectors import PersonDetector  # haarcascade
from .lib.defines import UniformType, Color
from .lib.utils import plt_imshow, histNorm


class OmilZomil:
    def __init__(self):
        self.HED_engine = HED()
        self.morph_engine = Morph()
        print('init!')

        self.full_dress_uniform_checker = FullDressUniformChecker()
        self.navy_service_uniform_checker = NavyServiceUniformChecker()
        self.person_detector = PersonDetector()

        self.kind = None
        self.detect_person = True

    def demo(self, img):
        morphed_edge, ret = self.morph_engine.detect_edge(img)
        hed_edge = self.HED_engine.detect_edge(img, 500, 500)
        plt_imshow(['morphed', 'hed'], [morphed_edge, hed_edge])

    def debug(self, debug_img):
        names, imgs = list(debug_img.keys()), list(debug_img.values())
        plt_imshow(names, imgs)

    def contour2img(self, org_img, contour_dic):
        img = org_img.copy()
        roi_dic = {}

        # cv2.drawContours(img, [contour_dic['shirt']], 0, Color.GREEN, -1)
        for name, contour in contour_dic.items():
            if name != 'shirt' and contour is not None:
                x, y, w, h = cv2.boundingRect(contour_dic[name])
                roi = org_img[y:y+h, x:x+w]
                cv2.rectangle(img, (x, y), (x+w, y+h), Color.PURPLE, 5)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, name, (x, y), font, 3, Color.PURPLE, 5)
                roi_dic[name] = roi

        return img, roi_dic

    def detect(self, img):
        input_img = None

        if self.detect_person:
            input_img, boxed_img = self.person_detector.detect(img)  # 사람인식
            if input_img is None:
                raise Exception("인식가능한 사람이 없습니다!")
        else:
            input_img = img

        hsv_dst, yCrCb_dst = histNorm(input_img)
        input_img = yCrCb_dst
        # hair_segmentation(org) 머리카락인식

        self.kind = UniformType.dic['FULL_DRESS']

        if self.kind is None:
            self.kind = classificate(self.org)  # 복장종류인식 (전투복, 동정복, 샘당)

        if self.kind == UniformType.dic['NAVY_SERVICE']:
            component_dic, contour_dic, masked_img = self.navy_service_uniform_checker.checkUniform(
                input_img)

        elif self.kind == UniformType.dic['FULL_DRESS']:
            component_dic, contour_dic, masked_img = self.full_dress_uniform_checker.checkUniform(
                input_img)

        boxed_img, roi_dic = self.contour2img(input_img, contour_dic)

        return component_dic, boxed_img, roi_dic, masked_img
