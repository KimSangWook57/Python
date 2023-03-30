import matplotlib.pyplot as plt
import numpy as np

# 여러 개의 그래프 하나의 그림 창에 그리는 방법 = 서브플롯
# 2x2 서브플롯 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 2x2 서브플롯 생성
fig, axs = plt.subplots(2, 2, figsize=(8, 8))

# 첫 번째 서브플롯 (왼족 위)
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sine')

# 두 번째 서브플롯 (오른쪽 위)
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosine')

# 세 번째 서브플롯 (왼쪽 아래)
axs[1, 0].plot(x, y1 + y2)
axs[1, 0].set_title('Sine + Cosine')

# 네 번째 서브플롯 (오른쪽 아래)
axs[1, 1].plot(x, y1 - y2)
axs[1, 1].set_title('Sine - Cosine')

plt.show()

# 다른 예시
# 정해진 위치에 바로 그래프를 넣는 방법.
# 2행 2열로 쪼개고 1번(왼쪽 위)에 넣어라.
plt.subplot(2, 2, 1)

plt.plot(x, y1)
plt.title('Sine')
# 2행 2열로 쪼개고 3번(왼쪽 아래)에 넣어라.
plt.subplot(2, 2, 3)

plt.plot(x, y2)
plt.title('Cosine')
# 4행 4열로 쪼개고 9번에 넣어라.
# plt.subplot(4, 4, 9)

# plt.plot(x, y2)
# plt.title('Cosine')
# 1행 2열로 쪼개고 2번(오른쪽)에 넣어라.
plt.subplot(1, 2, 2)

plt.plot(x, y1 + y2)
plt.title('Sine + Cosine')


plt.show()