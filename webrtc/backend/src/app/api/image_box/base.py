
UNIFORM_PARTS = {
    'blue' : [ "hair", "name_tag", "rank_tag" ], # 샘당
    'black' : [ "hair", "name_tag", "rank_tag", "muffler", "neck" ], # 정복
    'green' : [ "hair", "name_tag", "rank_tag", "flag" ], # 군복
}
class BaseImageBox:

    def __init__(self, uniform, guardhouse):
        self.inspection = {
            'guardhouse': guardhouse,  # 위병소
            'affiliation' : 1,      # 소속
            'rank' : 1,             # 계급
            'name' : "",            # 이름
            'uniform' : uniform,          # 복장
        }
        # 파츠 생성
        self.parts = {key: False for key in UNIFORM_PARTS[uniform]} # 유니폼에 따라 파츠 리스트 생성

        # 이미지
        self.main_image = None
        self.parts_images = {}

