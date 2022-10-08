import cv2, os

from .dress_checkers import FullDressUniformChecker, NavyServiceUniformChecker
from .dress_classifier import classificate, classification2
from .edge_detectors import HED, Morph, RCF
from .person_detectors import PersonDetector
from .face_detectors import FaceDetector
from .lib.defines import UniformType, Color
from .lib.utils import plt_imshow, histNorm, box2img


class OmilZomil:
    def __init__(self, resize=None, img_norm_type=None, uniform_type=None, debug_list=[], save_path=None):
        self.HED_engine = HED()
        self.morph_engine = Morph()
        self.full_dress_uniform_checker = FullDressUniformChecker()
        self.navy_service_uniform_checker = NavyServiceUniformChecker()
        self.person_detector = PersonDetector()
        self.face_detector = FaceDetector()
        print('init!')

        self.resize = resize
        self.img_norm_type = img_norm_type
        self.uniform_type = UniformType.dic[uniform_type]
        self.debug_list = debug_list
        
        self.frame_cnt = 0

    def demo(self, img):
        morphed_edge, ret = self.morph_engine.detect_edge(img)
        hed_edge = self.HED_engine.detect_edge(img, 500, 500)
        plt_imshow(['morphed', 'hed'], [morphed_edge, hed_edge])

    def debug(self, debug_img, msg=""):
        pairs = [(f'{msg} - {name}', img)
                 for name, img in debug_img.items() if img is not None]
        if len(pairs):
            if 'imwrite' in self.debug_list and self.save_path:
                for name, img in pairs:
                    parts_dir = os.path.join(self.path, name)
                    if msg:
                        parts_dir = os.path.join(parts_dir, msg)
                    dst_path = os.path.join(parts_dir, self.frame_cnt)
                    cv2.imwrite(dst_path, img)
            if 'plt' in self.debug_list:
                names, imgs = zip(*pairs)
                plt_imshow([*names], [*imgs])
                

    def boxImage(self, org_img, box_position_dic):
        img = org_img.copy()
        roi_dic = {}
        
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
        if self.resize is not None:
            img = cv2.resize(img, self.resize)
        
        input_img = img
        plt_imshow('img', img)
        # 사람인식
        person_box = self.person_detector.detect(img)
        person_base_point = person_box[0]
        person_img = box2img(img, person_box)
        if person_img is None:
            raise Exception("인식가능한 사람이 없습니다!")
        
        # 얼굴인식
        face_box = self.face_detector.detect(person_img)
        face_img = box2img(person_img, face_box)
        
        # 셔츠인식
        w, h = person_img.shape[:2]
        max_y = face_box[1][0]
        shirt_box = ((max_y, 0), (h, w))
        shirt_base_point = shirt_box[0]
        shirt_img = box2img(person_img, shirt_box)
        plt_imshow('shirt', shirt_img)
        
        # 히스토그램 평활화 여부 확인 후 적용
        if self.img_norm_type:
            histed_img = histNorm(input_img, type=self.img_norm_type)
            # 디버깅 여부 확인
            if self.debug_list == 'debug':
                plt_imshow(['org', 'histed_img'], [input_img, histed_img])
                input_img = histed_img

        if self.uniform_type is None:
            self.uniform_type = classificate(self.org)  # 복장종류인식 (전투복, 동정복, 샘당)

        # 옷 종류별로 분기를 나눔
        if self.uniform_type == UniformType.dic['NAVY_SERVICE']:
            component_dic, box_position_dic, masked_img_dic = self.navy_service_uniform_checker.checkUniform(
                shirt_img)

        elif self.uniform_type == UniformType.dic['FULL_DRESS']:
            component_dic, box_position_dic, masked_img_dic = self.full_dress_uniform_checker.checkUniform(
                shirt_img)

        base_point = (person_base_point[0] + shirt_base_point[0]), (person_base_point[1] + shirt_base_point[1])
        for name, pos in box_position_dic.items():
            x, y, w, h = pos
            x += base_point[1]
            y += base_point[0]
            box_position_dic[name] = (x, y, w, h)
            
        # 최종 debug 여부 확인
        if self.debug_list:
            boxed_img, roi_dic = self.boxImage(input_img, box_position_dic)
            plt_imshow(['boxed'], [boxed_img])
            self.debug(roi_dic, msg="roi")
            self.debug(masked_img_dic, msg="masked")
        return component_dic, box_position_dic
