import cv2

from .dress_checkers import FullDressUniformChecker, NavyServiceUniformChecker
from .dress_classifier import classificate
from .edge_detectors import HED, Morph, RCF
from .person_detectors import PersonDetector  # haarcascade
from .lib.defines import UniformType, Color
from .lib.utils import plt_imshow


class OmilZomil:
    def __init__(self):
        self.HED_engine = HED()
        print('init!')

        self.full_dress_uniform_checker = FullDressUniformChecker()
        self.navy_service_uniform_checker = NavyServiceUniformChecker()
        self.person_detector = PersonDetector()

        self.kind = None
        self.detect_person = True

    def debug(self, debug_img):
        names, imgs = list(debug_img.keys()), list(debug_img.values())
        plt_imshow(names, imgs)

    def contour2img(self, org_img, contour_dic):
        img = org_img.copy()
        roi_dic = {}

        # cv2.drawContours(img, [contour_dic['shirt']], 0, Color.GREEN, -1)
        for name, contour in contour_dic.items():
            if name != 'shirt':
                x, y, w, h = cv2.boundingRect(contour_dic[name])
                roi = org_img[y:y+h, x:x+w]
                cv2.rectangle(img, (x, y), (x+w, y+h), Color.PURPLE, 5)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, name, (x, y), font, 3, Color.PURPLE, 5)
                roi_dic[name] = roi

        return img, roi_dic

    def detect(self, img):
        person_roi = None
        if self.detect_person:
            person_roi, boxed_img = self.person_detector.detect(img)  # 사람인식

        if person_roi is None:
            raise Exception("인식가능한 사람이 없습니다!")

        # hair_segmentation(org) 머리카락인식
        # kind = classificate(self.org)  # 복장종류인식 (전투복, 동정복, 샘당)

        self.kind = UniformType.dic['FULL_DRESS']

        if self.kind == UniformType.dic['NAVY_SERVICE']:
            component_dic, contour_dic = self.navy_service_uniform_checker.checkUniform(
                person_roi)

        elif self.kind == UniformType.dic['FULL_DRESS']:
            component_dic, contour_dic, debug_img = self.full_dress_uniform_checker.checkUniform(
                person_roi)

        if self.detect_person:
            boxed_img, roi_dic = self.contour2img(person_roi, contour_dic)
        else:
            boxed_img, roi_dic = self.contour2img(img, contour_dic)

        return component_dic, boxed_img, roi_dic
