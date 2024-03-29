import matplotlib.pyplot as plt
import numpy as np

# 마커 변경 예제
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, marker='^')
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# '.' : 작은 점 (point)
# ',' : 픽셀 (pixel)
# 'o' : 원 (circle)
# 'v' : 역삼각형 (triangle_down)
# '^' : 삼각형 (triangle_up)
# '<' : 왼쪽 화살표 (triangle_left)
# '>' : 오른쪽 화살표 (triangle_right)
# '1' : 아래쪽으로 뾰족한 별 (tri_down)
# '2' : 위쪽으로 뾰족한 별 (tri_up)
# '3' : 왼쪽으로 뾰족한 별 (tri_left)
# '4' : 오른쪽으로 뾰족한 별 (tri_right)
# 's' : 네모 (square)
# 'p' : 오각형 (pentagon)
# '*' : 별표 (star)
# 'h' : 육각형1 (hexagon1)
# 'H' : 육각형2 (hexagon2)
# '+' : 플러스 (plus)
# 'x' : 엑스 (x)
# 'D' : 다이아몬드 (diamond)
# 'd' : 작은 다이아몬드 (thin_diamond)
# '|' : 수직선 (vline)
# '_' : 수평선 (hline)
