# 가변 인자와 기본값 인자 사용 예시
# 숫자 개수는 가변, 숫자 사이의 콤마는 기본값.
def print_numbers(*args, sep=", "):
    print(sep.join(map(str, args)))

# 가변 인자를 사용하여 함수 호출
print_numbers(1, 2, 3)               # 출력 결과: 1, 2, 3
print_numbers(1, 2, 3, sep=" - ")    # 출력 결과: 1 - 2 - 3

# 기본값 인자를 사용하여 함수 호출
def say_hello(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

say_hello("Alice")                  # 출력 결과: Hello, Alice!
say_hello("Bob", "Hi")              # 출력 결과: Hi, Bob!

# 인자의 순서와 조합 사용 예시
def print_numbers(a, b, *args, c=10, d=20):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")
    print(f"args: {args}")

# 함수 호출
print_numbers(1, 2, 3, 4, 5, c=30, d=40)

# 출력 결과: a: 1, b: 2, c: 30, d: 40, args: (3, 4, 5)
# 가변 인자인 3, 4, 5는 args가 뒤에서 print 되고 있으므로, 뒤로 밀렸다.

# 인자의 순서는 다음과 같은 규칙을 따릅니다.
# 위치 인자는 먼저 전달되어야 합니다.
# 가변 인자는 위치 인자 다음에 전달됩니다.
# 키워드 인자는 가변 인자나 위치 인자 뒤에 전달됩니다.
# 기본값 인자는 맨 마지막에 전달됩니다.

# 위 순서를 지키면 함수를 호출할 때 인자를 정확하게 전달할 수 있습니다. 
# 특히 키워드 인자를 사용할 때는 기본값 인자와 함께 사용하는 경우가 많은데, 
# 이 때는 기본값 인자를 뒤쪽에 위치시켜야 합니다. 
# 그렇지 않으면 구문 오류(SyntaxError)가 발생합니다.




