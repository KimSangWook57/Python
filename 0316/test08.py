# pip를 이용한 설치
# 대부분의 파이썬 패키지는 pip라는 패키지 관리자를 이용하여 설치할 수 있습니다. 
# pip는 파이썬 2.7.9 버전부터 기본적으로 제공되는 패키지 관리 도구입니다. 
# 명령 프롬프트(Windows) 또는 터미널(Mac, Linux)에서 아래와 같은 명령어를 이용하여 설치할 수 있습니다.
# NumPy 패키지를 설치 예시
# pip install numpy

# dir() 함수
# 모듈이나 클래스에 포함된 변수, 메소드, 클래스 등의 속성들을 확인할 수 있습니다.

# random 모듈에 대한 dir() 사용 예시
# import random

# # random 모듈 내에 포함된 변수, 함수, 클래스 등을 나열합니다.
# print(dir(random))

# # random 모듈 내에 포함된 choice 함수의 도움말을 출력합니다.
# print(help(random.choice))

# 모듈 탐색 우선순위
# 현재 작업 디렉토리 (os.getcwd()로 확인 가능)
# PYTHONPATH 환경 변수에 지정된 디렉토리
# 표준 라이브러리 디렉토리
# site-packages 디렉토리

# 이 중에서 가장 먼저 발견된 모듈이 사용되며, 나머지는 무시됩니다.

# sys.path
# 현재 파이썬 인터프리터가 모듈을 검색할 경로들을 담고 있는 리스트입니다.
# 현재의 디렉토리와 시스템 경로 변수 출력하기
# import os, sys
# print(os.getcwd())   # 현재 디렉토리 표시
# print(sys.path)      # 환경변수에 지정된 디렉토리

# from import
# from import는 모듈에서 특정 변수, 함수, 클래스 등을 가져올 때 사용됩니다.

# from import *
# *를 사용하여 모든 변수, 함수, 클래스 등을 가져오는 것은 권장되지 않습니다. 
# 왜냐하면, 모듈에서 모든 것을 가져오면 현재 스코프에서 이름 충돌이 일어날 수 있기 때문입니다. 
# 또한, 모듈에서 사용하지 않는 함수나 클래스도 불필요하게 가져오기 때문에 메모리 낭비가 발생할 수 있습니다.

# if __name__ == '__main__':의 기능
# 파이썬에서 스크립트를 실행할 때, 해당 모듈이 메인으로 실행되는 경우에만 코드를 실행하도록 하는 용도로 사용됩니다. 
# 이 코드를 작성하면 해당 모듈이 다른 모듈에 의해 import 되어 사용될 때는 해당 코드가 실행되지 않습니다.

# a.py 모듈에서 b.py 모듈을 import 하여 사용한다고 가정해보겠습니다. 
# 만약 b.py 모듈 내에 if name == 'main': 구문이 있다면, a.py 모듈에서 b.py 모듈을 import 해도 해당 구문은 실행되지 않습니다.

# 이러한 용도로 if name == 'main': 구문을 사용하는 이유는 보통 해당 모듈을 개발할 때 테스트 코드를 작성하여 테스트하는 경우가 많은데, 
#이 때 테스트 코드는 해당 모듈이 메인으로 실행되는 경우에만 실행되도록 하기 위해서 사용합니다. 
# 또한, 다른 모듈에서 import 되었을 때는 실행되지 않기 때문에, 모듈에서 정의한 함수나 클래스 등을 다른 모듈에서도 사용할 수 있습니다.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    print(add(3, 5))
    print(subtract(10, 7))

# 이 모듈을 다른 모듈에서 import해서 사용할 경우 if __name__ == '__main__': 이하의 코드는 실행되지 않습니다. 
# 하지만 이 모듈을 스크립트로 직접 실행할 때는 if __name__ == '__main__': 이하의 코드가 실행됩니다.
