import cv2
import numpy as np
from lib.utils import *


class PersonDetector():
    def __init__(self, only_person=True):
        self.net = cv2.dnn.readNet(
            "OZEngine/person_detectors/yolov2-tiny.weights", "OZEngine/person_detectors/yolov2-tiny.cfg")
        self.classes = []
        if only_person:
            self.classes = ['person']
        else:
            with open("OZEngine/person_detectors/coco.names", "r") as f:
                self.classes = [line.strip() for line in f.readlines()]
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i-1]
                              for i in self.net.getUnconnectedOutLayers()]
        self.colors = np.random.uniform(0, 255, size=(len(self.classes), 3))

    def detect(self, org_img):
        img = org_img
        height, width, channels = img.shape
        blob = cv2.dnn.blobFromImage(
            img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)

        class_ids = []
        confidences = []
        box = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # 좌표
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    box = (x, y, w, h)
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN

        print(class_ids)
        print(confidences)
        print(boxes)
        print(indexes)

        roi = None
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(self.classes[class_ids[i]])
                color = self.colors[i]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                roi = org_img[y:y+h, x:x+w]
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

        plt_imshow("Image", img)
        return roi, img
