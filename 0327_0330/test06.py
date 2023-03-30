import matplotlib.pyplot as plt
import numpy as np

# 범례 추가
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, linestyle='dashed', label='Sine')
plt.plot(x, y2, linestyle='dashdot', label='Cosine')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best', fontsize=12, shadow=True, title='Legend') # 범주 추가 코드
plt.show()

# 'best': 자동으로 최적의 위치를 선택합니다.
# 'upper right': 오른쪽 상단에 위치합니다.
# 'upper left': 왼쪽 상단에 위치합니다.
# 'lower right': 오른쪽 하단에 위치합니다.
# 'lower left': 왼쪽 하단에 위치합니다.
# 'right': 오른쪽에 위치합니다.
# 'center left': 중앙 왼쪽에 위치합니다.
# 'center right': 중앙 오른쪽에 위치합니다.
# 'lower center': 하단 중앙에 위치합니다.
# 'upper center': 상단 중앙에 위치합니다.
# 'center': 중앙에 위치합니다.
