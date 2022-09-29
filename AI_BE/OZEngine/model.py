import cv2

from .dress_checkers import FullDressUniformChecker, NavyServiceUniformChecker
from .dress_classifier import classificate
from .edge_detectors import HED, Morph, RCF
from .person_detectors import PersonDetector  # haarcascade
from .lib.defines import UniformType, Color
from .lib.utils import plt_imshow


class OmilZomil:
    def __init__(self):
        # self.HED_engine = HED()
        print('init!')
        self.org = None
        self.gray = None
        self.edge = None

        self.full_dress_uniform_checker = FullDressUniformChecker()
        self.navy_service_uniform_checker = NavyServiceUniformChecker()
        self.person_detector = PersonDetector()

        self.kind = None

        self.detect_person = False

        self.person_roi = None

    def debug(self, debug_img):
        names, imgs = list(debug_img.keys()), list(debug_img.values())
        plt_imshow(names, imgs)

    def contour2img(self, contour_dic):
        img = self.org.copy()

        cv2.drawContours(img, [contour_dic['shirt']], 0, Color.GREEN, -1)
        for name, contour in contour_dic.items():
            if name != 'shirt':
                x, y, w, h = cv2.boundingRect(contour_dic[name])
                roi = self.org[y:y+h, x:x+w]
                cv2.rectangle(img, (x, y), (x+w, y+h), Color.PURPLE, 5)
                font = cv2.FONT_HERSHEY_SIMPLEX
                print(name, (x, y))
                cv2.putText(img, name, (x, y), font, 3, Color.PURPLE, 5)

        plt_imshow(['res'], [img])

    def detect(self, img):
        self.org = img

        if self.detect_person:
            self.person_roi, boxed_img = self.person_detector.detect(
                self.org)  # 사람인식
        else:
            self.person_roi = self.org

        if self.person_roi is None:
            raise Exception("인식가능한 사람이 없습니다!")

        # hair_segmentation(org) 머리카락인식
        # kind = classificate(self.org)  # 복장종류인식 (전투복, 동정복, 샘당)

        self.kind = UniformType.dic['FULL_DRESS']

        if self.kind == UniformType.dic['NAVY_SERVICE']:
            component_dic, contour_dic = self.navy_service_uniform_checker.checkUniform(
                self.person_roi)

        elif self.kind == UniformType.dic['FULL_DRESS']:
            component_dic, contour_dic, debug_img = self.full_dress_uniform_checker.checkUniform(
                self.person_roi)

        print(component_dic)
        self.contour2img(contour_dic)
        self.debug(debug_img)
        return None
