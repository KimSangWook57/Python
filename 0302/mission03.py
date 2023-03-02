# 사용자로부터 이수한 학점을 입력 받는다. 
# 학점이 40학점 미만이면 "1학년입니다"를 출력하고, 
# 40이상 80미만이면 "2학년입니다"를 출력하고. 
# 학점이 80이상이면 "졸업반입니다"를 출력하는 프로그램을 작성하라.

value = int(input("이수학점 입력(0 이상)"))

if value < 0:
    print("잘못된 입력값입니다.")
elif 0 <= value < 40:
    print("1학년입니다.")
elif 40 <= value < 80:
    print("2학년입니다.")
else:
    print("졸업반입니다.")