import matplotlib.pyplot as plt
import numpy as np

# 색상 변경 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, color='blue')
plt.plot(x, y2, color='#FF5733')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 'b': 파란색 (blue)
# 'g': 초록색 (green)
# 'r': 빨간색 (red)
# 'c': 청록색 (cyan)
# 'm': 자홍색 (magenta)
# 'y': 노란색 (yellow)
# 'k': 검정색 (black)
# 'w': 흰색 (white)
