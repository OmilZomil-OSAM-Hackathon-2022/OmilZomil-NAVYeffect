import cv2
import numpy as np

class Morph():
    def __init__(self):
        alpha1 = -0.5 # 명암 조정값
        alpha2 = 1.0 # 명암 조정값
    
    def detect_edge(self, img, isEdge=False):
        if isEdge == False:
            org = img # cv2.imread(self.img_path, cv2.IMREAD_COLOR)
            # org = np.clip((1+alpha2) * org - 128 * alpha2, 0, 255).astype(np.uint8)
            
            org = cv2.normalize(org, None, 0, 255, cv2.NORM_MINMAX)

            # org = cv2.resize(org, dsize=(0,0), fx=0.5, fy=0.5)
            gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)  # ================  1 gray scale로 변환
            edge1 = cv2.Canny(gray,50, 100)
        else:
            org = np.zeros([img.shape[0], img.shape[1], 3])
            edge1 = img
        kernel = np.ones((2, 2), np.uint8)
        edge_morph = cv2.morphologyEx(edge1, cv2.MORPH_CLOSE, kernel)
        contours, hierarchy = cv2.findContours(edge_morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for i in range(len(contours)):
            contour = contours[i]
            # print(contour)
            # moments = cv2.moments(contour)
            area = cv2.contourArea(contour)
            if 100000 > area > 1000: # 5000 > area > 0:
                epsilon = 0.02 * cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, epsilon, True)

                #cv2.drawContours(org,[approx],0,(0,255,255),3)
                cv2.drawContours(org, [contour], 0, (0, 0, 255), 2)
                cv2.drawContours(org, [contour], 0, (255, 0, 0), -1)
            
        # lines = cv2.HoughLinesP(edge_morph, 1, np.pi/180, 2, None, 20, 2)
        # for line in lines:
        #     # 검출된 선 그리기 ---③
        #     x1, y1, x2, y2 = line[0]
        #     if abs(y2-y1) > 10 and abs(x2-x1) < 50:
        #         cv2.line(org, (x1,y1), (x2, y2), (255,255,0), 1)
        return edge_morph, org #org, edge_morph, edge1

        # cv2.waitKey(0)
        # cv2.destroyAllWindows()