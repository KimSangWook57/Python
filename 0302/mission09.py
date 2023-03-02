# 두 주사위를 던졌을 때, 합이 7이 되면 이김, 그렇지 않으면 지는 간단한 주사위 게임을 만들어보세요.
# 이길 때까지 반복합니다.
import random

print("주사위 게임에 오신 것을 환영합니다!")
print("주사위 2개를 던져, 7이 나오면 승리합니다!")
# 시도 횟수 카운트 추가.
cnt = 1

while True:
    
    print("첫번째 주사위를 던집니다...")
    dice1 = random.randint(1, 6)
    print(f"첫번째 주사위의 눈:{dice1}")
    print("두번째 주사위를 던집니다...")
    dice2 = random.randint(1, 6)
    print(f"두번째 주사위의 눈:{dice2}")
    result = dice1 + dice2
    if result == 7:
        print("승리!")
        print(f"시도 횟수 : {cnt}")
        break
    else:
        print("패배!")
        print("게임을 재시작합니다.")
        cnt += 1