# 판매자가 딸기와 포도를 판매하고 있다.
# 포도 한 알의 무게는 75g이고 딸기 한 알의 무게는 113.5g이다.
# 사용자로부터 포도 알의 개수와 딸기의 개수를 입력 받아
# 총 무게를 계산하여 출력하는 프로그램을 작성하고 실행하라.
s_weight = 113.5
g_weight = 75

s_num = int(input("딸기 개수 : "))
g_num = int(input("포도 개수 : "))

totalWeight = s_num * s_weight + g_num * g_weight
print(f"과일들의 총 무게 : {totalWeight}g")

