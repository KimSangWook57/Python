# 숫자를 문자열로 변화하는 방법은 str(num)을 이용한다. str(12)는 '12'가 된다. 
# 반대로 문자열을 숫자로 변환하려면 int(string)을 이용한다. int('12')는 12가 된다.
# 이를 이용하여 1부터 1000까지의 숫자의 각 자리수의 합을 모두 구하라. 예를 들어 234는 2+3+4=9가 된다.

sum = 0

num = int(input("더할 자리수 입력 : "))

for i in range(1, num + 1):
    for j in str(i):
        sum += int(j)

print(f"1부터 {num}까지 각 자리수를 더한 값:{sum}")

# 교수님 예제.
# total = 0

# for num in range(1, 1001):
#     # 각 자리수의 합
#     digits_sum = 0
#     for digit in str(num):
#         digits_sum += int(digit)
#     # 전체 합에 더함
#     total += digits_sum

# print(total)