import os

# 현재 작업 디렉토리 확인
current_dir = os.getcwd()
print("현재 작업 디렉토리:", current_dir)
print("=================================================")
# 새로운 디렉토리 생성
new_dir = "new_directory"
os.mkdir(new_dir)
print(f"새로운 디렉토리 '{new_dir}'가 생성되었습니다.")
print("=================================================")
# 생성한 디렉토리 내에 파일 생성
new_file = "new_file.txt"
with open(os.path.join(new_dir, new_file), "w") as f:
    f.write("새로운 파일 내용")
print(f"'{new_file}' 파일이 '{new_dir}' 디렉토리 내에 생성되었습니다.")
print("=================================================")
# 지정된 디렉토리의 파일 및 디렉토리 목록 확인
list_dir = os.listdir(new_dir)
print(f"'{new_dir}' 디렉토리 내의 파일 및 디렉토리 목록: {list_dir}")
print("=================================================")
# 파일인지 디렉토리인지 확인
for item in list_dir:
    item_path = os.path.join(new_dir, item)
    if os.path.isfile(item_path):
        print(f"'{item_path}'는 파일입니다.")
    elif os.path.isdir(item_path):
        print(f"'{item_path}'는 디렉토리입니다.")
print("=================================================")
# 파일 삭제
os.remove(os.path.join(new_dir, new_file))
print(f"'{new_file}' 파일이 삭제되었습니다.")
print("=================================================")
# 디렉토리 삭제
os.rmdir(new_dir)
print(f"'{new_dir}' 디렉토리가 삭제되었습니다.")
print("=================================================")