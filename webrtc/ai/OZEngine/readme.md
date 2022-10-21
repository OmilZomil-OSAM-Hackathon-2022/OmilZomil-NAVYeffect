
## 사용법 (Usage)


### 파라미터

먼저 OZEngine 모듈을 import해줍니다.
``` python
import OZEngine
```

다음으로 객체를 생성해줍니다.

``` python
detector = OZEngine()
```

OZEngine class에는 여러 함수들이 있는데 우리는 분석하기 위해 1개의 함수만 있으면 충분합니다!
check_person, train_mode 2개의 파라미터를 받고있습니다. 

`def detect(check_person=True, train_mode=False):`

| 파라미터 | 기본값 | 설명 |
| ------ | ------ | ------ |
| check_person | False | 사람인식모델의 유무를 결정하는 파라미터입니다. |
| train_mode | False | [plugins/github/README.md][PlGh] |

참고 1: `check_person=True` 옵션을 주게 되면 detect함수 내부에 있는 사람인식모델이 동작하게 됩니다. 이 옵션이 필요할까요? 저희 Omil-Zomil에서는 위병소의 데이터를 실시간으로 분석합니다. 실시간으로 분석할 때 갑작스럽게 데이터가 몰려 서버에 부하가 심하게 가해지는 현상을 방지하기 위해 캐시(cache)기술이 적용된 DB를 사용합니다. DB에 저장하고 순차적으로 먼저 들어온 이미지데이터를 처리하기 때문에 처리하는 순간에는 사람인식이 보장되어있는 상태입니다. 결론적으로 저희 Omil-Zomil 서비스 내부에서 실시간 분석을 위해 별도로 만든 옵션입니다.

참고 2: `check_person` 옵션은 현재 Omil-Zomil서비스에서 제공하고 있는 모델(, )에 사용자데이터를 추가하여 학습을 해야 하는 상황이 존재할 때 사용합니다. `check_person=True`로 하게되면 실제 모델 내부에서는 각 파츠들을 분류하는 분류모델을 사용하지 않습니다. 대신 파츠로 추정되는 이미지들을 모두 저장시킵니다. 학습할 때는 이렇게 저장된 이미지들을 사람이 수동으로 분류를 하고 학습모델을 train시키면 됩니다. 

더 많은 정보는, [tutorial](https://www.jaided.ai/easyocr/tutorial)과 [API Documentation](https://www.jaided.ai/easyocr/documentation)를 읽어보세요

### 실행

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

결과값은 위와 같이 나옵니다. `component`에는 현재 병사가 착용하고 있는 파츠만 return 됩니다. 각 파츠들은 정복, 전투복, 근무복에 따라 다르게 표시됩니다. 

`boxed_img`는 원본 이미지 (detect함수에 들어간 원본 이미지) 위에 인식된 얼굴의 위치와 파츠들의 위치가 bounding box형태로 표시가 된 이미지 입니다. 이 이미지 역시 numpy 배열로 return이 됩니다.

 `roi`는 인식된 파츠 이미지들에 ROI(Region Of Image)가 적용된 이미지입니다. 한마디로 인식된 부분만 잘린 이미지들입니다. 



``` python
reader = easyocr.Reader(['ch_sim','en'], gpu=False)
```



#### Run on command line

```shell
$ easyocr -l ch_sim en -f chinese.jpg --detail=1 --gpu=True
```

## 사용자 모델 학습

For recognition model, [Read here](https://github.com/JaidedAI/EasyOCR/blob/master/custom_model.md).

For detection model (CRAFT), [Read here](https://github.com/JaidedAI/EasyOCR/blob/master/trainer/craft/README.md).

## Implementation Roadmap

- Handwritten support
- Restructure code to support swappable detection and recognition algorithms
The api should be as easy as
``` python
reader = easyocr.Reader(['en'], detection='DB', recognition = 'Transformer')
```
The idea is to be able to plug-in any state-of-the-art model into EasyOCR. There are a lot of geniuses trying to make better detection/recognition models, but we are not trying to be geniuses here. We just want to make their works quickly accessible to the public ... for free. (well, we believe most geniuses want their work to create a positive impact as fast/big as possible) The eline should be something like the below diagram. Grey slots are placeholders for changeable light blue modules.

![plan](examples/easyocr_framework.jpeg)

## Acknowledgement and References

This project is based on research and code from several papers and open-source repositories.

All deep learning execution is based on [Pytorch](https://pytorch.org). :heart:

Detection execution uses the CRAFT algorithm from this [official repository](https://github.com/clovaai/CRAFT-pytorch) and their [paper](https://arxiv.org/abs/1904.01941) (Thanks @YoungminBaek from [@clovaai](https://github.com/clovaai)). We also use their pretrained model. Training script is provided by [@gmuffiness](https://github.com/gmuffiness).

The recognition model is a CRNN ([paper](https://arxiv.org/abs/1507.05717)). It is composed of 3 main components: feature extraction (we are currently using [Resnet](https://arxiv.org/abs/1512.03385)) and VGG, sequence labeling ([LSTM](https://www.bioinf.jku.at/publications/older/2604.pdf)) and decoding ([CTC](https://www.cs.toronto.edu/~graves/icml_2006.pdf)). The training pipeline for recognition execution is a modified version of the [deep-text-recognition-benchmark](https://github.com/clovaai/deep-text-recognition-benchmark) framework. (Thanks [@ku21fan](https://github.com/ku21fan) from [@clovaai](https://github.com/clovaai)) This repository is a gem that deserves more recognition.

Beam search code is based on this [repository](https://github.com/githubharald/CTCDecoder) and his [blog](https://towardsdatascience.com/beam-search-decoding-in-ctc-trained-neural-networks-5a889a3d85a7). (Thanks [@githubharald](https://github.com/githubharald))

Data synthesis is based on [TextRecognitionDataGenerator](https://github.com/Belval/TextRecognitionDataGenerator). (Thanks [@Belval](https://github.com/Belval))

And a good read about CTC from distill.pub [here](https://distill.pub/2017/ctc/).

## Want To Contribute?

Let's advance humanity together by making AI available to everyone!

3 ways to contribute:

**Coder:** Please send a PR for small bugs/improvements. For bigger ones, discuss with us by opening an issue first. There is a list of possible bug/improvement issues tagged with ['PR WELCOME'](https://github.com/JaidedAI/EasyOCR/issues?q=is%3Aissue+is%3Aopen+label%3A%22PR+WELCOME%22).

**User:** Tell us how EasyOCR benefits you/your organization to encourage further development. Also post failure cases in [Issue  Section](https://github.com/JaidedAI/EasyOCR/issues) to help improve future models.

**Tech leader/Guru:** If you found this library useful, please spread the word! (See [Yann Lecun's post](https://www.facebook.com/yann.lecun/posts/10157018122787143) about EasyOCR)

## GPU가속 지원

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

## Github Issues

Due to limited resources, an issue older than 6 months will be automatically closed. Please open an issue again if it is critical.

## Business Inquiries

For Enterprise Support, [Jaided AI](https://www.jaided.ai/) offers full service for custom OCR/AI systems from implementation, training/finetuning and deployment. Click [here](https://www.jaided.ai/contactus?ref=github) to contact us.
