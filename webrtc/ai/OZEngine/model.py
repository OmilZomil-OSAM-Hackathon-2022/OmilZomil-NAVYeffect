import cv2, os

from .dress_checkers import FullDressUniformChecker, NavyServiceUniformChecker
from .dress_classifier import DressClassifier
from .edge_detectors import HED, Morph, RCF
from .person_detectors import PersonDetector
from .face_detectors import FaceDetector
from .lib.defines import UniformType, Color
from .lib.utils import plt_imshow, histNorm, box2img


class OmilZomil:
    def __init__(self, resize=None, check_person=True, save_path=None, train_mode=False):
        self.HED_engine = HED()
        self.morph_engine = Morph()
        self.uniform_checker = None
        self.dress_classifier = DressClassifier()
        self.person_detector = PersonDetector()
        self.face_detector = FaceDetector()
        print('init!')

        self.resize = resize
        self.uniform_type = None
        self.check_person = check_person
        self.save_path = save_path
        self.train_mode = train_mode
        self.frame_cnt = 0

    def demo(self, img, info_dic=None):
        # morphed_edge, ret = self.morph_engine.detect_edge(img)
        hed_edge = self.HED_engine.detect_edge(img, 500, 500)
        # self.debug({'demo':morphed_edge}, msg='morphed')
        if info_dic is not None:
            hed_edge_bgr = cv2.cvtColor(hed_edge, cv2.COLOR_GRAY2BGR)
            hed_boxed_img, roi_dic = self.boxImage(hed_edge_bgr, info_dic)
            self.debug({'demo':hed_boxed_img}, msg='boxed_hed')
        self.debug({'demo':hed_edge}, msg='hed')
        

    def debug(self, debug_img, msg=""):
        pairs = [(f'{msg} - {name}', img)
                 for name, img in debug_img.items() if img is not None]
            
        for name, img in pairs:
            name = name.split(' - ')[1]
            parts_dir = os.path.join(self.save_path, name)
            if msg:
                parts_dir = os.path.join(parts_dir, msg)
            os.makedirs(parts_dir, exist_ok=True)
            dst_path = os.path.join(parts_dir, str(self.frame_cnt) + '.jpg')
            cv2.imwrite(dst_path, img)

    def boxImage(self, org_img, info_dic):
        img = org_img.copy()
        roi_dic = {}

        for name, box_position in info_dic['box_position'].items():
            if name != 'shirt' and box_position is not None:
                x, y, w, h = box_position
                roi = org_img[y:y+h, x:x+w]
                
                cv2.rectangle(img, (x, y), (x+w, y+h), Color.PARTS_BOX, 5)
                font = cv2.FONT_HERSHEY_SIMPLEX
                margin = 30
                if name == 'muffler':
                    y -= (10 + margin)
                else:
                    y += h+margin
                
                msg = name.split('_')[0]
                cv2.putText(img, msg, (x, y), font, 1, Color.PARTS_BOX, 3)
                if info_dic.get('probability'):
                    probability = round(info_dic['probability'][name]*100, 2)
                    cv2.putText(img, str(probability) + '%', (x, y+30), font, 1, Color.PARTS_BOX, 3)
                
                roi_dic[name] = roi

        return img, roi_dic

    def detect(self, org_img):
        if self.resize is not None:
            img = cv2.resize(img, self.resize)
        
        img = org_img.copy()
        boxed_img = org_img

        base_point = [0, 0]
        # 사람인식
        if self.check_person:
            person_box = self.person_detector.detect(img)
            if person_box is None:
                if self.debug_list:
                    self.frame_cnt += 1
                return None
            base_point[0] += person_box[0][0]
            base_point[1] += person_box[0][1]

            img = box2img(img, person_box)
        
        
        # 얼굴인식
        face_box = self.face_detector.detect(img)
        if face_box is None:
            return {'boxed_img':org_img}

        x,y,w,h = face_box[0][1], face_box[0][0], face_box[1][1]-face_box[0][1], face_box[1][0]-face_box[0][0]
        y += person_box[0][0]
        x += person_box[0][1]
        cv2.rectangle(boxed_img, (x, y), (x+w, y+h), Color.FACE_BOX, 5)
        face_img = box2img(img, face_box)
        self.debug({'face':face_img}, msg='roi')


        # 셔츠인식
        h, w = img.shape[:2]
        max_y = face_box[1][0]
        shirt_box = ((max_y, 0), (h, w))
        base_point[0] += shirt_box[0][0]
        base_point[1] += shirt_box[0][1]
        shirt_img = box2img(img, shirt_box)
        
        self.debug({'shirt':shirt_img}, msg='roi')

        # 옷 종류별로 분기를 나눔
        if self.uniform_type is None:
            self.uniform_type = self.dress_classifier.predict(shirt_img)[1]  # 복장종류인식 (전투복, 동정복, 샘당)
            if self.uniform_type == UniformType.dic['NAVY_SERVICE']:
                self.uniform_checker = NavyServiceUniformChecker(self.train_mode)
            elif self.uniform_type == UniformType.dic['FULL_DRESS']:
                self.uniform_checker = FullDressUniformChecker(self.train_mode)
            else:
                return None

        # 복장검사모델
        result_dic = self.uniform_checker.checkUniform(shirt_img)

        for name, pos in result_dic['box_position'].items():
            if pos:
                x, y, w, h = pos
                x += base_point[1]
                y += base_point[0]
                result_dic['box_position'][name] = (x, y, w, h)

            
        boxed_img, roi_dic = self.boxImage(boxed_img, result_dic)
            
        self.frame_cnt += 1
        return {'boxed_img':boxed_img, 'component':result_dic['component'], 'roi':roi_dic}