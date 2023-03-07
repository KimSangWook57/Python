# 사용자가 입력한 문자열에 대해 다음 물음에 답하라.

s = input("영어 문자열 입력 : ")
endline = ("="* 30)
# 01. 문자열의 문자수를 출력하라
s_len = len(s)
print(s_len)
print(endline)
# 02. 문자열을 10번 반복한 문자열을 출력하라
s_repeat = s * 10
print(s_repeat)
print(endline)
# 03. 문자열의 첫 번째 문자를 출력하라
s_first = s[0]
print(s_first)
print(endline)
# 04. 문자열에서 처음 3문자를 출력하라
s_first3 = s[:3]
print(s_first3)
print(endline)
# 05. 문자열에서 마지막 3문자를 출력하라
s_last3 = s[-3:]
print(s_last3)
print(endline)
# 06. 문자열의 문자를 거꾸로 출력하라
s_reverse = s[::-1]
print(s_reverse)
print(endline)
# 07. 문자열에 7번째 문자가 있으면 출력하고 없으면 '문자가 없습니다'라는 메시지를 출력하라
# 인덱스 범위를 먼저 지정해 준다.
if len(s) >= 7:
    print(s[6])
else:
    print("문자가 없습니다.") 
print(endline)
# 08. 문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열을 출력하라
# 첫 범위를 1로, 마지막 범위를 -1로(마지막 문자를 빼도록) 설정.
result = s[1:-1]
# result = ""
# for i in range(len(s)):
#     if i == 0 or i == len(s) - 1:
#         pass
#     else:
#         result += s[i]

print(result)
print(endline)
# 09. 문자를 모두 대문자로 변경하여 출력하라
s_upper = s.upper()
print(s_upper)
print(endline)
# 10. 문자를 모두 소문자로 변경하여 출력하라
s_lower = s.lower()
print(s_lower)
print(endline)
# 11. 문자열에서 'a'를 'e'로 대체하여 출력하라
s_replace = s.replace("a", "e")
print(s_replace)
print(endline)