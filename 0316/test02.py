# 클래스 메서드를 정의하고 사용하는 예시
# 클래스 메서드는 인스턴스가 아닌 클래스에 대한 작업을 수행하기 위해 사용되므로, 객체의 인스턴스 변수에 대한 접근이 불가능합니다. 
# 따라서, 클래스 메서드는 인스턴스를 통해 호출되는 것이 아니라, 클래스 이름을 이용하여 직접 호출됩니다.


class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    @classmethod
    def print_count(cls):
        print(cls.count)

# 클래스 메서드 호출
Rectangle.print_count() # 출력 결과: 0

# 인스턴스 생성 시 클래스 변수 값 증가
rectangle1 = Rectangle(3, 4)
Rectangle.print_count() # 출력 결과: 1

rectangle2 = Rectangle(5, 6)
Rectangle.print_count() # 출력 결과: 2
