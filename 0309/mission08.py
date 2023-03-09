from math import *

# 1~n까지의 합을 계산하는 함수
def sum_(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total
# 100까지의 합
print(sum_(100))

print("============================")
# 반지름을 전달하면 원의 면적을 반환하는 cir_area(r) 함수와 원의 둘레를 반환하는 cir_cirm(r) 함수를 작성하라. 
# 이들 함수를 이용하여 반지름이 3.5cm인 원의 면적과 둘레를 소수점 아래 첫 자리까지 구하라.
# 원의 면적
def cir_area(r):
    return pi * r * r
# 원의 둘레
def cir_cirm(r):
    return pi * r * 2

print(round(cir_area(3.5), 1))
print(round(cir_cirm(3.5), 1))

print("============================")
# den(n) 함수를 이용하여 약수를 구하여 반환하는 프로그램을 작성
# 12 => [1, 2, 3, 4, 6, 12]

def den(n):
    temp = []
    for i in range(1, n + 1):
        if n % i == 0:
            temp.append(i)
    return temp

print(den(32))

print("============================")