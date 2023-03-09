# 학생들의 성적을 딕셔너리로 저장하고, 성적 평균을 계산하는 프로그램을 작성해보세요.
# 출력결과
# Average grades:
# Alice: 90.0
# Bob: 80.0
# Charlie: 95.0


data = {
        "Alice": [85, 90, 95],
        "Bob": [75, 80, 85],
        "Charlie": [95, 95, 95]
        }

for name, score in data.items():
    avg = sum(score) / len(score)
    print(name, avg)