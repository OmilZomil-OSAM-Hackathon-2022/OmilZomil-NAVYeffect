class He:
    def __init__(self):
        self.HED_engine = HED()
        self.org = None
        self.gray = None
        self.edge = None

    def detect(img):
        self.org = img
        # check_person(org) 사람인식
        # hair_segmentation(org) 머리카락인식
        # kind = classification() # 복장종류인식 (전투복, 동정복, 샘당)
        # if kind == '1':
        #   
        # elif kind == '2':
        #   
        # elif kind == '3':
        #   
        pass
    

'''
for test

# load Engine
morph_engine, HED_engine = Morph(), HED()

# get edge image
morphed_edge, ret = morph_engine.detect_edge(org_img)
hed_edge = HED_engine.detect_edge(org_img, 500, 500)
# _, mixed = morph_engine.detect_edge(hed_edge, isEdge=True)

# show
plt_imshow(["morphed", "HED", "morphed ret"], [morphed_edge, hed_edge, ret])
# plt_imshow(["morphed", "HED", "mixed"], [morphed_edge, hed_edge, mixed])

~~~

# dst = cv2.bitwise_or(morphed_edge, hed_edge)
# ndst = cv2.bitwise_not(dst)
# plt_imshow(['dst', 'ndst'], [dst, ndst])
'''