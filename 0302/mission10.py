# 플레이어가 처음에 $50을 가지고 있다. 
# 동전을 한 번 던져서 앞면(1) 또는 뒷면(2)이 나온다. 
# 맞추면 $9을 따고 틀리면 $10을 잃는다. 플레이어가 돈을 모두 잃거나 $100이 되면 게임이 종료된다.
# 동전을 던져서 나오는 수는 다음 문장을 이용하라.

from random import *

stake = 50
cnt = 0

print("동전을 던져서, 판돈이 100$가 되거나 0$가 될때까지 반복합니다.")
print(f"시작 판돈은 {stake}$입니다.")
print("게임을 시작하겠습니다.")


while 0 < stake < 100:
    cnt += 1
    print("동전을 튕깁니다...")
    coin = randint(1, 2)
    # 동전 결과 확인
    print(f"coin = {coin}")
    guess = int(input("앞면(1) or 뒷면(2)? : "))
    if not ((guess == 1) or (guess == 2)):
        print("잘못된 입력입니다. 다시 동전을 튕기겠습니다.")
        continue
    if coin == guess:
        print("정답입니다!")
        stake += 9
        print(f"현재 판돈 : {stake}$")
    else:
        print("틀렸습니다!")
        stake -= 10
        print(f"현재 판돈 : {stake}$")

if stake > 100:
    print("승리!")
    print(f"시도 횟수 : {cnt}")

if stake < 0:
    print("패배!")
    print(f"시도 횟수 : {cnt}")