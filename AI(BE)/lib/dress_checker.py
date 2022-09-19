import cv2
import numpy as np
from .utils import *
from .defines import *

def checkMiliteryUniform(img):
    pass

def checkFullDressUniform(org_img):
    img = org_img.copy()
    h, w = img.shape[:2]
    # img = cv2.resize(img, (500,500))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower, upper = (44, 0, 0), (171, 255, 124) # 정복 filter
    black_mask = cv2.inRange(hsv, lower, upper)
    masked_img = cv2.bitwise_and(img, img, mask=black_mask)

    contours, hierarchy = cv2.findContours(black_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = hierarchy[0]
    hierarchy = [np.insert(hier, 0, idx) for idx, hier in enumerate(hierarchy)]
    contours, hierarchy = [list(t) for t in zip(*sorted(zip(contours, hierarchy), key=lambda x : cv2.contourArea(x[0]), reverse=True))]


    for i, (contour, lev) in enumerate(zip(contours, hierarchy)):
        cur_node, next_node, prev_node, first_child, parent = lev
        if i == 0:
            cv2.drawContours(img, [contour], 0, Color.RED, -1)
            shirt_node = cur_node
            print(lev)
            continue
        
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        
        if parent == shirt_node and 4 <= len(approx) <= 5:
            area = cv2.contourArea(contour)
            if area > 100:
                print('lev : ', lev)
                M = cv2.moments(contour)
                center_p = getCenterPosition(M)

                # simple way
                # if center_x < (W//2):
                #     cv2.
                # elif center
                
                cv2.drawContours(img, [contour], 0, Color.RED, 2)
                cv2.drawContours(img, [contour], 0, Color.GREEN, -1)
                cv2.line(img, center_p, center_p, Color.PURPLE, 50)

    half_line_p1, half_line_p2 = (w//2, 0), (w//2, h)
    cv2.line(img, half_line_p1, half_line_p2, Color.WHITE, 5)
    plt_imshow(['black filter', 'masked img (bitwise and)', 'img'], [black_mask, masked_img, img])

def checkNavyServiceUniform(org_img):
    img = org_img.copy()
    # img = cv2.resize(img, (500,500))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower, upper = (50, 10, 30), Color.WHITE, # 샘당 filter
    blue_mask = cv2.inRange(hsv, lower, upper)
    masked_img = cv2.bitwise_and(img, img, mask=blue_mask)

    contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    hierarchy = hierarchy[0]
    hierarchy = [np.insert(hier, 0, idx) for idx, hier in enumerate(hierarchy)]
    contours, hierarchy = [list(t) for t in zip(*sorted(zip(contours, hierarchy), key=lambda x : cv2.contourArea(x[0]), reverse=True))]


    for i, (contour, lev) in enumerate(zip(contours, hierarchy)):
        cur_node, next_node, prev_node, first_child, parent  = lev
        if i == 0:
            cv2.drawContours(img, [contour], 0, Color.RED, -1)
            shirt_node = cur_node
            print(lev)
            continue
        
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        
        if parent == shirt_node and 4 <= len(approx) <= 5:
            area = cv2.contourArea(contour)
            if area > 100:
                print('lev : ', lev)
                M = cv2.moments(contour)
                center_x = int(M["m10"] / M["m00"])
                center_y = int(M["m01"] / M["m00"])

                # simple way
                # if center_x < (W//2):
                #     cv2.
                # elif center
                
                cv2.drawContours(img, [contour], 0, Color.RED, 2)
                cv2.drawContours(img, [contour], 0, Color.GREEN, -1)
                cv2.line(img, (center_x, center_y), (center_x, center_y), Color.PURPLE, 50)

    h, w = img.shape[:2]
    half_line_p1, half_line_p2 = (w//2, 0), (w//2, h)
    cv2.line(img, half_line_p1, half_line_p2, Color.WHITE, 5)
    plt_imshow(['blue filter', 'masked img (bitwise and)', 'img'], [blue_mask, masked_img, img])