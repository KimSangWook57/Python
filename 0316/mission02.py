# 두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 각각 정의하라. 딕셔너리를 이용하여 
# 사용자가 '1'을 입력하면 sum()을 호출하고, '2'를 입력하면 sub(), '3'을 입력하면 mul(), '4'를 입력하면 div() 함수를 호출하여 
# 두 수의 연산을 수행하는 프로그램을 작성하라.
def add(n, m):
    return n + m

def sub(n, m):
    return n - m

def mul(n, m):
    return n * m

def div(n, m):
    return n / m

table = {'1':add, '2':sub, '3':mul, '4':div}


key = input("계산기 실행(1 = 덧셈, 2 = 뺄셈, 3 = 곱셈, 4 = 나눗셈) : ")
num1 = int(input("첫번째 숫자 입력 : "))
num2 = int(input("두번째 숫자 입력 : "))


if key in table:
    if key == '1':
        print("덧셈 결과 : ", add(num1, num2))
    elif key == '2':
        print("뺄셈 결과 : ", sub(num1, num2))
    elif key == '3':
        print("곱셈 결과 : ", mul(num1, num2))
    elif key == '4':
        print("나눗셈 결과 : ", round(div(num1, num2), 2))
    else:
        print("잘못된 키 입력")
