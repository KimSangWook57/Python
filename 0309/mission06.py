# 주어진 문자열에서 각 알파벳의 빈도수를 구하는 프로그램을 작성하시오.

text = "Hello, world!"

dict = {}
# dict에 text의 글자들을 쪼개서 넣었음.
for char in text:
    # 단어가 딕셔너리에 없다면...
    if char not in dict:
        # 딕셔너리의 단어 카운트는 1.
        dict[char] = 1
    else:
        # 값이 있다면 카운트 값을 1 증가.
        dict[char] += 1

print(dict)



