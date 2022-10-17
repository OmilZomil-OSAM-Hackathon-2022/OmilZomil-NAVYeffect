import cv2
import time
import os



def video2image(video_path):
    frame_n = 0
    video = cv2.VideoCapture(video_path)
    name = video_path.split('/')[-1].split('.')[0]
    os.makedirs(f'../image/video_frame/{name}', exist_ok=True)
    while True:
        ret, frame = video.read()
        if ret:
            h, w, c = frame.shape
            if w > h:
                pass
                # ro = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
                # frame = ro
                # ro1 = cv2.getRotationMatrix2D((w/2, h/2), -90, 1)
                # tr1 = cv2.warpAffine(frame, ro1, (w, h))
                # tr1 = cv2.resize(tr1, dsize=(
                #     h, w), interpolation=cv2.INTER_AREA)
                # frame = tr1
            frame = cv2.rotate(frame, cv2.ROTATE_180)
            cv2.imwrite(f'../image/video_frame/{name}/{frame_n}.jpg', frame)
            frame_n += 1
        else:
            break



# print('fps', video.get(cv2.CAP_PROP_FPS))
# width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print('original size: %d, %d' % (width, height))

# video.set(cv2.CAP_PROP_FRAME_WIDTH, height)
# video.set(cv2.CAP_PROP_FRAME_HEIGHT, width)
# print('original size: %d, %d' % (width, height))
video_path = '../video/fd_01.mp4'
video2image(video_path)
