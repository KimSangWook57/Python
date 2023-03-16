# 문제: 학생 정보를 관리하는 프로그램을 만드세요.
# 학생(Student) 클래스
# 인스턴스 변수: 이름(name), 학번(student_id), 학년(year), 전공(major), 평균 성적(avg_score)
# 메서드: get_info() - 학생의 정보를 문자열로 반환
class Student():
    def __init__(self, name, student_id, year, major, avg_score):
        self.name = name
        self.student_id = student_id
        self.year = year
        self.major = major
        self.avg_score = avg_score

    def get_info(self):
        return f"이름 : {self.name}, 학번 : {self.student_id}, 학년 : {self.year}, 전공 : {self.major}, 평균 성적 : {self.avg_score} "


# 학생들을 관리하는 클래스(StudentManager)
# 인스턴스 변수: 학생들(student_list)
# 메서드:
# add_student(student): 학생을 리스트에 추가하는 메서드
# remove_student(student_id): 학번을 이용해 학생을 리스트에서 제거하는 메서드
# find_student(student_id): 학번을 이용해 학생을 찾는 메서드
# show_all_students(): 모든 학생의 정보를 출력하는 메서드
class StudentManager():
    def __init__(self):
        # 학생 리스트 생성.
        self.student_list = []

    def add_student(self, student):
        # 리스트 안에 학생의 정보를 넣는다.
        self.student_list.append(student)

    def remove_student(self, student_id):
        # 리스트를 돌며 학생들의 정보를 student에 넣는다.
        for student in self.student_list:
            # 리스트 안의 학번이 입력한 학번과 같다면, 학생을 찾은 것이다.
            if student.student_id == student_id:
                # 삭제 과정 표시.
                self.student_list.remove(student)
                print(f"{student_id} 학번 학생 삭제 완료.")
                return
        # 루프를 다 돌았다면 찾지 못했다고 표시.
        print(f"{student_id} 학번을 가진 학생이 없습니다.")

    def find_student(self, student_id):
        # 리스트를 돌며 학생들의 정보를 student에 넣는다.
        for student in self.student_list:
            # 리스트 안의 학번이 입력한 학번과 같다면, 학생을 찾은 것이다.
            if student.student_id == student_id:
                print(f"{student_id} 학번을 가진 학생이 있습니다.")
                return
        # 루프를 다 돌았다면 찾지 못했다고 표시.
        print(f"{student_id} 학번을 가진 학생이 없습니다.")

    def show_all_students(self):
        # 리스트를 돌며 학생들의 정보를 student에 넣는다.
        for student in self.student_list:
            # get_info() 함수를 이용해 표시.
            print(student.get_info())


# 위 클래스들을 이용하여 다음과 같은 프로그램을 작성하세요.
# 학생 관리자(StudentManager)를 생성합니다.
student_manager = StudentManager()
# 학생(Student)을 생성합니다. 학생의 인스턴스 변수는 이름, 학번, 학년, 전공, 평균 성적을 포함합니다.
student1 = Student('홍길동', '20230001', 2, '컴퓨터공학', 90.5)
student2 = Student('임꺽정', '20230002', 4, '전자공학', 82.5)
student3 = Student('장길산', '20230003', 1, '건축공학', 92.5)
# 학생 관리자에 학생을 추가합니다.
student_manager.add_student(student1)
student_manager.add_student(student2)
student_manager.add_student(student3)
# 학생 관리자에서 학생을 삭제합니다.
student_manager.remove_student('20230001')
student_manager.find_student('20230004')
# 학생 관리자에서 학생을 찾습니다.
student_manager.find_student('20230002')
student_manager.find_student('20230005')
# 학생 관리자에서 모든 학생의 정보를 출력합니다.
student_manager.show_all_students()
