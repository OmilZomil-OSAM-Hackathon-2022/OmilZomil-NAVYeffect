import cv2, os

from .dress_checkers import FullDressUniformChecker, NavyServiceUniformChecker
from .dress_classifier import DressClassifier
from .edge_detectors import HED, Morph, RCF
from .person_detectors import PersonDetector
from .face_detectors import FaceDetector
from .lib.defines import UniformType, Color
from .lib.utils import plt_imshow, histNorm, box2img


class OmilZomil:
    def __init__(self, resize=None, img_norm_type=None, debug_list=[], save_path=None, train_mode=False):
        self.HED_engine = HED()
        self.morph_engine = Morph()
        self.uniform_checker = None
        self.dress_classifier = DressClassifier()
        self.person_detector = PersonDetector()
        self.face_detector = FaceDetector()
        print('init!')

        self.resize = resize
        self.img_norm_type = img_norm_type
        self.uniform_type = None
        self.debug_list = debug_list
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
        if len(pairs):
            if 'plt' in self.debug_list and self.frame_cnt == 0:
                names, imgs = zip(*pairs)
                plt_imshow([*names], [*imgs])
                
            if 'imwrite' in self.debug_list and self.save_path:
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

        # for demo
        x, y, w, h = info_dic['box_position']['face']
        cv2.rectangle(img, (x, y), (x+w, y+h), Color.FACE_BOX, 5)
        
        for name, box_position in info_dic['box_position'].items():
            if name != 'shirt' and name != 'face' and box_position is not None:
                x, y, w, h = box_position
                roi = org_img[y:y+h, x:x+w]
                
                cv2.rectangle(img, (x, y), (x+w, y+h), Color.PARTS_BOX, 5)
                font = cv2.FONT_HERSHEY_SIMPLEX
                margin = 30
                if name == 'mahura':
                    y -= (10 + margin)
                else:
                    y += h+margin
                
                msg = name.split('_')[0]
                # if name == 'class_tag':
                #     msg += info_dic['component']
                cv2.putText(img, msg, (x, y), font, 1, Color.PARTS_BOX, 3)
                if info_dic.get('probability'):
                    probability = round(info_dic['probability'][name]*100, 2)
                    cv2.putText(img, str(probability) + '%', (x, y+30), font, 1, Color.PARTS_BOX, 3)
                
                roi_dic[name] = roi

        return img, roi_dic

    def detect(self, img):
        if self.resize is not None:
            img = cv2.resize(img, self.resize)
        
        input_img = img
        # 사람인식
        person_box = self.person_detector.detect(img)
        person_base_point = person_box[0]
        person_img = box2img(img, person_box)
        if person_img is None:
            return None
        
        # 얼굴인식
        face_box = self.face_detector.detect(person_img)
        if face_box is None:
            return None

        face_img = box2img(person_img, face_box)

        self.debug({'face':face_img}, msg='roi')
        # 셔츠인식
        h, w = person_img.shape[:2]
        max_y = face_box[1][0]
        shirt_box = ((max_y, 0), (h, w))
        shirt_base_point = shirt_box[0]
        shirt_img = box2img(person_img, shirt_box)
        
        self.debug({'shirt':2}, msg='roi')
        
        # 히스토그램 평활화 여부 확인 후 적용
        if self.img_norm_type:
            histed_img = histNorm(input_img, type=self.img_norm_type)
            # 디버깅 여부 확인
            if 'plt' in self.debug_list:
                plt_imshow(['org', 'histed_img'], [input_img, histed_img])
                input_img = histed_img

        if self.uniform_type is None:
            self.uniform_type = self.dress_classifier.predict(shirt_img)[1]  # 복장종류인식 (전투복, 동정복, 샘당)
            if self.uniform_type == UniformType.dic['NAVY_SERVICE']:
                self.uniform_checker = NavyServiceUniformChecker(self.train_mode)
            elif self.uniform_type == UniformType.dic['FULL_DRESS']:
                self.uniform_checker = FullDressUniformChecker(self.train_mode)
            else:
                return None

        # 옷 종류별로 분기를 나눔
        result_dic = self.uniform_checker.checkUniform(shirt_img)

        base_point = (person_base_point[0] + shirt_base_point[0]), (person_base_point[1] + shirt_base_point[1])
        for name, pos in result_dic['box_position'].items():
            if pos:
                x, y, w, h = pos
                x += base_point[1]
                y += base_point[0]
                result_dic['box_position'][name] = (x, y, w, h)

        
            
        # 최종 debug 여부 확인
        if self.debug_list:
            # for debug
            result_dic['box_position']['face'] = [face_box[0][1], face_box[0][0], face_box[1][1]-face_box[0][1], face_box[1][0]-face_box[0][0]]
            result_dic['box_position']['face'][0] += person_base_point[1]
            result_dic['box_position']['face'][1] += person_base_point[0]

            boxed_img, roi_dic = self.boxImage(input_img, result_dic)
            
            # plt_imshow(['boxed'], [boxed_img])
            self.debug(roi_dic, msg="roi")
            self.debug(result_dic['masked_img'], msg="masked")
            self.debug({"result":boxed_img}, msg="res")
            self.demo(img, result_dic)
            
        self.frame_cnt += 1
        return {'component':result_dic['component'], 'box_position': result_dic['box_position']}