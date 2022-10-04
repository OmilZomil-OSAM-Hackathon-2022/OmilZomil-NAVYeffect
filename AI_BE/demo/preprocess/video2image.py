import cv2
import time


def video2image(video, fps):
    prev_time = 0
    frame_cnt = 0
    while True:
        ret, frame = video.read()
        current_time = time.time() - prev_time
        if (ret is True) and (current_time > 1. / fps):
            prev_time = time.time()
            cv2.imwrite(f'../image/video_result/1/{frame_cnt}.jpg', frame)
        else:
            break

FPS = 1
video = cv2.VideoCapture('../video/1.mp4')
video2image(video, FPS)