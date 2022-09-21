from matplotlib import pyplot as plt
import cv2
import numpy as np
import imutils
from .utils import *

MIN2SEC = 60

def prepare_image_PIL(im):
    im = im[:,:,::-1] - np.zeros_like(im) # rgb to bgr
    # im -= np.array((104.00698793,116.66876762,122.67891434))
    im = np.transpose(im, (2, 0, 1)) # (H x W x C) to (C x H x W)
    return im

def prepare_image_cv2(im):
    # im -= np.array((104.00698793,116.66876762,122.67891434))
    im = cv2.resize(im, dsize=(1024, 1024), interpolation=cv2.INTER_LINEAR)
    im = np.transpose(im, (2, 0, 1)) # (H x W x C) to (C x H x W)
    return im

def plt_imshow(title='image', img=None, figsize=(8, 5)):
    plt.figure(figsize=figsize)

    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []

            for i in range(len(img)):
                titles.append(title)

        for i in range(len(img)):
            if len(img[i].shape) <= 2:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)

            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])

        plt.show()
    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.show()


def find_contours(img, thresh=-1):
    # contours를 찾아 크기순으로 정렬
    if thresh > -1:
        ret, edge_img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    else:
        edge_img = img.copy()

    cnts = cv2.findContours(edge_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    receiptCnt = None

    # 정렬된 contours를 반복문으로 수행하며 4개의 꼭지점을 갖는 도형을 검출
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # contours가 크기순으로 정렬되어 있기때문에 제일 첫번째 사각형을 영수증 영역으로 판단하고 break
        if len(approx) == 4:
            receiptCnt = approx
            break

    # 만약 추출한 윤곽이 없을 경우 오류
    if receiptCnt is None:
        raise Exception(("Could not find receipt outline."))

    return receiptCnt


def draw_contours(img, contour):
    output = img.copy()
    cv2.drawContours(output, [contour], -1, (0, 255, 255), 10)
    plt_imshow("Draw Outline", output, figsize=(16, 10))

def drawPoint(org_img, position, color, thick):
    cv2.line(org_img, position, position, color, thick)

def getContourCenterPosition(contour):
    moments = cv2.moments(contour)
    return (int(moments["m10"] / moments["m00"]), int(moments["m01"] / moments["m00"]))

def sortContoursByArea(contours, hierarchy=[]):
    if len(hierarchy):
        hierarchy = hierarchy[0]
        hierarchy = [np.insert(hier, 0, idx) for idx, hier in enumerate(hierarchy)]
        sorted_contours, sorted_hierarchy = [list(t) for t in zip(*sorted(zip(contours, hierarchy), key=lambda x : cv2.contourArea(x[0]), reverse=True))]
        return sorted_contours, sorted_hierarchy
    else:
        sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
        return sorted_contours

def getVertexCnt(contour):
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
    return len(approx)

def getRectCenterPosition(rect):
    (p1, p2, p3, p4) = rect
    center_x, center_y = (p1[0]+p2[0]) / 2, (p1[1]+p3[1]) / 2
    return center_x, center_y

def isPointInBox(center_xy, box_min_max_xy):
    center_x, center_y = center_xy
    box_min_xy, box_max_xy = box_min_max_xy
    min_x, min_y = box_min_xy
    max_x, max_y = box_max_xy
    return min_x < center_x < max_x and min_y < center_y < max_y