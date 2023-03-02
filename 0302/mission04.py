# 사용자로부터 현재 시간을 나타내는 1~12의 숫자를 입력 받는다.
# 또 "am" 혹은 "pm"을 입력 받고 경과 시간을 나타내는 값을 입력 받는다.
# 이로부터 최종 시간이 몇 시인지 출력하는 프로그램을 작성하라.

hour1 = int(input("시간 입력 (1~12) : "))
ampm = int(input("오전이면 1, 오후면 2를 입력하시오 : "))
hour2 = int(input("몇 시간이 지났습니까? : "))

if ampm == 2:
    hour1 += 12

totalHour = hour1 + hour2
totalTime = totalHour % 24

if 0 <= totalTime <= 12:
    print(f"{hour2}시간이 흐른 후 시간: 오전{totalTime}시")
else:
    print(f"{hour2}시간이 흐른 후 시간: 오후{totalTime % 12}시")

