import time
import datetime
import cv2
import numpy as np

MODEL_PATH = './detectors/hed/weights/hed_pretrained_bsds.caffemodel'
PROTO_TXT_PATH = './detectors/hed/deploy.prototxt'

class CropLayer(object):
    def __init__(self, params, blobs):
        self.xstart = 0
        self.xend = 0
        self.ystart = 0
        self.yend = 0

    # Our layer receives two inputs. We need to crop the first input blob
    # to match a shape of the second one (keeping batch size and number of channels)
    def getMemoryShapes(self, inputs):
        inputShape, targetShape = inputs[0], inputs[1]
        batchSize, numChannels = inputShape[0], inputShape[1]
        height, width = targetShape[2], targetShape[3]

        self.ystart = int((inputShape[2] - targetShape[2]) / 2)
        self.xstart = int((inputShape[3] - targetShape[3]) / 2)
        self.yend = self.ystart + height
        self.xend = self.xstart + width

        return [[batchSize, numChannels, height, width]]

    def forward(self, inputs):
        return [inputs[0][:,:,self.ystart:self.yend,self.xstart:self.xend]]

class HED():
    def __init__(self):
        tstamp = time.time()
        print('[RCF] loading...')
        self.net = cv2.dnn.readNetFromCaffe(PROTO_TXT_PATH, MODEL_PATH)
        cv2.dnn_registerLayer('Crop', CropLayer)
        print('[RCF] finished loading (%.4f sec)' % (time.time() - tstamp))

    def detect_edge(self, img, width=256, height=256):
        org_width = img.shape[1]
        org_height = img.shape[0]

        start_time = datetime.datetime.now()
        print('시작시간 : {}'.format(start_time))
        img = cv2.resize(img, (width, height))
        inp = cv2.dnn.blobFromImage(img, scalefactor=1.0, size=(width, height),
                                    mean=(104.00698793, 116.66876762, 122.67891434),
                                    swapRB=False, crop=False)
        self.net.setInput(inp)
        out = self.net.forward()

        out = out[0, 0]
        out = cv2.resize(out, (org_width, org_height))

        out = 255 * out
        out = out.astype(np.uint8)

        end_time = datetime.datetime.now()
        print('종료시간 : {}'.format(end_time))

        time_delta = end_time - start_time
        print('수행시간 : {} 초'.format(time_delta.seconds) + "\n")

        return out