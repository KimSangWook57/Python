class Rectangle:
    count = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Rectangle.count += 1

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 클래스 변수 값을 출력
print(Rectangle.count) # 출력 결과: 0

# 인스턴스 생성 시 클래스 변수 값 증가
rectangle1 = Rectangle(3, 4)
print(Rectangle.count) # 출력 결과: 1

rectangle2 = Rectangle(5, 6)
print(Rectangle.count) # 출력 결과: 2

# 인스턴스 변수에 접근하여 값 출력
print(rectangle1.width) # 출력 결과: 3
print(rectangle1.height) # 출력 결과: 4
print(rectangle2.width) # 출력 결과: 5
print(rectangle2.height) # 출력 결과: 6

# 인스턴스 메서드 호출
print(rectangle1.area()) # 출력 결과: 12
print(rectangle2.area()) # 출력 결과: 30
print(rectangle1.perimeter()) # 출력 결과: 14



