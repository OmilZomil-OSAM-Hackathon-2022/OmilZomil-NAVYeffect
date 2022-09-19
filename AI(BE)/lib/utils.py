from matplotlib import pyplot as plt
import cv2
import numpy as np
import imutils

BLACK = (0,0,0)
RED = (0,0,255)
GREEN = (0,255,0)
BLUE = (255,0,0)
WHITE = (255,255,255)

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