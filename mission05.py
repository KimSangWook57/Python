# 1부터 n까지의 합은 n(n+1)/2로 주어진다.
# 1부터 100까지의 합을 구하여 출력하는 프로그램을 작성하고 실행하라.

num = int(input("정수 입력 : "))
sum = 0

for i in range(1, num + 1):
    sum += i
    
print(f"1부터 {num}까지의 합 = {sum}")