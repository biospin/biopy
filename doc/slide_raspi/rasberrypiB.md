name: inverse
layout: true
class: middle, inverse, full-text

라즈베리 os 다운로드
os 다운로드. 종류 다양 raspbian 를 받자
http://www.raspberrypi.org/downloads/
raspbian zip download

---

class: middle, inverse, full-text

win32diskimager
윈도우 프로그램이용
img 파일을 sd 카드에 씌움
라즈베리파이 부팅 붕~

---

class: middle, inverse, full-text

라즈베리 b+ GPIO
<img src="http://data.designspark.info/uploads/images/53bc258dc6c0425cb44870b50ab30621" alt="img" style="width: 450px;"/>

---

class: middle, inverse, full-text

![실물](/doc/img/rasledr.jpg)
![구조도](/doc/img/rasled.png)

배선그리기
http://fritzing.org/download/
---

class: middle, inverse, full-text

```
sudo apt-get update
sudo apt-get install python-rpi.gpio

sudo python
>>>import RPi.GPIO as GPIO
>>>GPIO.setmode(GPIO.BCM)
>>>GPIO.setup(17, GPIO.OUT)
>>>GPIO.setup(17, GPIO.HIGH)
>>>GPIO.setup(17, GPIO.LOW)

```

---
class: middle, inverse, full-text

방금그라디오
쑥갓키우기

---

class: middle, inverse, full-text

<iframe width="560" height="315" src="//www.youtube.com/embed/kERdJyF-7RM" frameborder="0" allowfullscreen></iframe>

http://www.youtube.com/watch?v=kERdJyF-7RM
---
class: center, middle, inverse, full-text

".gold[라디오 노래]만 듣고 싶다.<br>
.gold[광고]는 안듣고 싶은데..<br>
노래만 골라들으면 안되나요<br>
노래만 듣고 싶다. "

.pull-right[-- 노래만 듣고 싶은이]

---

class: center, middle, inverse, full-text

```
import 라디오모듈

r.upVolume(1)
r.upDownVolume(1)

import 라디오모듈
import lcd디스플레이

data = request.url(방금그록라디오)
최신노래정보 = data.parse.get최근꺼

최신노래.제목
최신노래.라디오채널
최신노래.가수

d.display(제목)
d.display(채널)
d.display(가수)

r.channelt(라디오채널)
```

---
class: center, middle, inverse, full-text

".gold[선곡이짱] 방송국 작가분들 선곡에 감사합니다.<br>
.gold[광고는 NO!] 전하는 말씀은 듣고 싶지 않아요<br>
실시간 노래가 술술.. 방금 그 라디오!!

---

class: middle, inverse, full-text
# 준비물

1. [방금그곡api](http://music.daum.net/onair/timeline)
1. python3
1. raspberry pi
1. [TEA5767 FM 디지털 스테레오 라디오 모듈](http://itempage3.auction.co.kr/DetailView.aspx?ItemNo=A955319132&frm3=V2)
1. [Nokia 5110 LCD](http://www.devicemart.co.kr/31029)
1. [스피커](http://www.10x10.co.kr/shopping/category_prd.asp?itemid=898765&rdsite=nvshop_sp&NaPm=ct%3Dhzw68blk%7Cci%3Dd6f9db6ebddfcf32f6bd366d6b80154138ec0cdd%7Ctr%3Dsl%7Csn%3D219718%7Chk%3D69a0516a1216cf93849a469bda19f1d5330d3df7)
1. [빵판](http://www.devicemart.co.kr/32298)
1. 스위치
1. [점퍼케이블](http://www.devicemart.co.kr/32284)

---
class: middle, middle, inverse, full-text

 선연결
- https://github.com/XavierBerger/pcd8544
- ![](https://camo.githubusercontent.com/7e1fdf3d7a138e6bad58c84361114fbc2cea8ff5/68747470733a2f2f7261772e6769746875622e636f6d2f5861766965724265726765722f706364383534342f6d61737465722f646f632f50434438353434776972696e672e706e67)
---
class:  middle, inverse, full-text
# 작업

- [pcd8544 Python library 설치](https://github.com/XavierBerger/pcd8544)
- pil 라이브러리 python2 에서만 실행;;
- [python3 사용하기 위해 Pillow lib 설치한다](http://pillow.readthedocs.org/en/latest/installation.html)
- python3 각종 에러가 발생하는데 lcd.py 적절히 수정해 준다.
- 한글폰트 설치 sudo apt-get install ttf-unfonts-core
- 각종 설치
    ```python
    sudo pip-3.2 install wiringpi
    sudo pip-3.2 install wiringpi2
    sudo pip-3.2 install spidev
    sudo pip-3.2 install Pillow
    ```
---
class:  middle, inverse, full-text

# code
- [onair.py source](https://github.com/onairradio/onairradio.github.io/blob/master/onair.py)

    ```python
    ...
    ch = {825: (97.3, "KBS1 라디오"), 824: ( 93.1, "KBS FM1")
    , 827: (106.1, "KBS2 라디오"), 826: ( 89.1, "KBS FM2")
    , 828: (111, "KBS 3라디오")

    ...
    url = 'http://music.daum.net/onair/songlist.json?type=top&searchDate='
    resp = requests.post(url=url)
    data = json.loads(resp.text)
    ...
    resp = requests.post(url=url)
    data = json.loads(resp.text)

    for song in reversed(data['songList']):
        if song['channel']['channelType'] ...
    ```
---
class: middle, inverse, full-text

쑥갓키우기
https://play.google.com/store/search?q=%EC%91%A5%EA%B0%93%ED%82%A4%EC%9A%B0%EA%B8%B0&hl=ko

---

class: middle, middle, inverse, full-text
앞으로 만들꺼
메이크페어
해리포토 마법 지팡이
음성 + 동장인식..

---

class: middle, middle, inverse, full-text
라즈베리파이 공모전
http://happysntcontest.kofst.or.kr/index.php

공모전 응모자 중교육
http://happysntcontest.kofst.or.kr/file/2014%ED%96%89%EB%B3%B5%ED%95%9C%EA%B3%BC%ED%95%99%EA%B8%B0%EC%88%A0%EA%B3%B5%EB%AA%A8%EC%A0%84%20%EA%B0%9C%EB%B0%9C%EC%A7%80%EC%9B%90%20%EA%B5%90%EC%9C%A1%20%EC%95%88%EB%82%B4_141014.pdf

라즈베리파이교육
서울 1.8(토)~9(일), 09~18시 전자부품연구원 케티파트너스 지하1층 교육장

---

class: middle, middle, inverse, full-text

설문
https://dubu.typeform.com/to/LXbQui

--

class: middle, inverse, full-text

![](img/Raspberry_Pi_B+_top.jpg)

감사합니다

---