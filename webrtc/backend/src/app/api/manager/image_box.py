
UNIFORM_PARTS = {
    2 : [  # 샘당
        "hair", "nametag", "leveltag"
        
        ],
    3 : [ # 정복
        "hair", "nametag", "leveltag", "muffler", "neck" 
        ],
    4 : [ # 군복
        "hair", "nametag", "leveltag", "flag"
    ],
}




class ImageBox:
    """
    이미지를 ai에게 전달
    ai 처리 결과를 보존
    ㄴ 첫 이미지인 경우 데이터 생성
    ㄴ 변경사항이 있는 경우 is_update
    ㄴ 없는 경우 무시
    ai 분기를 지정
    best 이미지 선정 등을 관리
    """
    pass

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
        # 메인 이미지 관리
        self.image_path = None
        self.old_image_count=0
        # 데이터 갱신 유무
        self.is_update = False
        self.parts_update = []

    
    def get_inspection(self):
        return self.inspection
    
    def get_parts(self):
        return self.parts

    def image_process(self, image, path):
        # 복장 양호 불량 인식
        result = self.ai.detect(img=image)
        result_images = {}

        # 첫 이미지인 경우
        if not self.image_path:
            self.image_path = path        
            self.inspection['uniform'] = self.ai.get_uniform()
            self.inspection['affiliation'] = self.ai.get_affiliation()
            self.parts = {key: False for key in UNIFORM_PARTS[self.inspection['uniform']]} # 유니폼에 따라 파츠 리스트 생성
            self.is_update = True
        
        # 각 파츠별 데이터 갱신
        for part in UNIFORM_PARTS[self.inspection['uniform']]:
            # 각 파츠가 갱신이 필요한 경우 
            if result[part] and not self.parts[part]:
                self.parts[part] = True # 양호로 갱신
                result_images[part] = f"가짜 이미지 - {part} - {path}"
                self.parts_update.append(part) # 업데이트 목록에 추가


        # 각 파츠별 추가 ai 인식
        # 이름 태그가 있으면
        if result["nametag"] and self.inspection['name'] == "":
            # 이름 인식
            self.inspection['name'] = self.ai.random_name()
            self.is_update = True        
        # 계급장이 있으면
        if result["leveltag"] and self.inspection['rank'] == 1:
            # 계급 인식
            self.inspection['rank'] = self.ai.random_rank()
            self.is_update = True        
        
        return result_images