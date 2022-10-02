import time
import torch
from .models import resnet101
import cv2
import numpy as np
import datetime

PATH_WEIGHT = './detectors/rcf/weights/only-final-lr-0.01-iter-130000.pth'

class RCF():

    def __init__(self, device='cuda'):

        tstamp = time.time()
        self.device = device

        device = torch.device(device)
        self.net = resnet101(pretrained=False)
        print('[RCF] loading with', self.device)
        self.net.load_state_dict(torch.load(PATH_WEIGHT, map_location=device))
        self.net.eval()
        print('[RCF] finished loading (%.4f sec)' % (time.time() - tstamp))

    def detect_edge(self, img):
        start_time = datetime.datetime.now()
        print('시작시간 : {}'.format(start_time))

        org_img = np.array(img, dtype=np.float32)
        h, w, _ = org_img.shape

        pre_img = self.prepare_image_cv2(org_img)
        pre_img = torch.from_numpy(pre_img).unsqueeze(0)

        outs = self.net(pre_img, (h, w))
        result = outs[-1].squeeze().detach().cpu().numpy()

        result = (result * 255).astype(np.uint8)

        end_time = datetime.datetime.now()
        print('종료시간 : {}'.format(end_time))

        time_delta = end_time - start_time
        print('수행시간 : {} 초'.format(time_delta.seconds) + "\n")

        return result

    def prepare_image_cv2(self, im):
        # im -= np.array((104.00698793,116.66876762,122.67891434))
        im = cv2.resize(im, dsize=(1024, 1024), interpolation=cv2.INTER_LINEAR)
        im = np.transpose(im, (2, 0, 1))  # (H x W x C) to (C x H x W)

        return im
