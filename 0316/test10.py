import sys

# sys.argv 예시
print("명령행 인자(argument) 리스트:", sys.argv)
print("=================================================")
# sys.getsizeof() 예시
a = [1, 2, 3]
print("a의 크기:", sys.getsizeof(a))
print("=================================================")
# sys.stdin, sys.stdout, sys.stderr 예시
sys.stdout.write("표준 출력 테스트\n")
sys.stderr.write("표준 오류 출력 테스트\n")
input_data = sys.stdin.readline().strip()
print("입력값:", input_data)
print("=================================================")
# sys.version, sys.platform 예시
print("현재 파이썬 버전:", sys.version)
print("현재 시스템 플랫폼:", sys.platform)
print("=================================================")
# sys.path 예시
print("모듈 검색 경로:", sys.path)
print("=================================================")