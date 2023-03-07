# 문자 'a'가 들어가는 단어를 키보드에서 입력 받아 
# 첫 번째 줄에는 'a'까지의 문자열을 출력하고 
# 두 번째 줄에는 나머지 문자열을 출력하는 프로그램을 작성하라.
# Your word: Buffalo
#Buffa
#lo

s = input("영어 단어 입력 : ")
# s = "Buffalo"
target_s = s.find("a")
# print(target_s)

# a가 있으면 나눠서 출력, 없으면 그대로 출력.
if target_s != -1:
    front = s[:target_s + 1]
    back = s[target_s + 1:]
    print(f"Your word : {s}")
    print(f"front : {front}")
    print(f"back : {back}")
else:
    print(f"Your word : {s}")
    print("not found 'a'")

# a가 여러개라면?
# 개행문자 \n으로 나누는 방법.
# result = s.replace('a', 'a\n')
# print(f"Your word : {s}")
# print(result)
