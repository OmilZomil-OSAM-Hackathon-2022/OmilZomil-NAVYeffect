# 사용자 모델 학습 방법


## 1. 모델 학습
Omil-Zomil은 사용자가 데이터를 쉽게 학습하고 테스트할 수 있도록 설계하였습니다.

분류 모델은 총 2가지가 있는데 파츠 분류 모델과 복장 분류 모델이 있습니다. 

먼저 폴더 구조는 아래와 같이 만듭니다. (꼭 아래와 같은 구조로 만들어야 동작합니다)
```
parts_classifier/
├─ PartsClassifier.py
├─ train.py
├─ CombatUniform/
│  ├─ dataset/train_set
│  │  ├─ flag_tag/
│  │  ├─ name_tag/
│  ├─ model/
├─ FullDressUniform/
```

저희는 전투복의 파츠를 분류하는 모델을 학습한다고 가정해봅시다. 
그리고 간단하게 태극기, 이름표만 인식되는 모델을 학습한다고 가정하겠습니다. 그럼 `parts_classifier/CombatUniform/dataset/train_set/flag_tag`에 태극기 이미지 파일을 붙여넣습니다. 그리고 이름표 이미지는 `parts_classifier/CombatUniform/dataset/train_set/name_tag`에 넣습니다. 
그 결과 아래와 같은 구조가 될 것입니다.
```
parts_classifier/
├─ CombatUniform/
│  ├─ dataset/train_set
│  │  ├─ flag_tag/
│  │  │  ├─ 1.jpg
│  │  ├─ name_tag/
│  │  │  ├─ 1.jpg
│  ├─ model/
├─ FullDressUniform/
```

네, 이제 학습할 준비를 마쳤습니다! 다음은 `train.py`파일을 작성하여 실제로 학습을 진행하는 단계입니다. `train.py`파일을 다음과 같이 작성합니다.

```python
# train.py
from OZEngine.FeatureExtractor import FeatureExtractor

fe = FeatureExtractor('./CombatUniform')
fe.train()
```

이제 파일을 실행시키면 classes, features.npy, img_paths 이 3개의 파일이 생성됩니다. 
classes는 분류이름이 저장되어있는 파일입니다. features.npy는 VGG-Net을 거쳐 나온 feature vector numpy 배열로 저장되어 있는 파일입니다.

```
parts_classifier/
├─ train.py
├─ PartsClassefier.py
├─ CombatUniform/
│  ├─ dataset/train_set
│  │  ├─ flag_tag/
│  │  │  ├─ 1.jpg
│  │  ├─ name_tag/
│  │  │  ├─ 1.jpg
│  ├─ model/
│  │  ├─ classes
│  │  ├─ feature.npy
│  │  ├─ img_paths
├─ FullDressUniform/
```

## 2. 모델 평가

학습이 끝난 후 모델의 정확도가 어느 정도인지 확인할 수 있습니다. 모델을 학습했을 때 사용했던 이미지 데이터 이외의 이미지를 준비해야 합니다. 준비가 되면 dataset폴더 하위에 evaluate_set 만들어서 학습할 때와 같은 디렉토리 구조를 만듭니다.

```
parts_classifier/
├─ validate.py
├─ PartsClassefier.py
├─ CombatUniform/
│  ├─ dataset/train_set
│  │  ├─ flag_tag/
│  │  │  ├─ 1.jpg
│  │  ├─ name_tag/
│  │  │  ├─ 1.jpg
│  ├─ dataset/evaluate_set
│  │  ├─ flag_tag/
│  │  │  ├─ 1.jpg
│  │  ├─ name_tag/
│  │  │  ├─ 1.jpg
│  ├─ model/
│  │  ├─ classes
│  │  ├─ feature.npy
│  │  ├─ img_paths
├─ FullDressUniform/
```


이 상태에서 validation.py를 다음과 같이 작성하고 실행시킵니다. 

```python
from OZEngine.parts_classifier.PartsClassifier import PartsClassifier

classifier = PartsClassifier('./')
res = classifier.evaluate(img)
print(res)  # 0.89
```

실행하면 evaluate_set폴더에 존재하는 이미지들이 얼마나 정확하게 분류가 되는지 확률로 
리턴받습니다.