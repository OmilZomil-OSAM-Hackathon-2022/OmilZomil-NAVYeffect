


class ImageBox:
    def __init__(self, ai, guardhouse):
        self.ai = ai
        # defualt 값 지정
        self.inspection = {
            'guardhouse': guardhouse,  # 위병소
            'affiliation' : 1,      # 소속
            'rank' : 1,             # 계급
            'name' : "",            # 이름
            'uniform' : 1,          # 복장
        }
        self.parts = {} # 기타 파츠
        # 이미지 관리
        self.main_image = None
        self.parts_image = {}
        self.old_image_count = 0
        # 데이터 갱신 유무
        self.is_update = False
        self.parts_update = []

    
    def get_inspection(self):
        return self.inspection
    
    def get_parts(self):
        return self.parts
    

    def image_process(self, image):
        report = self.ai.detect(org_img=image)
        print(report)
        return report

    def is_best_image(self, report):
        if len(report['component']) > self.old_image_count:
            self.image_update = report['boxed_img']

    def find_info(self, component : dict):
        """
        탐지된 파츠로 유니폼과 소속을 찾는 함수
        """
        if "flag" in component.keys():
            self.inspection['uniform'] = "green"
            self.inspection['affiliation'] = "육군"
        elif "muffler" in component.keys():
            self.inspection['uniform'] = "black"
            self.inspection['affiliation'] = "해군"
        elif "muffler" in component.keys():
            self.inspection['uniform'] = "black"
            self.inspection['affiliation'] = "해군"
        else:
            # 일단 해당 복장은 샘당임
            self.inspection['uniform'] = "blue"
            self.inspection['affiliation'] = "해군"