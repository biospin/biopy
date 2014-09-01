name: inverse
layout: true

---
class: title, center, middle, inverse

슬라이드, 미안하다!
# <span class="sky">호</span>호호 <span class="sky">하</span> 하하 <span class="sky">크</span>크크
.footnote[
- [Rigel](http://twitter.com/kozazz) (곽두환)
- [kozazz](https://github.com/kozazz) on GitHub]
- 출처 : http://www.lucypark.kr/slides/2014-pyconkr

---
.left-column[
## 개요
]

.right-column[
NLTK 덕에 파이썬으로 자연어처리를 하는 것이 편리해졌다.<br>
단, 한국어만 분석하려하지 않는다면.<br>

파이썬으로 한국어를 분석할 수는 없을까?<br>
국문, 영문, 중문 등 다양한 문자가 섞여 있는 문서는 어떻게 분석할 수 있을까?

이 발표에서는 자연어처리의 기초적인 개념을 다룬 후, NLTK 등의 자연어처리 라이브러리와 한국어 분석을 위해 개발중인 KoNLPy를 소개한다. 또, 파이썬으로 한국어를 분석할 때 유용한 몇 가지 트릭을 공유한다.

<br>

.small[
- KoNLPy docs: http://konlpy.readthedocs.org
- Slides URL: http://www.lucypark.kr/slides/2014-pyconkr
- Slides code: https://gist.github.com/e9t/546faa368424e04e25c7
]
]

---
.left-column[
<img src="me.jpg" width="100%">
## **박은정**
(a.k.a. lucypark, echojuliett, e9t)
]

.right-column[
<!--(데이터 분석하는 개발자 아닙니다.)-->
### 개발하는 **데이터 분석가**.

- 서울대학교 데이터마이닝 센터 박사과정
- "[대한민국 정치의 모든 것](http://pokr.kr)" 만드는 팀포퐁 멤버
- Just another yak shaver...

<br><br><br>

.small.gray[
<pre>
11:49 <@sanxiyn> 또다시 yak shaving의 신비한 세계
11:51 <@sanxiyn> yak shaving이 뭔지 다 아시죠?
11:51 <디토군> 방금 찾아보고 왔음
11:51 <@mana> (조용히 설명을 기대중)
11:51 <@sanxiyn> 나무를 베려고 하는데
11:52 <@sanxiyn> 도끼질을 하다가
11:52 <@sanxiyn> 도끼가 더 잘 들면 나무를 쉽게 벨텐데 해서
11:52 <@sanxiyn> 도끼 날을 세우다가
11:52 <@sanxiyn> 도끼 가는 돌이 더 좋으면 도끼 날을 더 빨리 세울텐데 해서
11:52 <@sanxiyn> 좋은 숫돌이 있는 곳을 수소문해 보니
11:52 <@mana> …
11:52 <&홍민희> 그거 전형적인 제 행동이네요
11:52 <@sanxiyn> 저 멀이 어디에 세계 최고의 숫돌이 난다고
11:52 <@sanxiyn> 거기까지 야크를 타고 가려다가
11:52 <@mana> 항상하던 짓이라서 타이핑을 할 수 없었습니다
11:52 <@sanxiyn> 야크 털을 깎아서…
11:52 <@sanxiyn> etc.
</pre>
]]



---
class: center

.full-image[![](francis.png)]

"caricature"

---
class: center, middle, inverse, full-text

".gold[사람의 생김새]를 결정짓는 것은<br>
.gold[골격과 피부의 미묘한 변화에서 비롯되는 차이]점이고,<br>
그 차이점을 없애 버린다면 모든 사람의 생김새는<br>
똑같을 것입니다."

.pull-right[-- 만화가 김충원]

---
class: center, middle, inverse, full-text

".gold[데이터]를 결정짓는 것은<br>
.gold[행과 열의 미묘한 변화에서 비롯되는 차이]점이고,<br>
그 차이점을 없애 버린다면 모든 데이터는<br>
똑같을 것입니다."

---
class: center, middle, full-text

수많은 공통점을 두고도<br>
차이를 만드는 요인.

데이터 분석의 관점에서는:<br>
.blue[**"Features"**]

---
class: center, middle, full-text

문서 간 차이를 만드는
.blue[**"Features"**]는
뭘까?

---
class: middle
.full-image[![](document.png)]

---
class: middle
.full-image[![](morphemes.png)]

---
class: center, middle, full-text

.blue[**형태소**]

언어의 최소 의미 단위.

.footnote[\* 영어는 tokenizing, stemming으로 충분한 경우도 있지만 결국 마찬가지. .small.gray[ex: "unbreakable"=="un-"+"break"+"-able"]]

---
# 형태소분석 with C/C++ & Java

.full-image[![](analyzers.png)]

- *corpus linguistics* == 언어 분석을 computational하게 해보자!
- 1995년, KTS를 시작으로 국내외에서 여러 "오픈소스" 형태소 분석기가 개발됨
- 형태소 분석기를 만든다 == 알고리즘 구현 + 방대한 코퍼스 기반으로 사전 구축
    - 한마디로, 정말 대단한 작업

.footnote[\* 형태소 분석기 링크들은 여기에: http://konlpy.readthedocs.org/en/latest/references]

---
class: center, middle, full-text

이러한 역작들을,<br>
.blue[더 많은 사람]들이 .blue[쉽게] 이용하게 할 수 있을까?

---
class: center, middle, full-text

그러한 관점에서<br>
누구나 쉽게 NLP를 할 수 있게 해준 패키지 두 개:

.left[
- **KoNLP**, for R
- **NLTK**, for Python
]

---
# **KoNLP**, for R .font-30[https://github.com/haven-jeon/KoNLP]

.mid-image[![](konlp.png)]

- 한나눔 형태소 분석기 R interface
- 세종계획.small.gray[한국어 코퍼스, 사전 등을 마련한 10년 계획 정부사업]의 확장적 사용
- 그 외 NLP를 편리하게 하는 각종 함수 구현
- 많은 down-to-earth 예제를 담은 documentation
- "Python으로도 이런게 있으면 좋겠다!" .small.blue[이름에도 내포돼있듯 KoNLPy의 가장 큰 inspiration!]

---
# **NLTK**, for Python .font-30[http://nltk.org]

.mid-image[![](nltk.png)]

- Porter, snowball, Lancaster 등 다양한 stemming 알고리즘 포함
- 그 외 chunking, NER, classification 알고리즘 포함
- 50개가 넘는 (주로 영어지만 다양한 언어의) 코퍼스 포함
- 역시 풍부한 문서
- (Natural) language free, platform free, and free
- "한국어만 지원되면 정말 좋겠다!"

.footnote[\* NLTK는 Language-free한 속성 때문에 파이썬 한국어 NLP에도 유용하게 이용할 수 있습니다. (예시: [Collocation 찾기](http://konlpy.readthedocs.org/en/latest/examples/collocations/))]

---
class: center, middle, full-text

.blue[파이썬]으로 <s>.gray[형태소 분석]</s>,<br>
.blue[한국어 NLP] 할 수 있으면 정말 좋겠네

.left[
1. 형태소 분석기 뿐 아니라, 더 많은 자연어 처리 기능 & 코퍼스를 포괄하면서
1. 여러 형태소 분석기 중에서는 목적/취향에 맞는 것을 쉽게 선택할 수 있게
1. 누구나 참여할 수 있는, 여과없는 오픈소스를
1. 상세한 예제를 담은 문서와 함께
1. 가장 Pythonic 한 형태로
]

.footnote[(...로 만드는 것이 "목표".)]

---

# **KoNLPy**, for Python .font-30[http://konlpy.rtfd.org]

.mid-image[![](konlpy.png)]

- "Standing on the shoulders of giants"
    - 2014년 7월, 한나눔 형태소 분석기만 담아 첫 릴리즈
    - 2014년 8월, 꼬꼬마, MeCab-ko 형태소 분석기도 포함하여 v0.3.0 릴리즈
    - 국회 의안 등 재사용/재배포가 가능한 공문서 위주로 toying data 추가
    - 그 외 각종 튜토리얼, `konlpy.utils.pprint` 등 편리한 함수 추가
- [GitHub](http://github.com/e9t/konlpy)을 통해 누구나 논의와 개발에 참여할 수 있습니다!

---
class: center, middle, full-text

한 번 써볼까요?

---
class: middle

- Installation

```bash
$ pip install JPype1 # Aㅏ... dependencies...
$ pip install konlpy
```

---

```python
>>> from konlpy.tag import Kkma
>>> from konlpy.utils import pprint # 파이썬 2에서 편리한 출력을 위함
>>> kkma = Kkma()
>>> pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
[네, 안녕하세요..,
 반갑습니다.]
>>> pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'))
[질문,
 건의,
 건의사항,
 사항,
 깃헙,
 이슈,
 트래커]
>>> pprint(kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^')
[(오류, NNG),
 (보고, NNG),
 (는, JX),
 (실행, NNG),
 (환경, NNG),
 (,, SP),
 (에러, NNG),
 (메세지, NNG),
 (와, JKM),
 (함께, MAG),
 (설명, NNG),
 (을, JKO),
 (최대한, NNG),
 (상세히, MAG),
 (!, SF),
 (^^, EMO)]
```
---

.scroll[
```python
>>> from konlpy.tag import *
>>> from konlpy.utils import pprint
>>> engines = [Kkma(), Hannanum(), Mecab()]
>>> s = u"갤럭시는 화면이 큰데, 좋은데?" # 'ㄴ데', '은데'가 다르다는 것에 주목!
>>> for e in engines:
...     print e
...     pprint(e.pos(s))
<konlpy.tag._kkma.Kkma instance at 0x2d292d8>
[(갤럭시, UN),
 (는, JX),
 (화면, NNG),
 (이, JKS),
 (크, VA),
 (ㄴ데, ECE),
 (,, SP),
 (좋, VA),
 (은데, ECD),
 (?, SF)]
<konlpy.tag._hannanum.Hannanum instance at 0x2d299e0>
[(갤럭시, N),
 (는, J),
 (화면, N),
 (이, J),
 (크, P),
 (ㄴ데, E),
 (,, S),
 (좋, P),
 (은, E),
 (데, N),
 (?, S)]
<konlpy.tag._mecab.Mecab instance at 0x2d29950>
[(갤럭시, NNP),
 (는, JX),
 (화면, NNG),
 (이, JKS),
 (큰데, VA+EC),
 (,, SC),
 (좋, VA),
 (은데, EF),
 (?, SF)]
```
]

---

- 태그셋 비교: [Korean POS tags comparison chart](https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8/edit?usp=sharing)

.full-image[![](tags.png)]

---
- 형태소 분석 모듈 간 성능 비교

    - 형태소 분석기는 속도, 메모리 사용, 정확도 등으로 성능 평가
    - One-size-fits-all 이라기보다는 서로 장단점이 있는 경우가 많음
    - 알고리즘 뿐 아니라 사전의 영향도 매우\*\*2 큼
    - 자신의 목적/취향에 맞는 분석기+사전 조합을 사용

.center[![](time.png)]

.footnote[
\* *Warning!*<br>
(1) 형태소 분석기 간 직접적인 비교가 아니라, KoNLPy 내부 모듈 간 비교입니다.<br>
(2) POS tagging은 형태소 분석과 구분됩니다. 자세한 설명은 구글신께 양보드립니다 :)]

---
class: center, middle, full-text

좀 더 재밌는걸 해봅시다!

---
# 예제: 워드클라우드 그리기

- 목적: 파이썬만으로 웹문서에서 중요한 명사를 뽑아 워드클라우드로 그리기!

.width-50.small-image[![](text.png)]
.width-50.small-image[![](wordcloud.png)]

.footnote[
\* 코드는 지면상 여기에서: http://konlpy.readthedocs.org/en/latest/examples/wordcloud/ (재밌는 예제들도 더 있어요!)
]

---
- 이걸 응용해서 만든 것이:

[.full-image[![](pokr.png)]](http://pokr.kr/person/1958194)
http://pokr.kr/person/1958194

---
# Future works for KoNLPy

1. 사전 interface 통일
1. ``konlpy.download()``: 코퍼스, 사전 등 data file을 소스코드에서 분리
1. GCJ 등을 활용해서 JVM을 따로 구동하지 않는 방법 고려
1. Python3 support
1. 한국어 documentation?


---
class: center, middle, full-text

시간이 좀 남았나요?

---
# 몇 가지 트릭

- 한글 파일 읽기: ["Decode early, encode late"](http://farmdev.com/talks/unicode/)

    ```python
    >>> with open('somefile.txt', 'r') as f:
    ...    doc = f.read().decode('utf-8')
    ```

    ```python
    >>> import codecs
    >>> codecs.open('somefile.txt', encoding='utf-8')
    ```

- sublee님의 [Hangulize](https://github.com/sublee/hangulize)

    ```python
    >>> from hangulize import hangulize
    >>> print hangulize('Guido van Rossum', 'nld')
    히도 판로쉼
    ```

---
# 몇 가지 트릭

- 문자의 정체 확인하기

    ```python
    >>> from unicodedata import name
    >>> print '%s, %s, %s' % (name(u"ㆍ"), name(u"․"), name(u"･"))
    HANGUL LETTER ARAEA, ONE DOT LEADER, HALFWIDTH KATAKANA MIDDLE DOT
    ```

    ```python
    >>> "･".decode("unicode-escape")
    u'\xef\xbd\xa5'
    >>> ord(u"･"), repr(u"･")
    (65381, "u'\\uff65'")
    ```

- 특수문자를 제외하고 어절을 얻고 싶은 경우

    ```python
    >>> import regex
    >>> regex.findall(ur'\p{Hangul}+', u'다람쥐, 헌 쳇바퀴에 타고파.')
    [u'\ub2e4\ub78c\uc950', u'\ud5cc', u'\uccc7\ubc14\ud034\uc5d0', u'\ud0c0\uace0\ud30c']
    ```

---
# 몇 가지 트릭

- 한글 romanize하기

    ```python
    >>> from unidecode import unidecode
    >>> unidecode(u'파이콘')
    'paikon'
    ```

- 한자, 한글, 영문가 섞여 있는 경우

    - Multilingual NLP에서 제안하는 다양한 접근법이 있습니다.
    - 간단한 꼼수 한 가지는: "한자 전처리, 영문 후처리"
        - 한자는 transliterate하고 (ex: '丁新闻' -> 정신문)
        - 한국어 처리를 한 후에 (ex: POS tagging)
        - 영문으로 분류된 tag에 한해 따로 stemming 등을 거침

---
class: center, middle, inverse, full-text

감사합니다 :D

http://lucypark.kr<br>
[@echojuliett](http://twitter.com/echojuliett)
