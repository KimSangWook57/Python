# 파일 읽기

file = open("example.txt", "r")

# 파일 내용 전체를 읽습니다.
content = file.read()
print(content)

# 파일에서 한 줄을 읽습니다.
line = file.readline()
print(line)

# 파일 전체를 읽고 각 줄을 리스트로 반환합니다.
lines = file.readlines()
print(lines)

file.close()  # 파일을 닫습니다.


# with 문은 파일을 열고 작업을 마치면 파일을 자동으로 닫아줍니다.

with open("example.txt", "r") as file:
    # 파일 내용 전체를 읽습니다.
    content = file.read()
    print(content)
