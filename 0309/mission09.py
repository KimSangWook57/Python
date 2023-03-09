from math import *

# 두 개의 매개변수 n, m을 전달받아 m x n개의 * 상자를 출력하는 프로그램을 함수로 작성. 
# 예: 2, 4  
# ****              
# ****
def box(row, col):
    for i in range(row):
        for j in range(col):
            print("*", end="")
        print("")
# 결과 출력.
box(2, 4)

print("==========================")
# 하나의 숫자를 전달받아 숫자의 자리 합을 구하는 함수를 작성. 예: 123  1+2+3 = 6

def sumsum(n):
    total = 0
    for i in range(1, n + 1):
        for j in str(i):
            total += int(j)
    return total

print(sumsum(1000)) # 출력결과: 13501

print("==========================")
# 두 개의 문자열이 서로 다른 처음 위치를 반환하는 함수를 작성. 두 개의 문자열이 같으면 -1을 반환
def isNotEqual(str1, str2):
    flag = 0
    length = min(len(str1), len(str2))
    for i in range(length):
        if str1[i] != str2[i]:
            if i != 0:
                return i + 1
    return -1

print(f"두 단어가 달라지는 순간의 단어 위치 :", isNotEqual("apple", "application"), "번째") # 출력결과: 5번째

print("==========================")
# 문자열과 하나의 문자를 전달받아 문자열에서 문자의 위치를 모두 찾아 리스트로 반환하는 함수를 작성
def char_count(str, char):
    temp = []
    for i in range(len(str)):
        if str[i] == char:
            temp.append(i)
    return temp

print(char_count("banana", "a")) # 출력결과: [1, 3, 5]

print("==========================")
# 재귀 함수를 이용하여 1부터 100까지의 합을 계산하는 프로그램
def sum_(n):

    if n == 1:
        return 1
    else:
        return n + sum_(n - 1)

print(sum_(100))  # 출력결과: 120
