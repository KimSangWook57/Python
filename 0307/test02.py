# 1부터 10까지의 숫자 중에서 짝수만 포함하는 리스트를 생성

even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(even_numbers)  # 출력: [2, 4, 6, 8, 10]

# 리스트 내 모든 요소에 1을 더하는 예제

original_list = [1, 2, 3, 4, 5]
new_list = [num + 1 for num in original_list]
print(new_list)  # [2, 3, 4, 5, 6]

# 리스트 내 문자열의 길이를 구하는 예제

words = ['apple', 'banana', 'cherry', 'durian']
word_lengths = [len(word) for word in words]
print(word_lengths)  # [5, 6, 6, 6]

# 문자열 리스트에서 길이가 5보다 큰 문자열만 대문자로 바꾸기

words = ["apple", "banana", "orange", "grape", "watermelon"]
result = [word.upper() for word in words if len(word) > 5]
print(result)  # ['BANANA', 'ORANGE', 'WATERMELON']

# 리스트 내 중첩된 요소들을 단일 리스트로 만드는 예제

original_list = [[1, 2], [3, 4], [5, 6]]
new_list = [num for sublist in original_list for num in sublist]
print(new_list)  # [1, 2, 3, 4, 5, 6]

# 주어진 이차원 리스트에서 짝수만 리스트로 생성하기

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [num for row in matrix for num in row if num % 2 == 0]
print(result)  # [2, 4, 6, 8]
