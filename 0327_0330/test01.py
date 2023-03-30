# Matplotlib이란?
# Matplotlib은 파이썬에서 데이터 시각화를 위한 가장 일반적인 라이브러리입니다.
# 다양한 유형의 그래프를 그리는 데 사용할 수 있습니다.
# Matplotlib은 파이썬의 기본 라이브러리인 NumPy와 함께 사용됩니다.

import matplotlib.pyplot as plt
import numpy as np

# x, y 데이터 생성
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# 선 그래프 그리기
plt.plot(x, y)

# 선 그래프 스타일 변경
plt.plot(x, y, color='red', linestyle='--', linewidth=2, marker='o', markersize=5)

# color: 그래프 색상
# linestyle: 선 스타일 (solid, dashed, dotted, dashdot 등)
# linewidth: 선 굵기
# marker: 마커 스타일 (circle, square, triangle 등)
# markersize: 마커 크기

# 그래프 타이틀과 축 라벨 설정
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('y')

# 그래프 출력
plt.show()


