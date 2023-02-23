# 추가문제
end = ("-" * 50)
# 초를 입력하면 분과 초로 표시하는 프로그램.
# 예를 들어, 200초를 입력하면 3분 20초로 표현하라

sec = int(input("초 입력 : "))
min1 = sec // 60
sec1 = sec % 60 
print(f"{min1}분 {sec1}초")
print(end)

# 분(min)을 입력 하면, 일, 시간, 분으로 출력하는 프로그램을 만들어라.
# (예 : 1550분은 1일 1시간 50분)

min = int(input("분 입력 : "))
hour = min // 60
day1 = hour // 24
hour1 = hour % 24
min2 = min % 60
print(f"{day1}일 {hour1}시간 {min2}분")
print(end)






