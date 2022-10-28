



from app.api.image_box.base import BaseImageBox



class ImageBox(BaseImageBox):
    def __init__(self, uniform, guardhouse):
        super().__init__(uniform, guardhouse)


    def update(self, result):

        # 이미지 갱신
        if len(result['component']) > self.image_count:
            self.main_image = result['boxed_img']

        # 이름 인식
        if self.inspection['name'] == "":
            cached_name = result['component'].get("name_tag")
            self.inspection['name'] = cached_name.replace('cached ', '', 1) #cached  제거

        # 계급 인식
        if self.inspection['rank'] == "":
            self.inspection['rank'] = result['component'].get("rank_tag")

        # 파츠 상태 업데아트
        for part_name, status in result['component'].items():
            if status and self.parts[part_name] == False:
                self.parts[part_name] = True # 양호로 갱신
