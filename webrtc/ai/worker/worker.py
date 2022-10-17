import cv2


class Worker:
    pass

    def work(self, msg):
        # open
        path = f"{msg}"
        img = cv2.imread(path)
        print(img)
        pass

