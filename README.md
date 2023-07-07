<h2 align="center">
Korean OCR using paddleOCR
</h2>

<div align="center">
  <img src="https://img.shields.io/badge/license-Apache%202-dfd.svg">
  <img src="https://img.shields.io/badge/python-3.7+-aff.svg"/>
  <img src="https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-pink.svg"/>
</div>

This is a Korean OCR Python code using the paddleOCR library

## Requirements

- Python 3.7+
- paddlepaddle
- paddleocr

You can install it from PyPI:

```shell
pip install paddlepaddle # for gpu user please install paddlepaddle-gpu
pip install paddleocr
```

## PaddleOCR

Awesome multilingual OCR toolkits based on PaddlePaddle (practical ultra lightweight OCR system, support 80+ languages recognition, provide data annotation and synthesis tools, support training and deployment among server, mobile, embedded and IoT devices)

This repository is simply configured for PaddleOCR functionality and inspection. If you want to check out the various features of paddleOCR, please refer to the [paddleOCR repository](https://github.com/PaddlePaddle/PaddleOCR).

```python
from main import MyPaddleOCR
 
ocr = MyPaddleOCR()
```

**지원 가능한 언어 목록을 조회**하는 기능입니다.

```python
ocr.get_available_langs()
```

Output :

```shell
Available Language : ['ch', 'en', 'korean', 'japan', 'chinese_cht', 'ta', 'te', 'ka', 'latin', 'arabic', 'cyrillic', 'devanagari', 'french', 'german', 'structure']
```

**사용가능한 Model을 조회**하는 기능입니다.

```python
ocr.get_available_models()
```

Output :

```shell
#1 Model Vesion : [PP-OCRv3] - Language : ['ch', 'en', 'korean', 'japan', 'chinese_cht', 'ta', 'te', 'ka', 'latin', 'arabic', 'cyrillic', 'devanagari']
#2 Model Vesion : [PP-OCRv2] - Language : ['ch']
#3 Model Vesion : [PP-OCR] - Language : ['ch', 'en', 'french', 'german', 'korean', 'japan', 'chinese_cht', 'ta', 'te', 'ka', 'latin', 'arabic', 'cyrillic', 'devanagari', 'structure']
```

**OCR** (Optical Character Recognition)

```python
img_path = 'assets/images/test_image_3.jpg'
ocr.run_ocr(img_path, debug=True)
```

<div align="center">
<img src="https://blog.kakaocdn.net/dn/ynA1O/btsmwXvgqja/Rpo9KTE1oUrECSWqa5FKVK/img.png" hight="50%">
</div>

Output : 

```shell
[2023/07/06 00:10:29] ppocr DEBUG: dt_boxes num : 4, elapse : 0.8806350231170654
[2023/07/06 00:10:29] ppocr DEBUG: rec_res num  : 4, elapse : 0.25487518310546875
['아래한글', '한글문서', '디자인', '202204']
```