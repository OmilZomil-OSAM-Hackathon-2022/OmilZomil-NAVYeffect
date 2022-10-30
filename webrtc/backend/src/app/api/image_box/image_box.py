



from app.api.image_box.base import BaseImageBox



class ImageBox(BaseImageBox):
    def __init__(self, uniform, guardhouse):
        super().__init__(uniform, guardhouse)
        self.update_list = set()


    def update(self, result):

        # 이미지 갱신
        if len(result['component']) > self.image_count:
            self.main_image = result['boxed_img']
            self.update_list.add("main")

        # 이름 인식
        if self.inspection['name'] == "" and result['component'].get("name_tag"):
            cached_name = result['component'].get("name_tag")
            self.inspection['name'] = cached_name.replace('cached ', '', 1) #cached  제거
            self.update_list.add("main")

        # 계급 인식
        if self.inspection['rank'] == "" and result['component'].get("class_tag"):
            self.inspection['rank'] = result['component'].get("class_tag")
            self.update_list.add("main")

        # 파츠 상태 업데아트
        for part_name, status in result['component'].items():
            if status and self.parts[part_name] == False:
                self.parts[part_name] = True # 양호로 갱신
                self.parts_images[part_name] = result['roi'][part_name]
                self.update_list.add(part_name)
