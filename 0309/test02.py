# set 생성
my_set = {1, 2, 3}

# 개수 확인
print(len(my_set))  # 출력: 3

# 요소 추가
my_set.add(4)
print(my_set)  # 출력: {1, 2, 3, 4}

# 여러 요소 추가
my_set.update([5, 6, 7])
print(my_set)  # 출력: {1, 2, 3, 4, 5, 6, 7}

# 요소 제거 (remove)
my_set.remove(3)
print(my_set)  # 출력: {1, 2, 4, 5, 6, 7}

# 요소 제거 (discard)
my_set.discard(10)  # 요소가 없어도 오류 발생하지 않음
print(my_set)  # 출력: {1, 2, 4, 5, 6, 7}

print("========================================")
# 집합 연산
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 합집합
print(set1.union(set2))  # {1, 2, 3, 4, 5}
print(set1 | set2)       # {1, 2, 3, 4, 5}

# 교집합
print(set1.intersection(set2))  # {3}
print(set1 & set2)              # {3}

# 차집합
print(set1.difference(set2))  # {1, 2}
print(set1 - set2)            # {1, 2}

# 대칭차집합
print(set1.symmetric_difference(set2))  # {1, 2, 4, 5}
print(set1 ^ set2)                      # {1, 2, 4, 5}
