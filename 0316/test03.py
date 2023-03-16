class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


p = Person("Alice", 25)
print(p.__age)  # 비공개 인스턴스 변수에 접근 시 에러 발생

p = Person("John", 30)
print(p.get_name())  # "John" 출력
p.set_name("Alice")
print(p.get_name())  # "Alice" 출력
