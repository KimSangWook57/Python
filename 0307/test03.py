# 튜플은 생성 시 값의 추가, 삭제, 수정이 불가 => 불변성 유지 및 값 수정 방지.(키값)

# 빈 튜플 생성
t1 = ()
print(t1)  # ()

# 요소가 하나인 튜플은 요소 뒤에 콤마(,)를 붙여서 생성
t2 = (1,)
print(t2)  # (1,)

# 여러 요소를 가진 튜플 생성
t3 = (1, 2, 3)
print(t3)  # (1, 2, 3)

# 리스트나 문자열을 튜플로 변환
t4 = tuple([1, 2, 3])
print(t4)  # (1, 2, 3)

t5 = tuple("hello")
print(t5)  # ('h', 'e', 'l', 'l', 'o')

# 소괄호 없이도 생성 가능
t = 1, 2, 3
print(t)  # (1, 2, 3)

# 튜플 언패킹(tuple unpacking)은 튜플의 각 요소를 개별 변수로 할당하는 것을 말합니다.
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # 1
print(b)  # 2
print(c)  # 3

# 튜플과 리스트는 각각 서로 다른 데이터 타입이지만, 서로 변환할 수 있습니다.
# 주의점은 리스트 안에 요소가 변경 가능한 객체인 경우, 튜플로 변환하더라도 요소 값이 변경될 수 있다는 점입니다. 
# 예를 들어, 다음과 같은 리스트를 튜플로 변환하면 튜플의 요소 값이 변경될 수 있습니다.
my_list = [1, 2, [3, 4]]
my_tuple = tuple(my_list)
print(my_tuple) # 출력 결과: (1, 2, [3, 4])

my_tuple[2][0] = 5
print(my_tuple) # 출력 결과: (1, 2, [5, 4])

# 튜플을 이용한 함수에서는 여러 값을 동시에 반환할 수 있으며, 함수의 매개변수로서 튜플을 사용하여 함수에 여러 인수를 전달할 수 있습니다.
def calculate(x, y):
    add = x + y
    subtract = x - y
    multiply = x * y
    divide = x / y
    return add, subtract, multiply, divide

result = calculate(10, 2)  
print(result)   #  결과: (12, 8, 20, 5.0)
