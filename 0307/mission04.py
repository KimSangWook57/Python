# 3명 이상 친구 이름 리스트를 작성하고 다음 내용을 프로그램하시오.
# insert 문법 형식에 주의.
friend_list = ["홍길동", "임꺽정", "장길산", "홍경래"]
# 01. insert()로 맨 앞에 새로운 친구 추가
friend_list.insert(0, "김연아")
print(friend_list)
# 02. insert()로 3번째 위치에 새로운 친구 추가
friend_list.insert(2, "박찬호")
print(friend_list)
# 03. append()로 마지막에 친구 추가
friend_list.append("손연재")
print(friend_list)

# 리스트 [1, 2, 3]에 대해 다음과 같은 처리를 하라.
list1 = [1, 2, 3]
# 01. 두 번째 요소를 17로 수정
list1[1] = 17
print(list1)
# 02. 리스트에 4, 5, 6을 추가
list1 += [4, 5, 6]
# list2 = [4, 5, 6]
# list1.extend(list2)
print(list1)
# 03. 첫 번째 요소 제거
del list1[0]
print(list1)
# 04. 리스트를 요소 순서대로 배열하기
list1.sort()
print(list1)
# 05. 인덱스 3에 25넣기
list1.insert(3, 25)
print(list1)
