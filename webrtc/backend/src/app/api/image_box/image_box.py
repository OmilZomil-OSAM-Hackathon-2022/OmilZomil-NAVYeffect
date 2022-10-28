



from app.api.image_box.base import BaseImageBox



class ImageBox(BaseImageBox):
    def __init__(self, uniform, guardhouse):
        super().__init__(uniform, guardhouse)


    def create_part_list(self):
        pass

    def update(self, result):
        print(self.inspection)
        print(self.parts)
        print(result['component'])
