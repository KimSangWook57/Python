import matplotlib.pyplot as plt
import numpy as np

# 그래프 스타일링
# 외부 스타일 리스트
styles = ['bmh', 'classic', 'dark_background', 'fivethirtyeight', 'ggplot', 'grayscale', 'Solarize_Light2', 'tableau-colorblind10']

# 스타일 적용 예제
for style in styles:
    plt.style.use(style)
    x = np.arange(0, 10, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, label='Sine')
    plt.plot(x, y2, label='Cosine')
    plt.title('Sine and Cosine Waves')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
