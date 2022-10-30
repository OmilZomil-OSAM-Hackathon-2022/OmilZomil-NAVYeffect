import cv2

def histNorm(org_img):
    hsv = cv2.cvtColor(org_img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    equalizedV = cv2.equalizeHist(v)
    hsv2 = cv2.merge([h,s,equalizedV])
    hsv_dst = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)


    yCrCb = cv2.cvtColor(org_img, cv2.COLOR_BGR2YCrCb)
    y, Cr, Cb = cv2.split(yCrCb)
    equalizedY = cv2.equalizeHist(y)
    yCrCb2 = cv2.merge([equalizedY, Cr, Cb])
    yCrCb_dst = cv2.cvtColor(yCrCb2, cv2.COLOR_YCrCb2BGR)

    return (hsv_dst, yCrCb_dst)

def onChange(pos):
    pass

img = cv2.imread("0.jpg", cv2.IMREAD_COLOR)
hsv_dst, yCrCb_dst = histNorm(img)
img = cv2.resize(yCrCb_dst, (500, 500))
# _, img = histNorm(img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow("Trackbar Windows")
cv2.namedWindow("Show Windows")

cv2.createTrackbar("minB", "Trackbar Windows", 0, 255, lambda x : x)
cv2.createTrackbar("minG", "Trackbar Windows", 0, 255, lambda x : x)
cv2.createTrackbar("minR", "Trackbar Windows", 0, 255, lambda x : x)

cv2.createTrackbar("maxB", "Trackbar Windows", 0, 255, lambda x : x)
cv2.createTrackbar("maxG", "Trackbar Windows", 0, 255, lambda x : x)
cv2.createTrackbar("maxR", "Trackbar Windows", 0, 255, lambda x : x)

cv2.setTrackbarPos("minB", "Trackbar Windows", 52)
cv2.setTrackbarPos("minG", "Trackbar Windows", 36)
cv2.setTrackbarPos("minR", "Trackbar Windows", 37)

cv2.setTrackbarPos("maxB", "Trackbar Windows", 255)
cv2.setTrackbarPos("maxG", "Trackbar Windows", 255)
cv2.setTrackbarPos("maxR", "Trackbar Windows", 255)

while cv2.waitKey(1) != ord('q'):

    min_b = cv2.getTrackbarPos("minB", "Trackbar Windows")
    min_g = cv2.getTrackbarPos("minG", "Trackbar Windows")
    min_r = cv2.getTrackbarPos("minR", "Trackbar Windows")

    max_b = cv2.getTrackbarPos("maxB", "Trackbar Windows")
    max_g = cv2.getTrackbarPos("maxG", "Trackbar Windows")
    max_r = cv2.getTrackbarPos("maxR", "Trackbar Windows")
    
    lower = (min_b, min_g, min_r)
    upper = (max_b, max_g, max_r)

    img_mask = cv2.inRange(img_hsv, lower, upper)
    img_result = cv2.bitwise_and(img, img, mask=img_mask)

    print(lower, upper)
    w, h = img.shape[:2]
    point = (w//2, h - 10)
    img_result = cv2.line(img_result, point, point, (0, 255, 0), 3)
    cv2.imshow("Show Windows", img_mask)

cv2.destroyAllWindows()
    
