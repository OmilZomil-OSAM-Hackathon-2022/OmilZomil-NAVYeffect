import cv2
import time


def video2image(video):
    i = 0
    while True:
        ret, frame = video.read()
        if ret:
            print(frame.shape, i)
            h, w, c = frame.shape
            if w > h:
                ro = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
                frame = ro
                # ro1 = cv2.getRotationMatrix2D((w/2, h/2), -90, 1)
                # tr1 = cv2.warpAffine(frame, ro1, (w, h))
                # tr1 = cv2.resize(tr1, dsize=(
                #     h, w), interpolation=cv2.INTER_AREA)
                # frame = tr1

            print(frame.shape, i)
            cv2.imwrite(f'../image/video_frame/1/{i}.jpg', frame)
            i += 1
            break
        else:
            break
    print(i)


video = cv2.VideoCapture('../video/1.mp4')
# print('fps', video.get(cv2.CAP_PROP_FPS))
# width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print('original size: %d, %d' % (width, height))

# video.set(cv2.CAP_PROP_FRAME_WIDTH, height)
# video.set(cv2.CAP_PROP_FRAME_HEIGHT, width)
# print('original size: %d, %d' % (width, height))

video2image(video)
