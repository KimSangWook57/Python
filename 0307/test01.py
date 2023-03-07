# 문자열 인덱싱 예제 1
s = "Hello, World!"
print(s[0])   # 'H'
print(s[1])   # 'e'
print(s[-1])  # '!'

# 문자열 인덱싱 예제 2
s = "Python is a fun programming language!"
print(s[7])  # 'i'
print(s[11]) # 'f'
print(s[-12]) # 'm'

# 문자열 인덱싱 예제 3
s = "ABCDEFG"
print(s[1:4]) # 'BCD'
print(s[:3])  # 'ABC'
print(s[3:])  # 'DEFG'

# 문자열 슬라이싱
# string[start:end:step]
# defalut[0:str(len):1]

# 문자열에서 홀수 번째 문자 추출하기
string = "abcdefghij"

result = ""
for i in range(len(string)):
    if i % 2 == 0:
        result += string[i]

print(result)  # 출력값: "acegi"

# 문자열 뒤집기 예시.
s = "Hello, world!"
reversed_s = s[::-1]
print(reversed_s)  # "!dlrow ,olleH"

# 문자열 구성 파악 메소드 예시
print("hello123".isalnum())  # True
print("123".isalpha())  # False
print("123".isdecimal())  # True
print("123".isdigit())  # True
print("hello".isidentifier())  # True
print("hello".islower())  # True
print("123".isnumeric())  # True
print("Hello, World!".isprintable())  # True
print("   ".isspace())  # True
print("\t".isspace())  # True
print("Hello, World!".istitle())  # True
print("HELLO".isupper())  # True

# 문자열 대소문자 변환 함수 예시
print("hello, world!".upper())  # "HELLO, WORLD!"
print("HeLLo, wOrLd!".lower())  # "hello, world!"
print("hello, world!".capitalize())  # "Hello, world!"
print("hello, world!".title())  # "Hello, World!"
print("Hello, World!".swapcase())  # "hELLO, wORLD!"

# 문자열 찾기 함수 예시
s = "hello, world!"

print(s.find("o"))  # 4
print(s.rfind("o"))  # 8
print(s.index("o"))  # 4
print(s.rindex("o"))  # 8
print(s.count("o"))  # 2

# 문자열 공백 삭제 및 변경 함수 예시
s = "  hello,   world!  "

print(s.strip())  # "hello,   world!"
print(s.lstrip())  # "hello,   world!  "
print(s.rstrip())  # "  hello,   world!"
print(s.replace("o", "0"))  # "  hell0,   w0rld!  "
print(s.replace("o", "0", 1))  # "  hell0,   world!  "

# split()은 문자열을 지정된 구분자(sep)로 나누어 리스트로 반환합니다. 
# sep 인자를 생략하면 공백을 구분자로 사용합니다. 
# maxsplit 인자를 사용하여 나눌 횟수를 지정할 수 있습니다.
string = "hello world"
string_list = string.split()  # 기본값인 공백을 구분자로 사용
print(string_list)  # ['hello', 'world']

string = "apple,banana,grape"
string_list = string.split(",")  # 쉼표를 구분자로 사용
print(string_list)  # ['apple', 'banana', 'grape']

# splitlines()는 문자열을 개행 문자 또는 캐리지 리턴 문자 등을 기준으로 분리하여 리스트로 반환합니다.
# join()은 문자열을 반복 가능한 객체의 요소들을 구분자로 연결하여 반환합니다.
# 문자열 분리, 결합 함수 예시
s = "apple,banana,grape"

print("apple\nbanana\rgrape".splitlines())  # ["apple", "banana", "grape"]
print(",".join(["apple", "banana", "grape"]))  # "apple,banana,grape"

# 문자열 정렬, 채우기 함수 예시
s = "hello"

print(s.center(10))  # "  hello   "
print(s.center(10, "-"))  # "--hello---"
print(s.ljust(10))  # "hello     "
print(s.ljust(10, "*"))  # "hello*****"
print(s.rjust(10))  # "     hello"
print(s.rjust(10, "+"))  # "+++++hello"
print("123".zfill(5))  # "00123"
