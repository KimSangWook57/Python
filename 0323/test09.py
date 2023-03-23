# 패턴 옵션
# 정규표현식에서 사용되는 패턴 옵션은 대소문자 무시, 다중행 모드 등이 있습니다.

# re.IGNORECASE 또는 re.I 옵션
# re.IGNORECASE 옵션은 대소문자를 무시합니다. 예를 들어, re.findall(r"a", "AbCdAaA", re.IGNORECASE)는 ['A', 'a', 'A', 'a', 'A']와 같은 리스트를 반환합니다.
# re.MULTILINE 또는 re.M 옵션
# re.MULTILINE 옵션은 다중행 모드를 사용합니다. 예를 들어, "abc\ndef\nghi"라는 문자열에서 r"^g"를 검색할 때, re.MULTILINE 옵션이 적용되면 "g"와 매칭됩니다.


# re.IGNORECASE
import re

string = "Python is an interpreted language"

pattern = 'python'
result = re.findall(pattern, string)
print(result)  # []

result = re.findall(pattern, string, re.IGNORECASE)
print(result)  # ['Python']

# re.MULTILINE
string = """Python is an interpreted language
It is dynamically typed
And it is easy to learn"""

pattern = '^Python|typed$'
result = re.findall(pattern, string, re.MULTILINE)
print(result)  # ['Python', 'typed']

# 이메일 주소 추출
def extract_email(string):
    # pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # 무지무지 복잡한 정규식 예시.
    pattern = r'(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
    emails = re.findall(pattern, string)
    return emails


string = "John's email is john.doe123@example.com. Jane can be reached at jane@example.co.uk. test email is asdfgh@naver.com"

emails = extract_email(string)
print(emails)  # ['john.doe123@example.com', 'jane@example.co.uk']


print("==========================================")
# 정규표현식을 사용한 데이터 유효성 검증
# 메일 주소의 유효성을 검증하는 예제

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email1 = 'example@example.com'
email2 = 'example@example.co.kr'
email3 = 'example.example.com'
email4 = 'example@example.'
email5 = 'example@example'

print(is_valid_email(email1))  # True
print(is_valid_email(email2))  # True
print(is_valid_email(email3))  # False
print(is_valid_email(email4))  # False
print(is_valid_email(email5))  # False


print("==========================================")
# 정규표현식을 사용한 데이터 유효성 검증
# 전화번호 유효성 검증하는 예제
def is_valid_phone_number(phone_number):
    pattern = r'^\d{3}-\d{3,4}-\d{4}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False

phone_number1 = '010-1234-5678'
phone_number2 = '02-123-4567'
phone_number3 = '123-4567'

print(is_valid_phone_number(phone_number1))  # True
print(is_valid_phone_number(phone_number2))  # True
print(is_valid_phone_number(phone_number3))  # False

print("==========================================")
# 로그 데이터에서 IP 주소를 추출하는 예시
log_data = [
    '192.168.0.1 - - [21/Feb/2022:10:12:01 +0900] "GET /index.html HTTP/1.1" 200 2326',
    '192.168.0.2 - - [21/Feb/2022:10:12:02 +0900] "GET /images/banner.jpg HTTP/1.1" 200 6571',
    '192.168.0.3 - - [21/Feb/2022:10:12:03 +0900] "POST /login.php HTTP/1.1" 302 -',
    '192.168.0.4 - - [21/Feb/2022:10:12:04 +0900] "GET /favicon.ico HTTP/1.1" 404 209'
]

ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

for log in log_data:
    ip = re.findall(ip_pattern, log)
    print(ip)


# 정규표현식의 한계
# 복잡한 패턴 처리의 한계
# 정규표현식은 매우 복잡한 패턴도 처리할 수 있지만, 너무 복잡한 패턴의 경우 처리 속도가 느려질 수 있습니다. 또한, 패턴의 복잡도가 높을수록 패턴을 이해하기 어려워지므로, 유지보수에 어려움을 겪을 수 있습니다.

# 모든 문제에 대해 적합하지 않음
# 정규표현식은 문자열 처리에 대한 매우 강력한 도구지만, 모든 문제에 대해 적합하지 않습니다. 예를 들어, 복잡한 자연어 처리나 문법 분석 등과 같은 문제에는 전용 라이브러리나 도구를 사용하는 것이 더욱 적합할 수 있습니다.

# 다양한 문자열 형식 처리의 한계
# 정규표현식은 일반적인 문자열 형식에 대한 처리를 제공합니다. 하지만, 특수한 문자열 형식이나 데이터 타입에 대한 처리에는 한계가 있습니다. 예를 들어, CSV 파일의 경우, 각 필드가 쉼표로 구분되어 있으므로, 쉼표를 기준으로 필드를 분리하는 방식으로 데이터를 처리할 수 있습니다. 하지만, CSV 파일의 경우, 인용부호나 특수문자 등의 예외상황이 있으므로, 정규표현식만으로 완벽하게 처리하기 어려울 수 있습니다.

# 유니코드 문자열 처리의 한계
# 정규표현식은 기본적으로 ASCII 문자열을 처리하는 것을 기본으로 합니다. 따라서, 유니코드 문자열을 처리할 때에는 적절한 옵션을 설정해야 합니다. 그렇지 않으면, 유니코드 문자열을 처리할 때 예기치 않은 결과가 발생할 수 있습니다.

# 가독성이 떨어지는 패턴
# 정규표현식을 사용하면서, 가독성이 떨어지는 패턴을 작성할 수 있습니다. 이러한 패턴은 다른 사람이 코드를 이해하기 어렵게 만들 수 있습니다.

# 패턴의 이해도가 낮은 경우
# 패턴의 이해도가 낮은 경우, 잘못된 패턴을 작성할 가능성이 높습니다. 이러한 경우, 원하는 결과를 얻기 어려울 수 있습니다. 따라서, 패턴을 작성할 때에는, 이해도를 높이기 위해 가능한 간단한 패턴을 작성하는 것이 좋습니다.



