## Tutorial

이 문서는 OmilZomil객체를 처음 활용하시는 분들을 위한 문서입니다.

<h2 id="image">동영상 입력</h2>
<br>

다음 예제는 특정 이미지를 읽고 AI영상처리 로직을 수행하는 코드입니다. 영상처리 AI의 결과물인 박스가 존재하는 이미지와 파츠여부 값이 출력됩니다.
```python
# demo.py

import cv2, os
from demo_lib.utils import setImportPath, plt_imshow
setImportPath()
from OZEngine import OmilZomil

os.environ['AI_PATH'] = '/config/workspace/WEB_CLOUD_OmilZomil_NAVYeffect/ai' # ai폴더가 있는 위치

detector = OmilZomil()  # 객체 선언
img = cv2.imread('image/test.jpg')  # 분석할 이미지 대상
result = detector.detect(img)  # detect함수 실행

plt_imshow('res', result['boxed_img'])  # 이미지 출력

print(result['component'])  # 파츠여부 값만 출력
```

<h2 id="video">동영상 입력</h2>
<br>
사진이 아닌 동영상도 분석이 가능합니다. 동영상을 분석하기 위해 먼저 동영상을 프레임별로 이미지로 저장하는 코드가 필요합니다.

<br>

<h3 id="video">1. video2image</h3>

 아래는 동영상을 이미지로 저장하는 코드입니다. preprocess는 ai/demo 하위에 존재하는 폴더입니다. 그 중 video2image 함수는 비디오 경로를 string형식으로 입력하면 해당 동영상의 이름을 고려하여 ai/demom/image폴더에 이미지를 저장합니다.

```python
from preprocess import video2image

video_path = '../video/fd_01.mp4' # 동영상 위치
video2image(video_path)
```

해당 코드의 실행 결과로 다음과 같이 이미지파일이 만들어집니다.

```
/demo/image/res/fd_01/
├─ 1.jpg
├─ 2.jpg
├─ 3.jpg
│
│  ...
│  
├─ 981.jpg
```

<br>

<h3 id="video">2. frame 별 분석</h3>
 다음은 만들어진 프레임들로 OmilZomil 객체에 입력시켜 결과값을 출력하는 단계입니다.

 ```python
from demo_lib.utils import setImportPath
setImportPath()
import os
import traceback
import time
import tensorflow as tf
from tqdm import tqdm

from OZEngine.lib.utils import *
from OZEngine import OmilZomil

save_path = os.path.join(os.getcwd(), 'image/res/fd_01')  # 이미지 저장할 위치
os.makedirs(save_path, exist_ok=True)
model = OmilZomil()

frame_path = 'image/video_frame/fd_01' # 프레임 이미지가 존재하는 디렉토리 위치
frames = os.listdir(frame_path)
frame_n = len(frames)
print('frame n ', frame_n)  # 전체 프레임 개수
for i in tqdm(range(1, frame_n), desc='detecting'):
    read_path = os.path.join(frame_path, f'{i}.jpg')
    img = cv2.imread(read_path)
    
    result = model.detect(img)
    if result['step'] >= 1:
        model.saveImg({'result':result['boxed_img']}, save_path=save_path)
    if result['step'] >= 2:
        model.saveImg({'shirts':result['shirt_img']}, save_path=save_path)
    
    if result['step'] >= 3:
        if result.get('roi'):
            model.saveImg(result['roi'], save_path=save_path)
```

위의 코드의 경우 `image/video_frame/fd_01/*.jpg` 이미지들을 AI 영상처리 후 `image/res/fd_01/*.jpg`로 저장을 합니다. 단순 jpg가 아닌 태그별로 폴더가 나뉘고, 최종 결과값 이미지가 각기 다른 디렉토리로 저장이 됩니다. 저장이 되는 위치는 다음과 같습니다.

```
/demo/image/res/fd_01/class_tag
├─ 1.jpg
├─ 2.jpg
├─ 3.jpg
│
│  ...
│  
├─ 1312.jpg
```

```
/demo/image/res/fd_01/boxed_img
├─ 1.jpg
├─ 2.jpg
├─ 3.jpg
│
│  ...
│  
├─ 1592.jpg
```

<h3 id="video">3. 결과값을 GIF로 변환</h3>

마지막으로 폴더에 저장되어 있는 결과 이미지들을 FFMPEG로 gif파일로 변환할 수 있습니다. FFMPEG 명령어는 다음과 같습니다.

```bash
ffmpeg -y -threads 1 -i "" -c:v libx264 -preset fast -c:a aac  -max_muxing_queue_size 1024 ""
```
