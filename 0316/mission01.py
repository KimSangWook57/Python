# enumerate() 내장 함수를 이용하여 사용자가 입력한 문자열에서 'a' 문자의 위치를 모두 찾아 출력하는 프로그램을 작성하라. 
# 'a'가 없으면 "a가 없습니다'라는 메시지를 출력하라.
letters = input("영단어 입력 : ")

flag = 0

for idx, char in enumerate(letters):
    if char == 'a':
        print(idx)
        flag = 1

if flag == 0:
    print("no 'a' in letters")





