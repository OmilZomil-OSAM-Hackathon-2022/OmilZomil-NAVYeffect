import cv2

from .dress_checkers import FullDressUniformChecker, NavyServiceUniformChecker
from .dress_classifier import classificate, classification2
from .edge_detectors import HED, Morph, RCF
from .person_detectors import PersonDetector
from .lib.defines import UniformType, Color
from .lib.utils import plt_imshow, histNorm


class OmilZomil:
    def __init__(self, resize=None, img_norm_type=None, uniform_type=None, mode='real'):
        self.HED_engine = HED()
        self.morph_engine = Morph()
        self.full_dress_uniform_checker = FullDressUniformChecker()
        self.navy_service_uniform_checker = NavyServiceUniformChecker()
        self.person_detector = PersonDetector()
        print('init!')

        self.resize = resize
        self.img_norm_type = img_norm_type
        self.uniform_type = UniformType.dic[uniform_type]
        self.mode = mode

    def demo(self, img):
        morphed_edge, ret = self.morph_engine.detect_edge(img)
        hed_edge = self.HED_engine.detect_edge(img, 500, 500)
        plt_imshow(['morphed', 'hed'], [morphed_edge, hed_edge])

    def debug(self, debug_img):
        pairs = [(name, img)
                 for name, img in debug_img.items() if img is not None]
        if len(pairs):
            names, imgs = zip(*pairs)
            plt_imshow([*names], [*imgs])

    def boxImage(self, org_img, box_position_dic):
        img = org_img.copy()
        roi_dic = {}

        # cv2.drawContours(img, [contour_dic['shirt']], 0, Color.GREEN, -1)
        for name, box_position in box_position_dic.items():
            if name != 'shirt' and box_position is not None:
                x, y, w, h = box_position
                roi = org_img[y:y+h, x:x+w]
                cv2.rectangle(img, (x, y), (x+w, y+h), Color.PURPLE, 5)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, name, (x, y), font, 3, Color.PURPLE, 5)
                roi_dic[name] = roi

        return img, roi_dic

    def detect(self, img):
        input_img = None

        if self.resize is not None:
            img = cv2.resize(img, resize)

        input_img, boxed_img = self.person_detector.detect(img)  # 사람인식
        if input_img is None:
            raise Exception("인식가능한 사람이 없습니다!")

        # input_img = classification2(input_img)
        if self.img_norm_type:
            histed_img = histNorm(input_img, type=self.img_norm_type)
            if self.mode == 'debug':
                plt_imshow(['org', 'histed_img'], [input_img, histed_img])
                input_img = histed_img

        if self.uniform_type is None:
            self.uniform_type = classificate(self.org)  # 복장종류인식 (전투복, 동정복, 샘당)

        if self.uniform_type == UniformType.dic['NAVY_SERVICE']:
            component_dic, box_position_dic, masked_img_dic = self.navy_service_uniform_checker.checkUniform(
                input_img)

        elif self.uniform_type == UniformType.dic['FULL_DRESS']:
            component_dic, box_position_dic, masked_img_dic = self.full_dress_uniform_checker.checkUniform(
                input_img)

        if self.mode == 'debug':
            boxed_img, roi_dic = self.boxImage(input_img, box_position_dic)
            plt_imshow(['boxed'], [boxed_img])
            self.debug(roi_dic)
            self.debug(masked_img_dic)
        return component_dic, box_position_dic
