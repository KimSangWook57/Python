# 가변 인자
# 파이썬에서는 가변 인자(*args, **kwargs)를 쉽게 처리할 수 있습니다. 이를 통해 함수가 받는 인자의 개수를 동적으로 조절할 수 있습니다.

# *args를 이용한 가변 인자 처리
# *args는 위치 인자(positional argument)를 가변적으로 처리하기 위한 구문입니다.
# *args는 함수의 인자 리스트에서 가변 인자를 나타내며, 함수 내부에서는 튜플(tuple) 형태로 처리됩니다.

def sum_numbers(*args):
    result = 0
    for arg in args:
        result += arg
    return result

# 가변 인자를 사용하여 함수 호출
result1 = sum_numbers(1, 2, 3, 4, 5)   # 15
result2 = sum_numbers(1, 2, 3)         # 6
result3 = sum_numbers(1, 2)            # 3


# **kwargs를 이용한 가변 인자 처리
# **kwargs는 키워드 인자(keyword argument)를 가변적으로 처리하기 위한 구문입니다.
# **kwargs는 함수의 인자 리스트에서 가변 키워드 인자를 나타내며, 함수 내부에서는 딕셔너리(dictionary) 형태로 처리됩니다.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 가변 키워드 인자를 사용하여 함수 호출
print_info(name='Alice', age=25, country='USA')
# 출력 결과: 
# name: Alice
# age: 25
# country: USA

# LEGB

# L (Local) : 함수 내부의 지역 변수입니다.
# E (Enclosing) : 함수를 포함하는 다른 함수(중첩 함수) 내부의 변수입니다.
# G (Global) : 전역 변수입니다.
# B (Built-in) : 내장 함수나 모듈 등 파이썬이 기본적으로 제공하는 것들입니다.

# 함수 내부에서 변수를 참조할 때, 먼저 로컬 변수를 찾고, 
# 없으면 상위 함수에서 변수를 찾습니다. 
# 상위 함수에서도 찾지 못하면 전역 변수를 찾고, 
# 마지막으로 내장 함수나 모듈에서 변수를 찾습니다.
x = 'global'

def outer():
    x = 'outer'
    
    def inner():
        x = 'inner'
        print('x in inner:', x)
    
    inner()
    print('x in outer:', x)

outer()
print('x in global:', x)
