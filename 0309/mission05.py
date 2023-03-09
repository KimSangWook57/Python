# 숫자들이 들어있는 리스트에서 중복된 숫자를 제거하고, 남은 숫자들의 합을 계산하는 프로그램을 작성해보세요.
# Sum of unique numbers: 15

list1 = [1, 2, 2, 3, 3, 3, 4, 4, 5]
set1 = set(list1)
total = sum(set1)

print(f"Sum of unique numbers : {total}")