# 사용자로부터 5개의 숫자를 문자열로 입력 받아 각 숫자를 +로 연결한 문자열을 생성하라. 
# 예를 들어 2, 5, 11, 33, 55를 입력하면 '2+5+11+33+55'를 생성하라.

# str = ""
# length = 5

# for i in range(1, length + 1):
#     n = input(f"{i}번째 숫자 입력 : ")
#     if (i != length):
#         str += n + "+"
#     else:
#         str += n

# print(str)

# 교수님 예제.

num_list = input("5개의 숫자 입력(띄어쓰기로 구분해줄 것) :").split()
result = "+".join(num_list)
print(result)