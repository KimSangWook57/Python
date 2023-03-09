# 다음 딕셔너리에 대한 물음에 답하라.
d = [
     {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
     {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
     {'name': 'Princess', 'phone': '555-3141', 'email': ''},
     {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}
    ]


# 전화번호가 8로 끝나는 사용자 이름을 출력하라.
for people in d:
    if people['phone'][7] == '8':
        print(people['name'])

print("================================")
# 이메일이 없는 사용자 이름을 출력하라.
for people in d:
    if people['email'] == "":
        print(people['name'])

print("================================")
# 사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 
# 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라.
name = input("input name : ")

flag = 0

for people in d:
    if people['name'] == name:
        print(people['phone'], people['email'])
        flag = 1

if flag == 0:
    print("not found")