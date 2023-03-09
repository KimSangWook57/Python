# 람다 함수의 기본 문법 = lambda 인자: 표현식

# 람다 함수는 함수의 인자로 전달되거나, 함수의 반환값으로 사용될 수 있기 때문에 매우 유용하게 사용됩니다.
# 함수의 인자로 전달된 예시.
students = [
    {'name': 'Alice', 'score': 80},
    {'name': 'Bob', 'score': 90},
    {'name': 'Charlie', 'score': 70},
]

# 점수(score)를 기준으로 학생 리스트 정렬(내림차순을 위해 reverse값을 true로 지정.)
sorted_students = sorted(students, key=lambda student: student['score'], reverse=True)
print(sorted_students)
# 출력 결과: [{'name': 'Bob', 'score': 90}, {'name': 'Alice', 'score': 80}, {'name': 'Charlie', 'score': 70}]

# 재귀함수(Recursive Function)
# 자기 자신을 호출하여 문제를 해결하는 함수를 의미합니다. 즉, 함수 내에서 자기 자신을 호출하여 반복적으로 작업을 수행합니다.
# 함수가 종료되는 조건을 반드시 포함해야 한다(상수 반환문)

# 재귀함수의 예시
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)  # 출력결과: 120

