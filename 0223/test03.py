# 멤버쉽 연산자 사용 예제
a = [1, 2, 3, 4, 5]
b = "Hello, World!"
print(3 in a)  # True 출력
print(6 in a)  # False 출력
print("o" in b)  # True 출력
print("k" not in b)  # True 출력
print("-" * 50)

# 문자열 출력 예제
print("Hello, world!")  # "Hello, world!" 출력
print("My name is John.")  # "My name is John." 출력
print('The "quick brown" fox jumps over the lazy dog.')  # 'The "quick brown" fox jumps over the lazy dog.' 출력
print("I'm a boy.")  # "I'm a boy." 출력
print("He said, \"Hello!\"")  # "He said, "Hello!"" 출력
print("10"+"20") #문자열 잇기  1020
print("abc " * 3) #문자열 3번 출력  abc abc abc

# 변수 출력 예제
x = 10
y = 5
z = x + y
print(x, y, z)  # 10 5 15 출력

print(10+20)  # 30
print("-" * 50)

# 딕셔너리 출력 예제
person = {"name": "John", "age": 25, "city": "New York"}
print(person)  # {'name': 'John', 'age': 25, 'city': 'New York'} 출력

# 딕셔너리 값 출력 예제
print(person["name"])  # 'John' 출력
print(person["age"])  # 25 출력
print(person["city"])  # 'New York' 출력

endline = ("=" * 50)
print(endline)

# % 연산자.
# 문자열
name = "John"
print("Hello, %s!" % name)

# 정수
num = 42
print("The answer is %d." % num)

# 실수
pi = 3.14159
print("Pi is approximately %.2f." % pi)

# 여러 개의 변수
first_name = "Jane"
last_name = "Doe"
age = 25
print("My name is %s %s and I am %d years old." % (first_name, last_name, age))

# 진수 변환
decimal_num = 42
binary_num = bin(decimal_num)
print("The decimal number %d is equal to the binary number %s." % (decimal_num, binary_num))
print(endline)

# format 연산자.
# 문자열
name = "John"
print("Hello, {}!".format(name))

# 정수
num = 42
print("The answer is {}.".format(num))

# 실수
pi = 3.14159
print("Pi is approximately {:.2f}.".format(pi))

# 여러 개의 변수
first_name = "Jane"
last_name = "Doe"
age = 25
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))

# 인덱스를 이용한 대입
first_name = "Jane"
last_name = "Doe"
age = 25
print("My name is {1} {0} and I am {2} years old.".format(last_name, first_name, age))

print(endline)

# f-string 포메팅(최신)
# f-string에서 다양한 서식 지정자를 이용하는 예제
name = "John"
age = 30
height = 175.5
# f-string 포메팅 방법을 위해, 문자열 앞에 f를 넣어 준다.
print(f"My name is {name}, I'm {age:d} years old, and my height is {height:.2f} cm.")
# 출력 결과: "My name is John, I'm 30 years old, and my height is 175.50 cm."

pi = 3.14159265

print(f"The value of pi is approximately {pi:.2f}.")
# 출력 결과: "The value of pi is approximately 3.14."

x = 12345

print(f"The value of x is {x:10d}.")
# 출력 결과: "The value of x is      12345."

y = 12.345

print(f"The value of y is {y:10.2f}.")
# 출력 결과: "The value of y is     12.35."

z = 3

print(f"The value of z is {z:+5d}.")
# 출력 결과: "The value of z is    +3."

w = 12345

print(f"The value of w is {w:0>10d}.")
# 출력 결과: "The value of w is 0000012345."

text = "Hello, World!"

print(f"{text:^20}")
# 출력 결과: "   Hello, World!    "


