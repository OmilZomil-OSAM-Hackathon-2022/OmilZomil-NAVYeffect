import cv2, os

from .dress_checkers import FullDressUniformChecker, NavyServiceUniformChecker, CombatUniformChecker
from .dress_classifier import DressClassifier
from .edge_detectors import HED, Morph, RCF
from .person_detectors import PersonDetector
from .face_detectors import FaceDetector
from .hair_detectors import HairDetector
from .lib.defines import UniformType, Color
from .lib.utils import plt_imshow, histNorm, box2img, cvtPoint


class OmilZomil:
    def __init__(self, check_person=True, train_mode=False, hed_mode=False, box_padding=0, roi_padding=0):
        if hed_mode:
            self.HED_engine = HED()
            self.morph_engine = Morph()
        self.uniform_checker = None
        self.dress_classifier = DressClassifier()
        self.person_detector = PersonDetector()
        self.face_detector = FaceDetector()
        self.hair_detector = HairDetector()
        print('init!')

        self.hed_mode = hed_mode
        self.uniform_type = None
        self.check_person = check_person
        self.train_mode = train_mode
        self.frame_cnt = 0
        self.base_point = [0, 0]

        self.W = 0
        self.H = 0

        self.box_padding = box_padding
        self.roi_padding = roi_padding

    def addBasePoint(self, box):
        self.base_point[0] += box[0][0]
        self.base_point[1] += box[0][1]

    def applyBasePoint(self, points, method):
        if method == '2':
            p1, p2 = points
            pass 

        elif method == '4':
            x, y, w, h = points
            return x+self.base_point[1], y+self.base_point[0], w, h

    def saveImg(self, img_dic, save_path=""):
        pairs = [(f'{name}', img)
                 for name, img in img_dic.items() if img is not None]
            
        for name, img in pairs:
            parts_dir = os.path.join(save_path, name)

            os.makedirs(parts_dir, exist_ok=True)
            dst_path = os.path.join(parts_dir, str(self.frame_cnt) + '.jpg')
            cv2.imwrite(dst_path, img)

    def boxImage(self, org_img, info_dic, box_padding=0, roi_padding=0, is_roi=False,):
        img = org_img.copy()
        roi_dic = {}

        for name, box_position in info_dic['box_position'].items():
            if name != 'shirt' and box_position is not None:
                x, y, w, h = box_position
                if is_roi:
                    roi_x, roi_y, roi_w, roi_h = x, y, w, h
                    roi_x = max(0, roi_x - roi_padding)
                    roi_y = max(0, roi_y - roi_padding)
                    roi_w = min(self.W, roi_w + (roi_padding*2))
                    roi_h = min(self.H, roi_h + (roi_padding*2))
                    roi = org_img[roi_y:roi_y+roi_h, roi_x:roi_x+roi_w]
                
                x = max(0, x - box_padding)
                y = max(0, y - box_padding)
                w = min(self.W, w + (box_padding*2))
                h = min(self.H, h + (box_padding*2))
                cv2.rectangle(img, (x, y), (x+w, y+h), Color.PARTS_BOX, 5)
                font = cv2.FONT_HERSHEY_SIMPLEX
                margin = 30
                y += -(10+margin) if name == 'muffler' else h+margin
                
                msg = name.split('_')[0]
                cv2.putText(img, msg, (x, y), font, 1, Color.PARTS_BOX, 3)
                if info_dic.get('probability'):
                    probability = round(info_dic['probability'][name]*100, 2)
                    cv2.putText(img, str(probability) + '%', (x, y+30), font, 1, Color.PARTS_BOX, 3)
                if is_roi:
                    roi_dic[name] = roi

        return img, roi_dic

    def detect(self, org_img):
        full_img = org_img.copy()
        img = org_img.copy()
        boxed_img = org_img

        self.W, self.H = boxed_img.shape[:2]

        if self.hed_mode:
            hed_edge = self.HED_engine.detect_edge(img, 500, 500)
            hed_edge_bgr = cv2.cvtColor(hed_edge, cv2.COLOR_GRAY2BGR)
            hed_boxed_img = hed_edge_bgr

        self.base_point = [0, 0]
        # 사람인식
        if self.check_person:
            person_box = self.person_detector.detect(img)
            if person_box is None:
                return {'step':0}
            img = box2img(img, person_box)
            self.addBasePoint(person_box)
        
        self.frame_cnt += 1
        # 얼굴인식
        face_box = self.face_detector.detect(img)
        if face_box is None:
            if self.hed_mode:
                return {'step':1, 'boxed_img':org_img, 'hed_boxed_img':hed_boxed_img}
            else:
                return {'step':1, 'boxed_img':org_img}

        face_x, face_y, face_w, face_h = cvtPoint(face_box, method='2to4')
        face_y += person_box[0][0]
        face_x += person_box[0][1]

        padding = 30
        hair_face_x = max(0, face_x - padding)
        hair_face_y = max(0, face_y - ((padding*3)))
        hair_face_w = min(self.W, face_w + (padding*2))
        hair_face_h = min(self.H, face_h + ((padding*3)))
        hair_roi = full_img[hair_face_y:hair_face_y+hair_face_h, hair_face_x:hair_face_x+hair_face_w]
        
        cv2.rectangle(boxed_img, (face_x, face_y), (face_x+face_w, face_y+face_h), Color.FACE_BOX, 5)
        if self.hed_mode:
            cv2.rectangle(hed_boxed_img, (face_x, face_y), (face_x+face_w, face_y+face_h), Color.FACE_BOX, 5)
        face_img = box2img(img, face_box)

        # 두발인식
        hair_condition = self.hair_detector.detect(hair_roi)

        # 셔츠인식
        h, w = img.shape[:2]
        max_y = face_box[1][0]
        shirt_box = ((max_y, 0), (h, w))
        shirt_img = box2img(img, shirt_box)
        self.addBasePoint(shirt_box)

        # 옷 종류별로 분기를 나눔
        if self.uniform_type is None:
            self.uniform_type = self.dress_classifier.predict(shirt_img)[1]  # 복장종류인식 (전투복, 동정복, 샘당)
            if self.uniform_type == UniformType.dic['NAVY_SERVICE']:
                self.uniform_checker = NavyServiceUniformChecker(self.train_mode)
            elif self.uniform_type == UniformType.dic['FULL_DRESS']:
                self.uniform_checker = FullDressUniformChecker(self.train_mode)
            elif self.uniform_type == UniformType.dic['COMBAT']:
                self.uniform_checker = CombatUniformChecker(self.train_mode)
            else:
                return {'step':2, 'boxed_img':org_img}

        # 복장검사모델
        result_dic = self.uniform_checker.checkUniform(shirt_img)

        for name, pos in result_dic['box_position'].items():
            if pos:
                result_dic['box_position'][name] = self.applyBasePoint(pos, method='4')
            
        boxed_img, roi_dic = self.boxImage(boxed_img, result_dic, box_padding=self.box_padding, roi_padding=self.roi_padding, is_roi=True)

        if self.hed_mode:
            hed_boxed_img, _ = self.boxImage(hed_boxed_img, result_dic)

        if self.hed_mode:
            return {'step':3, 'hair_condition':hair_condition, 'shirt_img':shirt_img, 'boxed_img':boxed_img, 'dress_kind':self.uniform_type,'hed_boxed_img': hed_boxed_img, 'component':result_dic['component'], 'roi':roi_dic}
        else:
            return {'step':3, 'hair_condition':hair_condition ,'shirt_img':shirt_img, 'boxed_img':boxed_img, 'dress_kind':self.uniform_type, 'component':result_dic['component'], 'roi':roi_dic}
