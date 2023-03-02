# 사용자로부터 국어, 영어, 수학 세 과목의 성적을 입력받아, 각 과목의 평균 점수와 총 평균 점수를 계산한 후, 
# 학점을 출력하는 프로그램을 작성하세요.
# 평균 점수는 소수점 둘째자리까지 출력합니다.
# 총 평균 점수는 국어: 40%, 영어: 40%, 수학: 20%로 가중치를 부여하여 계산합니다.
# 총 평균 점수가 90점 이상인 경우 "A", 80점 이상인 경우 "B", 70점 이상인 경우 "C", 60점 이상인 경우 "D", 60점 미만인 경우 "F"를 출력합니다.
k_score = int(input("국어 성적을 입력하세요: "))
e_score = int(input("영어 성적을 입력하세요: "))
m_score = int(input("수학 성적을 입력하세요: "))

totalScore = k_score * 40 / 100 + e_score * 40 / 100 + m_score * 20 / 100

if totalScore >= 90:
    grade = "A"
elif totalScore >= 80:
    grade = "B"
elif totalScore >= 70:
    grade = "C"
elif totalScore >= 60:
    grade = "D"
else:
    grade = "F"

print(f"국어: {k_score}, 영어: {e_score}, 수학: {m_score}")
print(f"각 과목의 평균 점수: {k_score:.2f}, {e_score:.2f}, {m_score:.2f}")
print(f"총 평균 점수: {totalScore:.2f}")
print(f"당신의 학점은 {grade}입니다.")
