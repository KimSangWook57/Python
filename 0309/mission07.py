# 두 개의 리스트가 주어졌을 때, 두 리스트에 공통으로 포함된 요소를 모두 담은 리스트를 반환하는 프로그램을 작성하시오.

list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]

# 공통된 요소인 2와 4를 모두 포함한 리스트를 반환한다.
# 결과값
# [2, 4]

list3 = set(list1) & set(list2)
print(list(list3))