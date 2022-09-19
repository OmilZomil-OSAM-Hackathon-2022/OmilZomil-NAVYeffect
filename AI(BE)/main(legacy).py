import cv2
import numpy as np

img_path = '/Users/joon0zo/Project/Correcter/image/mil_04.jpg'
org = cv2.imread(img_path, cv2.IMREAD_COLOR)
# print(org)
# org = cv2.resize(org, dsize=(0,0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)  # ================  1 gray scale로 변환

kernel = np.ones((3, 6), np.uint8)
kernel2 = np.ones((5, 30), np.uint8)
roi_list = []

morph = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)  # 2 ================ 경계선 찾기
# morph = gray

thr = cv2.adaptiveThreshold(morph, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY_INV, 3, 30)  # 3 ================ 임계처리

morph2 = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, kernel2)  # 4 ================ 뭉게기
contours, _ = cv2.findContours(morph2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 5 ================ 특징점 찾기

org2 = cv2.copyMakeBorder(org, 0, 0, 0, 0, cv2.BORDER_REPLICATE)
for cnt in contours:
    try:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 5 and 30 < h < 100:
            # print(w, h)
            roi = org2[y:y + h, x:x + w]
            # cv2.imshow('roi', roi)
            roi_list.append(roi)
            cv2.rectangle(org, (x, y), (x+w, y+h), (255, 0, 0), 2)

    except Exception as e:
        pass

cv2.imshow('org', org)
cv2.imshow('morph', morph)
cv2.imshow('thr', thr)
cv2.imshow('morph2', morph2)

cv2.waitKey(0)
cv2.destroyAllWindows()