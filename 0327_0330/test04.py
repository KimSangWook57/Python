import matplotlib.pyplot as plt
import numpy as np

# 라인 스타일 변경 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, linestyle='dashed')
plt.plot(x, y2, linestyle='dashdot')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 'solid': 실선
# 'dashed': 파선
# 'dashdot': 점선과 파선 번갈아가며
# 'dotted': 점선
