# 다양한 그래프 유형

# 막대 그래프 (Bar plot)
# 막대 그래프는 범주형 데이터를 시각화하는 데 자주 사용됩니다. x축에는 범주형 변수, y축에는 연속형 변수를 사용하여 표시합니다.

import matplotlib.pyplot as plt
import numpy as np

labels = ['apple', 'banana', 'orange', 'grape', 'kiwi']
values = [20, 10, 15, 25, 30]

plt.bar(labels, values)
plt.show()

# 히스토그램 (Histogram)
# 히스토그램은 데이터의 분포를 나타내는 데 자주 사용됩니다. 데이터를 구간으로 나누고, 각 구간에 속하는 데이터의 개수를 세어서 표시합니다.

data = np.random.normal(0, 1, 1000)

plt.hist(data)
plt.show()

# 히트맵 (Heatmap)
# 히트맵은 데이터의 상관 관계를 나타내는 데 자주 사용됩니다. 색상을 사용하여 데이터 값의 크기를 나타냅니다.

data = np.random.rand(10, 10)

plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.show()

# imshow(): 2차원 배열을 이미지로 변환하여 표시
# cmap: 매개변수를 사용하여 색상 맵을 지정
# colorbar(): 색상 막대기를 추가

# 등고선 그래프 (Contour plot)
# 등고선 그래프는 2차원 함수의 등고선을 나타내는 데 자주 사용됩니다.
def f(x, y):
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2*np.pi, 100)
y = np.linspace(0, 2*np.pi, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contour(X, Y, Z)
plt.show()
