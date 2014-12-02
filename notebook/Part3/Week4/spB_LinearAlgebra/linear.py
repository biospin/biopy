
# coding: utf-8

# ---
# 
# <h1> 보강 : 행렬에 관한 python 활용 </h1>
# 
# ---
# 

# <h2> 1. 행렬의 기본 정의 </h2>
# 행렬 기본, 차수, 명칭 등등
# 
# <h2> 2. 기본 행렬 연산 </h2>
# 간단한 행렬 연산
# 
# <h2> 3. 행렬대수의 기초 </h2>
# <br/>
# 
# ---
# 

# <h3> 1. 행렬의 기본 정의 </h3>
# 
# **m x n 행렬 = m 행, n 열**
# 
# **n x n 행렬 = 정방행렬 (square matrix)**
# 
# **1 x 1 행렬 = 스칼라 (scalar)**
# 
# **m x 1 행렬 = 열벡터 (column vector)**
# 
# **1 x n 행렬 = 행벡터 (row vector)**
# 
# <br>
# 
# **0 행렬 = (zero matrix) 모든 원소가 0 **
# 
# **I 행렬 = 항등행렬 (identity matrix), 대각선 1, 나머지 0**
# 
# **D 행렬 = 대각행렬 (diagonal matrix), 대각선 외는 모두 0인 정방행렬**
# 
# **T 행렬 = 삼각행렬 (triangular matrix), 대각선 기준으로 한쪽에만 값이 있는 행렬**
# 
# **S 행렬 = 대칭행렬 (symmetric matrix), 대각선 기준 대칭**
# 
# **P 행렬 = 치환행렬 (permutation matrix), 각각의 행과열 입장에서 1이 하나이고 나머진 0**
# 
# <br>
# 
# **분할행렬(partitioned matrix) = 기존의 행렬은 작은단위 행렬로 표현**
# 
# **블록록대각행렬(block diagonal matrix) = 주대각선 위치한 정사각형 부 행렬들을 제외하고는 다른 부 행렬을 모두 0행렬**

# In[1]:

import numpy as np
import scipy as sc
import scipy.linalg
# scipy linalg 라이브러리 레퍼런스 
# http://docs.scipy.org/doc/scipy-0.14.0/reference/linalg.html


# In[2]:

# 대각행렬 
D = np.array([[1,0,0],
              [0,2,0],
              [0,0,3]])


# In[3]:

# 삼각행렬
T = np.array([[1,2,3],
              [0,3,4],
              [0,0,5]])


# In[4]:

# 대칭행렬
S = np.array([[1,2,3],
              [2,1,2],
              [3,2,1]])


# In[5]:

# 치환행렬 
P = np.array([[0,1,0],
              [1,0,0],
              [0,0,1]])


# In[6]:

# 분할행렬
p11 = np.array([[1,2],
                [3,4]])
p12 = np.array([[5],
                [6]])
p21 = np.array([[7,8]])
p22 = np.array([[9]])

p1 = np.column_stack([p11, p12])
p2 = np.column_stack([p21, p22])
p = np.vstack([p1,p2])
p


# In[7]:

# 블록록대각행렬(block diagonal matrix)
b = np.array([[1,2,0,0,0],
              [3,4,0,0,0],
              [0,0,5,0,0],
              [0,0,0,6,7],
              [0,0,0,8,9]])
b


# ---
# <h3> 2. 기본 행렬 연산 </h3>
# ---
# 2.1 전치
# 
# 2.2 동등
# 
# 2.3 행렬 덧셈,뺄셈
# 
# 2.4 행렬 곱셈
# 
# 2.5 크로넥터 곱
# 

# <h5> 2.1 전치 </h5>

# In[8]:

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
np.transpose(A)


# <h5> 2.2 동등 </h5>

# In[9]:

np.equal(A,A)


# <h5> 2.3 행렬 덧셈, 뺄셈 </h5>

# In[10]:

B = np.array([[1,1,1],
              [1,1,1],
              [1,1,1]])

A + B


# In[11]:

A - B


# <h5> 2.4 행렬 곱 </h5>

# In[12]:

A * 2


# In[13]:

C = np.array([[1],[1],[1]])
np.dot(A, C)


# <h5> 2.5 크로넥터 곱 </h5>
# 
# m x n 행렬 ⓧ l x k 행렬
# 
# => ml x nk 행렬

# In[14]:

sc.linalg.kron(A,C)


# In[15]:

sc.kron(A,C)


# In[16]:

np.kron(A,C)


# ---
# <h3> 3. 행렬 대수의 기초 </h3>
# ---
# 3.1 대각합 (trace)
# 
# 3.2 행렬식 (deteminant)
# 
# 3.3 계수 (rank) 와 비특이행렬 (nonsingular matrix)
# 
# 3.4 선형종속 (linear dependence)
# 
# 3.5 역행렬 (inverse matrix)
# 
# 3.6 선형등식체계 해
# 
# 3.7 고유값(eigenvalue) 과 고유벡터(eigenvector)
# 
# 3.8 직교행렬과 대칭행렬의 대각화
# 
# 3.9 멱등행렬 (idempotent matrix)
# 
# 3.10 이차형태 (quadratic form)
# 
# 3.11 확률변수(random variables) 집합의 공분산행렬 (covariance matrix)
# 
# 3.12 콜레스키 분해 (Cholesky decomposition)
# 
# 3.13 QR 분해
# 
# 3.14 특이값 분해 (SVD 분해)
# 
# 3.15 벡터 및 행렬 노옴 (norm)
# 
# ---

# <h5> 3.1 대각합 trace </h5>
# 
# **대각합의 속성**
# 
# > tr(kA) = k * tr(A)
# 
# > tr(A + B) = tr(A) + tr(B)
# 
# > tr(A') = tr(A)
# 
# > tr(AB) = tr(BA)

# In[17]:

print A
sc.trace(A)


# <h5> 3.2 행렬식 deteminant </h5>
# 
# 행렬 A 의 deteminant = |A| 로 표시
# 
# **행렬식과 관련 속성**
# 
# > |A'| = |A|
# 
# > |AB| = |A||B|
# 
# > 대각행렬 A 이면, |A| = a<sub>11</sub>a<sub>22</sub>  ...  a<sub>mm</sub> 이다. (대각의 곱)
# 
# > 한 행이라도 모두 0 이면 |A| = 0
# 
# > 두 행 또는 두 열이 동등하면 |A| = 0
# 
# > 한 행이나 한 열이 다른 행이나 열의 곱이면 |A| = 0

# In[18]:

sc.linalg.det(A)


# <h5> 3.3 계수와 비특이행렬 </h5>
# 
# **계수(rank)** 란 행렬의 선형독립인 행(또는 열) 의 '최대 수'를 말한다.
# 
# 다른 행이나 열이 어떤 행이나 열의 스칼라 곱으로 표현 가능하지 않은 갯수이다.
# 
# <pre>
# S = [1 2]
#     [2 4]
# </pre>
#          
# 의 계수인 r(S) = 1 이다.
# 
# 2번째 행은 1번째 행의 *2 으로 구해지기 때문.
# 
# |S| = 0 이 나오며, 따라서 특이행렬이라고 한다.
# 
# <br/>
# 
# 만약 |S| = 0 이면,
# 
# S 는 **특이행렬(singular matrix)** 이고,
# 
# |S| != 0 이면 **비특이행렬 (nonsingular matrix)** 이라고 한다.

# In[19]:

S = np.array([[1,2],[2,4]])
np.linalg.matrix_rank(S) # rank 계수가 1 != 2


# In[20]:

sc.linalg.det(S) # 행렬식 = 0 => 특이행렬이다.


# **행렬 계수 속성**
# 
# > 0 행렬은 계수가 0 이다.
# 
# > m x n 행렬이면, r(A) <= min(m,n)
# 
# > r(AB) <= min(r(A), r(B))
# 
# > r(A) = r(A') = r(AA') = r(A'A)
# 
# > 행렬계수는 비특이행렬의 전승, 후승에 의해 변하지 않는다.(?)
# 
# > m x n 행렬일때,
#   A 가 비특이행렬(|A| != 0) 이면 r(A) = n 이고,
#   A 가 특이행렬(|A| = 0) 이면 r(A) < n 이다.

# <h5> 3.4 선형 종속 (linear dependence)</h5>
# 
# n 개의 벡터{x1, x2, .. xn} 과 n 개의 스칼라 {k1, k2, .. kn}에서 
# 
# k1x1 + k2x2 + ... + knxn = 0 을 충족하는 
# 
# 0이 아닌 스칼라 집합이 있다면 선형종속이다.
# 
# 쉽게 말해,
# 
# 어떤 벡터 x<sub>i</sub> 는 다른 벡터의 조합으로 나타낼 수 있을 경우.
# 
# 그렇지 않은 경우를 선형독립 (linear independence) 라고 한다.

# In[21]:

X = np.array([[4,5,2,14],
              [3,9,6,21],
              [8,10,7,28],
              [1,2,9,5]])

# 각 열벡터 생성
x1 = X[:,[0]] 
x2 = X[:,[1]]
x3 = X[:,[2]]
x4 = X[:,[3]]
x1


# In[22]:

# 선형 종속 검증 
x1 + 2*x2 + 0*x3 - x4 


# In[23]:

print sc.linalg.det(X)
round(sc.linalg.det(X))


# 선형종속 => det(X) = 0 => 특이행렬 singular matrix   

# <h5> 3.5 역행렬 </h5>
# 
# n x n 정방행렬 A 의 역행렬(inverse matrix)은 
# 
# A 의 전승 또는 후승(앞에서 곱, 뒤에서 곱) 에 의해 항등행렬 I 를 생성하는 행렬로서,
# 
# A<sup>-1</sup> 으로 표기한다.
# 
# 역행렬이 존재하기 위해서는 **비특이행렬** 이여야 한다.
# 
# 역행렬을 구하는 방법.
# 
# A<sup>-1</sup> = 1 / |A| * adjA
# 
# 여인자행렬 (cofactor matrix) 의 전치된 행렬이 
# 
# 수반행렬 (adjoint matrix) adjA 라고 한다.
# 
# 

# In[24]:

A = np.array([[1,2],[3,4]])
inv_A = sc.linalg.inv(A)
inv_A


# In[25]:

sc.dot(A, inv_A)


# In[26]:

# np.round 를 통해 항등행렬이 맞는지 확인하자.
np.round(sc.dot(A, inv_A))


# In[27]:

# 일반 함수 round 를 행렬함수로 바꾸어 적용해보자.
vfunc = np.vectorize(round)
vfunc(sc.dot(A, inv_A))


# **역행렬 속성**
# 
# > 역행렬이 존재하면 그것이 유일하다.
# 
# > (A')<sup>-1</sup> = (A<sup>-1</sup>)'
# 
# > (AB)<sup>-1</sup> = B<sup>-1</sup>A<sup>-1</sup>
# 
# > |A<sup>-1</sup>| = 1/|A|

# <h5> 3.6 선형등식체계의 해 </h5>
# 
# linear equation system 은 표현형태 
# 
# > Ax = h
# 
# **계수행렬(coefficient matrix) A** 는 m x n 이고,
# 
# **변수행렬 x**는 n x 1 이고,
# 
# **상수행렬 h**는 m x 1 형태를 갖는다.
# 
# > x = A<sup>-1</sup>h
# 
# 만약 A 가 정방행렬이고 비특이행렬이면, 역행렬이 존재하고, 따라서 해는 유일하다.

# In[28]:

A = np.array([[3,5],[4,2]])
h = np.array([[13],[8]])
A


# In[29]:

sc.linalg.det(A) # 역행렬 존재여부 확인


# In[30]:

inv_A = sc.linalg.inv(A) # 역행렬


# In[31]:

sc.dot(inv_A, h) # x = inv(A) * h


# In[32]:

sc.linalg.solve(A, h) # 편리하게 선형등식체계 해를 구하는 함수 제공


# In[33]:

# 해를 도출할 수 없는 경우
A = np.array([[1,2],[2,4]])
print "deteminant = ", sc.linalg.det(A)
inv_A = sc.linalg.inv(A) # 특이행렬의 역행렬을 구하려고 하면 에러발생


# <h5> 3.7 고유값과 고유벡터 </h5>
# 
# n * n 정방행렬 A 에 대하여 Ax = Lx 인 스칼라 값 L, 벡터 x (영벡터 아님) 가 존재할때, 
# 
# L 을 고유값, x 를 고유벡터라고 한다.
# 
# A 라는 행렬을 일종의 변환행렬이라고 생각할때, 
# 
# 그 변환에 대해서 (크기만 변화) 방향이 변하지 않는 벡터이기 때문에 고유벡터라고 한다.
# 
# 고유값-고유벡터의 갯수는 0 ~ 최대 n 개이다.
# 
# 고유벡터를 구해보자. 
# 
# Ax = Lx
# 
# Ax - Lx = 0
# 
# (A - LI)x = 0 # 스칼라값 L 에 항등행렬 I 를 곱해 행렬뺄셈을 한다.
# 
# 여기서 (A - LI) 행렬이 비특이행렬(역행렬 존재)하면,
# x = 0 이라는 자명해(trivial solution) 만 존재하고,
# 고유벡터는 없다.
# 
# (A - LI) 가 특이행렬(역행렬X) 이면,
# x = 0 이외의 비자명해(nontrivial solution) 을 가지게 된다.
# 
# (A - LI) 의 행렬식 deteminant 값이 0 이 되도록 하는 L 값을 계산해서 나오는 값이 고유값이다.
# 

# In[34]:

v, m = sc.linalg.eig(A)
v


# In[35]:

m


# <h5> 3.8 직교행렬과 대칭행렬의 대각화 </h5>
# 
# A 가 **대칭행렬**이면, 
# 
# 고유값은 실수이고, (복소수 아님)
# 
# 각 고유값에 대응되는 고유벡터는 직교(orthogonal) 한다.
# 
# <br/>
# 
# 그래서 모두 다른 n 개 고유값에 대응되는 고유벡터들 
# 
# x<sub>1</sub>,x<sub>2</sub>,...,x<sub>n</sub> 로 구성된 
# 
# 행렬 X = (x<sub>1</sub>,x<sub>2</sub>,...,x<sub>n</sub>) 은 
# 
# **직교행렬(orthogonal matrix)** 이다.
# 
# 따라서 **X 의 전치행렬** = **X 의 역행렬**이다.
# 
# > X'X = XX' = I , X' = X<sup>-1</sup>

# In[36]:

import math
a = 1/math.sqrt(2)
X = np.array([[a,a],[a,-a]]) # 직교행렬 생성


# In[37]:

np.transpose(X) # 전치행렬


# In[38]:

sc.linalg.inv(X) # 역행렬


# 대칭행렬 A 는 직교행렬 X 가 존재(아마도 고유벡터들로 이루어진 직교행렬을 말하는 듯)해서 
# 
# 아래와 같은 형태를 만족하는 행렬이 존재한다.
# 
# > AX = X A_
# 
# > X'AX = X'X A_ = A_
# 
# A_ 는 대각행렬이고, 이런 변화를 **대칭행렬의 대각화 (diagonalization)** 이라고 한다.
# 
# (아마도 대각화의 장점은 연산의 편리성인거 같다.
# 
# A = X'A_X 로 대각화 되었다면,
# 
# A<sup>-1</sup> 은 A_ 대각행렬의 대각원소들을 역수로 바꾸면 되고,
# 
# A<sup>2</sup> 은 A_ 대각행렬의 대각원소들을 제곱한 것과 같다.)

# In[39]:

# 대칭행렬
A = np.array([[2,1],[1,2]])

# 대각행렬을 구해보자. (고유벡터를 사용)
_, X = sc.linalg.eig(A)

# X'AX
sc.dot(sc.dot(np.transpose(X), A), X)


# **직교행렬 속성**
# 
# > 직교행렬의 고유값은 +1, -1 
# 
# > 직교행렬 X 의 전치행렬 X' 와 역행렬 X^-1^ 도 직교행렬이다
# 
# > 직교행렬의 행렬식은 +1 이거나 -1 이다

# <h5> 3.9 멱등행렬 </h5>
# 
# A = A' 와 A = A<sup>2</sup> 를 만족하면 **멱등행렬(idempotent matrix)**
# 
# 0 행렬과 I 행렬이 멱등행렬의 대표적 예이다.
# 
# 계량 경제학에서 가장 많이 사용되는 멱등행렬 M 을 예로 살펴보자.
# 
# > M = I - X(X'X)<sup>-1</sup>X'
# 
# 위 행렬 M 은 대칭행렬이여서 M' = M 전치행렬과 자기자신이 같다.
# 
# 또, M = M<sup>2</sup> 이다.

# **멱등행렬 속성**
# 
# > 멱등행렬 고유값은 1 또는 0 이다
# 
# > A 가 멱등행렬이면, I - A 도 멱등행렬이다.

# <h5> 3.10 이차형태 </h5>
# 
# 행렬 A 와 벡터 a, x 가 있다고 했을때,
# 
# <pre>
# A = [a<sub>11</sub> a<sub>12</sub> ... a<sub>1n</sub>]
#     [a<sub>21</sub> a<sub>22</sub> ... a<sub>2n</sub>]
#     [...    ...   ]
#     [a<sub>n1</sub> a<sub>n2</sub> ... a<sub>nn</sub>]
#     
# a = [a<sub>1</sub>]
#     [a<sub>2</sub>]
#     [..]
#     [a<sub>n</sub>]
#     
# x = [x<sub>1</sub>]
#     [x<sub>2</sub>]
#     [..]
#     [x<sub>n</sub>]
# </pre>
# 
# > L = a'x = a<sub>1</sub>x<sub>1</sub> + a<sub>2</sub>x<sub>2</sub> + ... +  a<sub>n</sub>x<sub>n</sub>
# 
# L 은 x 에 의한 **일차형태(linear form)**이라 하고,
# 
# 대칭행렬 A 와 벡터 x 에 의해 정의된 스칼라 Q
# 
# > Q = x'Ax
# 
# Q 는 x에 대한 **이차형태(quadratic form)**이라 한다.
# 
# 예를 들어,
# 
# <pre>
# A = [a<sub>11</sub> a<sub>12</sub>]  x = [x<sub>1</sub>]
#     [a<sub>21</sub> a<sub>22</sub>]      [x<sub>2</sub>]
# 
# 에 대한 이차형태는 아래와 같다.
#     
# Q = x'Ax = [x<sub>1</sub> x<sub>2</sub>][a<sub>11</sub> a<sub>12</sub>][x<sub>1</sub>] = a<sub>11</sub>x<sub>1</sub><sup>2</sup> + a<sub>12</sub>x<sub>1</sub>x<sub>2</sub> + a<sub>21</sub>x<sub>1</sub>x<sub>2</sub> + a<sub>22</sub>x<sub>2</sub><sup>2</sup>
#                  [a<sub>21</sub> a<sub>22</sub>][x<sub>2</sub>]
# 
# </pre>
# 
# 회귀모형의 모수를 최소제곱법이나 최우법에 의해 추정하는 과정에서 
# 
# 모수벡터에 대해 목적함수를 미분하는 것이 필요하므로
# 
# 일차형태와 이차형태에 대한 편미분에 대하여 간단히 살펴보자. (???)
# 
# 
# 우선 벡터 x 의 각 원소에 의한 일차형태 편미분은 
# 
# dL/dx = a
# 
# dQ/dx = Ax + A'x = (A + A')x 

# <h5> 3.11 확률변수 집합의 공분산행렬 </h5>
# 
# 평균이 0 이고, 분산이 sigma<sup>2</sup> 인,
# 
# 서로 독립인 n개 확률변수(random variables) 집합 x' = [x<sub>1</sub> x<sub>2</sub> ... x<sub>n</sub>] 을 정의하자.
# 
# 이때 확률변의 기댓값이 0 이므로, 
# 
# 공분산행렬(covariance matrix) 는 다음과 같다. 
# 
# C = E[xx']
# 
# 여기서 E[x<sub>i</sub>x<sub>j</sub>] = {sigma<sup>2</sup>  i = j, 0  i != j} 이므로, 공분산행렬은 다음과 같다. 
# 
# <pre>
# C = I sigma<sup>2</sup> =  E [sigma<sup>2</sup> 0 ... 0]
#                   [0  sigma<sup>2</sup> ... 0]
#                   [...         ...]
#                   [0  0 ... sigma<sup>2</sup>]                            
# </pre>
# 
# 물론 확률변수의 공분산이 Cov(x<sub>i</sub>, x<sub>j</sub>) = sigma<sub>ij</sub> 인 일반적인 경우의 공분산행렬은 다음과 같다. 
# 
# <pre>
# (a = sigma)
# 
# C = [a<sub>11</sub> a<sub>12</sub> ... a<sub>1n</sub>]
#     [a<sub>21</sub> a<sub>22</sub> ... a<sub>2n</sub>]
#     [...    ...   ]
#     [a<sub>n1</sub> a<sub>n2</sub> ... a<sub>nn</sub>]
# </pre>
# 
# 공분산행렬은 cov 함수를 사용한다.

# In[40]:

sc.cov(A)


# <h5> 3.12 콜레스키 분해 </h5>
# 
# 행렬 A 가 양의 정부호(positive definite) 대칭행렬이면, (양의 정부호는 deteminant 값을 말하는듯)
# 
# 이 행렬은 U'U 로 나누어진다.
# 
# 여기서 U 는 양의 대각원소를 갖는 위삼각행렬(upper triangle) 이며, 
# 
# 이와같은 분해를 **콜레스키 분해(Cholesky decomposition)** 라고 한다.
# 
# <br/>
# 
# R 은 콜레스키 분해를 계산하는 함수 chol() 을 제공한다. 
# 
# U <- chol(A)
# 
# 입력변수인 A 는 n * n 행렬이며, 출력변수 U 는 A = U'U 를 만족하는 n * n 위삼각행렬이다.

# In[41]:

A


# In[42]:

U = sc.linalg.cholesky(A)
U


# In[43]:

tr_U = np.transpose(U)
tr_U


# In[44]:

sc.dot(tr_U, U)


# <h5> 3.13 QR 분해 </h5>
# 
# 계수가 p 인 n x p 행렬 A 가 존재할때, 
# 
# 행렬 A 는 Q 와 R 의 곱으로 분해될 수 있다. 
# 
# 이때, Q 는 차수가 n x p 인 직교행렬이며, 
# 
# R 은 차수가 p x p 인 위삼각행렬이다. 
# 
# > A = QR
# 

# In[45]:

A = np.array([[1,1,1,1],
              [1,2,2,1],
              [2,3,1,6]])
A


# In[46]:

Q, R = sc.linalg.qr(A)
Q # 직교행렬


# In[47]:

R # 위삼각행렬


# In[48]:

sc.dot(Q, R) # 분해 증명 A = Q*R


# QR 분해는 **최소제곱추정치**를 구할때 유용하다. 
# 
# 즉, A 가 n x p 행렬이고, 계수(rank) 가 p 이면 
# 
# 직교행렬의 특성 Q'Q = I 을 이용해,
# 
# 연립방정식체계 Ax = h 의 해를 아래처럼 구할 수 있다. 
# 
# > Ax = h
# 
# > x = R<sup>-1</sup> Q' h

# In[49]:

A = np.array([[1,2,3],[4,5,6],[7,8,-9]])
h = np.array([[3],[-4],[2]])

# x 구하기 
Q, R = sc.linalg.qr(A)
print sc.linalg.inv(R).dot(np.transpose(Q)).dot(h)

# 하지만 바로 구할 수 있는 solve 를 이용하자.
sc.linalg.solve(A, h)


# <h5> 3.14 특이값 분해 </h5>
# 
# n x p 행렬 A 일때, 
# 
# > A = UDV'
# 
# 이와 같은 분해를 **특이값 분해 (singular value decomposition) 또는 SVD 분해** 라고 한다. 
# 
# U 좌측 특이행렬 n x n 
# V 우측 특이행렬 p x p 
# D 대각행렬, 주 대각선의 값 모두 양의 실수 n x p
# 
# **고유값분해  vs  SVD 분해**
# 
# 고유값분해는 정방행렬만 가능, 
# SVD 분해는 모든행렬을 분해할 수 있다.
# 
# A 행렬이 양의 정부호 대칭행렬일 경우 A 고유값분해 = A 특이값분해 

# In[50]:

# 양의정부호 대칭행렬일때 고유값분해 = SVD분해 인지 확인해보자.

A = np.array([[4,2,-2],[2,10,2],[-2,2,5]]) # 대칭행렬
A


# In[51]:

sc.linalg.det(A) # 양의 정부호


# In[52]:

_, x = sc.linalg.eig(A) # 고유값분해
x


# In[53]:

u, s, v = sc.linalg.svd(A) # SVD 분해 : 열 위치가 다르거나, 방향이 180도 바뀌는 정도는 차이난다.
u


# <h5> 3.15 벡터 및 행렬 노옴 </h5>
# 
# 노움(norm) 이란 일반적으로 벡터나 행렬의 크기(size)나 길이(length)를 말한다.
# 
# 방향은 가지지 않아서 양수값이다. 
# 
# 노옴을 구하는 5가지 방법 
# 
# **1. 열 합의 절대 최대값 (maximum absolute colum sum)** 
# : 열 원소 합의 최대값
# 
# **2. 행 합의 절대 최대값 (maximum absolute row sum)**
# 
# **3. 최대 모듈러스(maximum modulus)**
# : 모든 원소의 최대 모듈러스를 노옴으로 한다.  
# 
# **4. 유클리드 노옴(Euclidean norm) 또는 프로베니우스 노옴(Frobenius norm)**
# : 모든 원소 제곱합의 제곱근을 노옴으로 한다.
# 
# **5. 스펙트럼 노옴(spectral norm) 또는 2-노옴(2-norm)**
# : 특이값(singular value) 중 최대값
# 
# ? 모듈러스 
# 
# 실함수(real function)영역에서 최대 모듈러스 = 절대 최대값 인데 반해,
# 
# 복소함수로 확장되면, 최대 모듈러스 = 최대 절대값 원리
# 
# ex) 복소함수 z = a + bi => 최대 모듈러스 |z| = root(a<sup>2</sup> + b<sup>2</sup>)
# 
# 
# norm(v, type=c("O","I","F","M","2"))
# 
# type 은 순서대로 
# 
# "O" 열합의 최대값, "I" 행합의최대값, "F" 유클리드노옴, "M" 최대모듈러스, "2" 스펙트럼노옴

# In[54]:

A = np.array([[2,2,2],[5,5,6],[0,-1,-2]])
print A

sc.linalg.norm(A)


# In[55]:

sc.linalg.norm(A, 'fro') # 제곱합의 제곱근


# In[56]:

sc.linalg.norm(A, np.inf)  # max(abs(x))


# In[57]:

sc.linalg.norm(A, -np.inf)  # min(abs(x))


# In[58]:

sc.linalg.norm(A, 1)  # max(abs(x)) axis=0, column


# In[59]:

sc.linalg.norm(A, -1)  # min(abs(x)) axis=0, column


# In[60]:

sc.linalg.norm(A, 2)  # 2-norm, largest sing.value


# In[61]:

sc.linalg.norm(A, -2)  # smallest sing.value


# In[ ]:



