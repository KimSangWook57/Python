# 파이썬에서 수치 계산을 위한 핵심 라이브러리입니다. NumPy는 고성능의 다차원 배열 객체와 이러한 배열을 처리할 수 있는 다양한 함수를 제공합니다. 
# NumPy는 선형 대수, 통계, 난수 생성, 푸리에 변환 등과 같은 많은 수치 계산 기능을 포함하며, 
# 다른 과학적 계산용 라이브러리들 (SciPy, pandas, scikit-learn 등)의 기본이 되기도 합니다.
# 다차원 배열 객체(numpy.ndarray)
# 배열 생성 함수(numpy.array(), numpy.zeros(), numpy.ones(), numpy.arange(), numpy.linspace() 등)
# 배열 복사 함수(numpy.copy(), numpy.view() 등)
# 배열 변형 함수(numpy.reshape(), numpy.transpose(), numpy.ravel() 등)
# 배열 연산 함수(numpy.add(), numpy.subtract(), numpy.multiply(), numpy.divide() 등)
# 집계 함수(numpy.sum(), numpy.mean(), numpy.std(), numpy.min(), numpy.max() 등)
# 선형 대수 연산 함수(numpy.dot(), numpy.matmul(), numpy.linalg.inv() 등)
# 난수 생성 함수(numpy.random.rand(), numpy.random.randint(), numpy.random.normal() 등)

# pandas는 파이썬에서 데이터 분석과 조작을 위한 라이브러리입니다. 
# 데이터 불러오기 및 저장: pandas는 CSV, 엑셀, SQL, JSON, HTML 등 다양한 데이터 형식을 지원하여 데이터를 불러오고 저장할 수 있습니다.
# 데이터 정제: pandas를 사용하면 결측치 처리, 중복 제거, 데이터 타입 변환 등 데이터 정제 작업을 수행할 수 있습니다.
# 데이터 조작: 데이터를 필터링, 정렬, 그룹화, 피벗, 병합, 조인 등 다양한 방법으로 조작할 수 있습니다.
# 데이터 분석: pandas는 기술통계, 시계열 분석, 빈도 계산 등 데이터 분석 작업을 수행하는 데 유용한 함수를 제공합니다.

# Series: 1차원 데이터 구조로, 인덱스와 값으로 구성됩니다.
# DataFrame: 2차원 데이터 구조로, 행과 열로 구성됩니다.
# Index: Series나 DataFrame의 인덱스를 나타내는 객체입니다.
# GroupBy: 데이터를 그룹으로 나누어서 통계 정보를 계산합니다.
# merge(): 두 개 이상의 DataFrame을 병합합니다.
# concat(): 여러 개의 DataFrame을 연결합니다.
# read_csv(): CSV 파일을 읽어 DataFrame으로 반환합니다.
# to_csv(): DataFrame을 CSV 파일로 저장합니다.

# import pandas as pd

# # 시리즈(Series) 예시
# data = pd.Series([0.25, 0.5, 0.75, 1.0])
# print(data)

# # 데이터프레임(DataFrame) 예시
# data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'year': [2017, 2017, 2018, 2019],
#         'score': [100, 95, 80, 90]}
# df = pd.DataFrame(data)
# print(df)

# # 데이터프레임에서 열 선택 예시
# print(df['name'])
# print(df.year)

# # 조건을 이용한 데이터 선택 예시
# print(df[df.year > 2017])

# # 데이터프레임에 열 추가 예시
# df['grade'] = ['A', 'A-', 'B+', 'B']
# print(df)

# # 데이터프레임에서 행 선택 예시
# print(df.loc[0])
# print(df.loc[[0, 2]])

# # 데이터프레임에서 행과 열 선택 예시
# print(df.loc[0, 'name'])
# print(df.loc[[0, 2], ['name', 'score']])

# matplotlib는 파이썬에서 그래프와 시각화를 생성하기 위한 라이브러리입니다. 
# matplotlib는 다양한 그래프와 차트를 그릴 수 있는 기능을 제공하며, 
# 데이터 분석 결과를 시각적으로 표현하기 위한 다양한 스타일과 기능을 지원합니다.

# pyplot: 그래프를 그리기 위한 함수들을 제공합니다.
# figure: 그래프 전체를 관리하는 클래스입니다.
# subplot: 여러 개의 서브 플롯을 생성하는 함수입니다.
# plot: 선 그래프를 그리는 함수입니다.
# scatter: 산점도를 그리는 함수입니다.
# bar: 막대 그래프를 그리는 함수입니다.
# hist: 히스토그램을 그리는 함수입니다.
# boxplot: 박스 플롯을 그리는 함수입니다.
# xlabel, ylabel, title: 축 레이블과 그래프 제목을 설정하는 함수입니다.
# legend: 범례를 추가하는 함수입니다.
# xlim, ylim: x축, y축 범위를 설정하는 함수입니다.

import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(-np.pi, np.pi, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

# 그래프 그리기
plt.plot(x, y_sin, label='sin')
plt.plot(x, y_cos, label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sin and Cos Functions')
plt.legend()
plt.show()
