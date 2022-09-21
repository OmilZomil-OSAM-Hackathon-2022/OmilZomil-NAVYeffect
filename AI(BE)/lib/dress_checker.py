import cv2
import numpy as np
from .utils import *
from .defines import *
from .ocr import OCR


def getNavyServiceUniformClasses(org_img):
    img = org_img.copy()
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower, upper = (0, 114, 212), (190, 255, 255) # 샘당 계급장 filter 
    yellow_mask = cv2.inRange(hsv_img, lower, upper)
    
    morphed_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_CLOSE, (10,2))

    masked_img = cv2.bitwise_and(img, img, mask=morphed_mask)

    contours, _ = cv2.findContours(morphed_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    classes = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        print('area :', area)
        if 10 < area:
            classes += 1
            cv2.drawContours(img, [contour], 0, Color.RED, -1)

    print('classes :', classes)
    plt_imshow(['yellow filter', 'morphed mask', 'masked img', f'img L({classes})'], [yellow_mask, morphed_mask, masked_img, img])
    
    if 1 <= classes <= 4:
        return classes
    else:
        return None

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
    contours, hierarchy = sortContoursByArea(contours)

    for i, (contour, lev) in enumerate(zip(contours, hierarchy)):
        cur_node, next_node, prev_node, first_child, parent = lev
        if i == 0:
            cv2.drawContours(img, [contour], 0, Color.RED, -1)
            shirt_node = cur_node
            continue
        
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        
        if parent == shirt_node and 4 <= len(approx) <= 5:
            area = cv2.contourArea(contour)
            if area > 100:
                M = cv2.moments(contour)
                center_p = getCenterPosition(M)

                # simple way
                # if center_x < (W//2):
                #     cv2.
                
                cv2.drawContours(img, [contour], 0, Color.RED, 2)
                cv2.drawContours(img, [contour], 0, Color.GREEN, -1)
                drawLine(img, center_p, center_p, Color.PURPLE, 50)

    half_line_p1, half_line_p2 = (w//2, 0), (w//2, h)
    cv2.line(img, half_line_p1, half_line_p2, Color.WHITE, 5)
    plt_imshow(['black filter', 'masked img (bitwise and)', 'img'], [black_mask, masked_img, img])

def checkNavyServiceUniform(org_img):
    img = org_img.copy()
    # img = cv2.resize(img, (500,500))
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, w = img.shape[:2]

    lower, upper = (50, 10, 30), Color.WHITE # 샘당 filter 
    blue_mask = cv2.inRange(hsv_img, lower, upper)
    masked_img = cv2.bitwise_and(img, img, mask=blue_mask)

    contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    sorted_contours, sorted_hierarchy = sortContoursByArea(contours, hierarchy)


    ocr_str, ocr_boxes = OCR(img)
    contour_dic = {}
    component_dic = {}
    name_tag_content, level_tag_content = None, None
    for i, (contour, lev) in enumerate(zip(sorted_contours, sorted_hierarchy)):
        cur_node, next_node, prev_node, first_child, parent = lev
        if i == 0:  # 셈브레이
            cv2.drawContours(img, [contour], 0, Color.RED, -1)
            shirt_node = cur_node
            continue

        if parent == shirt_node and 4 <= getVertexCnt(contour) <= 5 and cv2.contourArea(contour) > 300: # 이름표 또는 계급장
            center_p = getContourCenterPosition(contour)
            max_xy, min_xy = np.max(contour, axis=0)[0],np.min(contour, axis=0)[0] 
            
            # simple way
            if center_p[0] < (w//2) and not component_dic.get('name_tag'):
                for ocr_box in ocr_boxes:
                    ocr_center_xy = getRectCenterPosition(ocr_box)
                    if isPointInBox(ocr_center_xy, (min_xy, max_xy)):
                        contour_dic['name_tag'] = contour
                        component_dic['name_tag'] = ocr_str
                        cv2.drawContours(img, [contour], 0, Color.RED, 2)
                        cv2.drawContours(img, [contour], 0, Color.GREEN, -1)
                        drawPoint(img, center_p, Color.PURPLE, 50)
                        break

            elif center_p[0] > (w//2) and not component_dic.get('class_tag'):
                x, y, w, h = cv2.boundingRect(contour)
                roi = org_img[y:y+h, x:x+w]
                classes = getNavyServiceUniformClasses(roi)
                if classes:
                    contour_dic['class_tag'] = contour
                    component_dic['class_tag'] = classes
                    cv2.drawContours(img, [contour], 0, Color.RED, 2)
                    cv2.drawContours(img, [contour], 0, Color.GREEN, -1)
                    drawPoint(img, center_p, Color.PURPLE, 50)
                    break

    half_line_p1, half_line_p2 = (w//2, 0), (w//2, h)
    cv2.line(img, half_line_p1, half_line_p2, Color.WHITE, 5)

    
    cv2.imwrite('./res/res05.jpg', masked_img)
    cv2.imwrite('./res/res06.jpg', img)
    plt_imshow(['blue filter', 'masked img (bitwise and)', 'img'], [blue_mask, masked_img, img])
    return component_dic, contour_dic