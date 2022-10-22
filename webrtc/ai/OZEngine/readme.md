
## 사용법 (Usage)


### 파라미터

먼저 OZEngine 모듈을 import하고 객체를 생성해줍니다
``` python
import OZEngine

detector = OZEngine()
```

OZEngine class에는 여러 함수들이 있는데 우리는 분석하기 위해 detect 함수 1개만 있으면 충분합니다! 
check_person, train_mode 2개의 파라미터를 받고있습니다. detect 함수 정의는 다음과 같이 되어있습니다.

``` python
def detect(check_person=True, train_mode=False):
```

| 파라미터 | 기본값 | 설명 |
| ------ | ------ | ------ |
| check_person | False | 사람인식모델의 유무를 결정하는 파라미터입니다. |
| train_mode | False | 분류모델의 사용유무를 결정하는 파라미터입니다. |

Note 1: `check_person=True` 옵션을 주게 되면 detect함수 내부에 있는 사람인식모델이 동작하게 됩니다. 이 옵션이 필요할까요? [참고] 결론적으로 저희 Omil-Zomil 서비스 내부에서 실시간 분석을 위해 별도로 만든 옵션입니다.

Note 2: `check_person` 옵션은 현재 Omil-Zomil서비스에서 제공하고 있는 모델(, )에 사용자데이터를 추가하여 학습을 해야 하는 상황이 존재할 때 사용합니다. `check_person=True`로 하게되면 실제 모델 내부에서는 각 파츠들을 분류하는 분류모델을 사용하지 않습니다. 대신 파츠로 추정되는 이미지들을 모두 저장시킵니다. 학습할 때는 이렇게 저장된 이미지들을 사람이 수동으로 분류를 하고 학습모델을 train시키면 됩니다. 

더 많은 정보는, [tutorial](https://www.jaided.ai/easyocr/tutorial)과 [API Documentation](https://www.jaided.ai/easyocr/documentation)를 읽어보세요

### 실행

#### Run Code
OZEngine 객체 detector의 멤버함수 detect를 호출합니다.
호출할 때에 이미지의 numpy 배열도 같이 넘겨줍니다.
``` python
detector.detect(img)
```

#### Result
``` bash
{
	'component': {
		'rank_tag':'병장',
		'name_tag':'조준영',
		'neckerchief': True,
		'muffler': True
	},
	'boxed_img': {
		[결과 이미지 numpy 배열]
	},
	'roi': {
		'rank_tag': [계급장 이미지 numpy 배열],
		'name_tag':[계급장 이미지 numpy 배열],
		'neckerchief': [네카치프 이미지 numpy 배열],
		'muffler': [마후라 이미지 numpy 배열]
	}
}
```

결과값은 위와 같이 나옵니다. `component`에는 현재 병사가 착용하고 있는 파츠만 return 됩니다. 각 파츠들은 정복, 전투복, 근무복에 따라 다르게 표시됩니다. 만약 파츠를 착용하고 있지 않으면 빈 dictionary가 반환됩니다. 또는 사람이 인식되지 않거나 군복으로 판단되지 않으면 None값이 반환됩니다.

`boxed_img`는 원본 이미지 (detect함수에 들어간 원본 이미지) 위에 인식된 얼굴의 위치와 파츠들의 위치가 bounding box형태로 표시가 된 이미지 입니다. 이 이미지 역시 numpy 배열로 return이 됩니다. 만약 사람이 인식되지 않으면 원본 이미지와 같은 이미지가 반환됩니다. (연속된 이미지로 볼 때 끊기지 않게 보기기 위함입니다) 

 `roi`는 인식된 파츠 이미지들에 ROI(Region Of Image)가 적용된 이미지입니다. 한마디로 인식된 부분만 잘린 이미지들입니다. 만약 파츠를 착용하고 있지 않으면 빈 dictionary가 반환됩니다. 또는 사람이 인식되지 않거나 군복으로 판단되지 않으면 None값이 반환됩니다.

#### Code Example

아래는 이미지 입력부터 결과값 출력까지 전체적인 코드 예시입니다.

``` python
import cv2
import OZEngine

detector = OZEngine()  # 객체 선언
img = cv2.imread('/image/example.jpg')  # 분석할 이미지 대상
result = detector.detect(img)  # detect함수 실행

print(result['component'])  # 파츠여부 값만 출력
'''
예상 출력 값
{
  'rank_tag':'병장',
  'name_tag':'조준영',
  'neckerchief': True,
  'muffler': True
}
'''
```


## 사용자 정의 모델 학습

For recognition model, [Read here](https://github.com/JaidedAI/EasyOCR/blob/master/custom_model.md).

For detection model (CRAFT), [Read here](https://github.com/JaidedAI/EasyOCR/blob/master/trainer/craft/README.md).

## 개발자 RoadMap

### 1. check_person 옵션 활용

 저희 Omil-Zomil에서는 위병소의 데이터를 실시간으로 분석합니다. 실시간으로 분석할 때 갑작스럽게 데이터가 몰려 서버에 부하가 심하게 가해지는 현상을 방지하기 위해 캐시(cache)기술이 적용된 DB를 사용합니다. DB에 저장하고 순차적으로 먼저 들어온 이미지데이터를 처리하기 때문에 처리하는 순간에는 사람인식이 보장되어있는 상태입니다.
 
``` python
import cv2
import OZEngine
from OZEngine.person_detectors import PersonDetector

detector = OZEngine()
person_detector = PersonDetector() # 사람인식모델 선언

img = cv2.imread('/image/example.jpg')  # 분석할 이미지 대상
box = person_detector(img) 

result = detector.detect(img, check_person=True)  # check_person값을 True로
```

### 2. train_mode 옵션 활용


``` python
import cv2
import OZEngine

detector = OZEngine()

img = cv2.imread('/image/example.jpg')  # 분석할 이미지 대상
result = detector.detect(img, train_mode=True)  # train_mode값을 True로
```

### 3. 사용자 동영상 분석

``` python
import os
import tensorflow as tf
from tqdm import tqdm
from OZEngine.lib.utils import *
from OZEngine import OmilZomil

save_path = os.path.join(os.getcwd(), 'image/res/final_fd')
os.makedirs(save_path, exist_ok=True)
model = OmilZomil()

frame_path = 'image/video_frame/fd_1'
frames = os.listdir(frame_path)
frame_n = len(frames)
print('frame n ', frame_n)

for i in tqdm(range(0, frame_n), desc='detecting'):
	read_path = os.path.join(frame_path, f'{i}.jpg')

	img = cv2.imread(read_path)
	result = model.detect(img)
	if result.get('boxed_img') is  not  None:
		model.saveImg({'result':result['boxed_img']}, save_path=save_path)
		model.saveImg({'hed_result':result['hed_boxed_img']}, save_path=save_path)
	if result.get('roi'):
		model.saveImg(result['roi'], save_path=save_path)
```

## 참고 및 참조

This project is based on research and code from several papers and open-source repositories.

저희 분석모델의 전반적인 Deep Learning 알고리즘의 기반은 [Tensorflow](https://pytorch.org):heart: 입니다. 

두발상태인식모델은 HairSegNet을 사용했고 [github 저장소](https://github.com/clovaai/CRAFT-pytorch)에서 확인하실 수 있습니다. [관련 논문](https://arxiv.org/pdf/1712.07168.pdf)도 있으니 참고하여 보실 수 있습니다. (@[thangtran480](https://github.com/thangtran480)님께 감사드립니다 :thanks:) 


## GPU가속 지원

저희 오밀조밀 프로젝트에서는 Tensorflow 2.10을 사용하고 있으며 GPU지원이 가능합니다. 
To request a new language, we need you to send a PR with the 2 following files:

1. In folder [easyocr/character](https://github.com/JaidedAI/EasyOCR/tree/master/easyocr/character),
we need 'yourlanguagecode_char.txt' that contains list of all characters. Please see format examples from other files in that folder.
2. In folder [easyocr/dict](https://github.com/JaidedAI/EasyOCR/tree/master/easyocr/dict),
we need 'yourlanguagecode.txt' that contains list of words in your language.
On average, we have ~30000 words per language with more than 50000 words for more popular ones.
More is better in this file.

If your language has unique elements (such as 1. Arabic: characters change form when attached to each other + write from right to left 2. Thai: Some characters need to be above the line and some below), please educate us to the best of your ability and/or give useful links. It is important to take care of the detail to achieve a system that really works.

Lastly, please understand that our priority will have to go to popular languages or sets of languages that share large portions of their characters with each other (also tell us if this is the case for your language). It takes us at least a week to develop a new model, so you may have to wait a while for the new model to be released.

See [List of languages in development](https://github.com/JaidedAI/EasyOCR/issues/91)
