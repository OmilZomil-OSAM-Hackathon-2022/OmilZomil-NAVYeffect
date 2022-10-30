import cv2


class HairCondition:
    dic = {'GOOD':1 , 'BAD': 0}

class UniformType:
    dic = {'FULL_DRESS': 1, 'NAVY_SERVICE': 2, 'COMBAT': 3,}


class Classes:
    dic = {1: '이병', 2: '일병', 3: '상병', 4: '병장'}


class Color:
    BLUE = (255, 0, 0)
    GREEN = (0, 255, 0)
    RED = (0, 0, 255)
    PURPLE = (173, 119, 137)
    WHITE = (255, 255, 255)
    PARTS_BOX = (61, 255, 45)
    FACE_BOX = (145, 85, 235)

class FullDressUniformMask:
    pass