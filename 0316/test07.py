from abc import *

# 추상 클래스를 사용하여 여러 클래스가 일정한 형태의 메서드를 구현하도록 강제하는 예제

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("Car started.")
        
    def stop(self):
        print("Car stopped.")

class Bike(Vehicle):
    def start(self):
        print("Bike started.")
        
    def stop(self):
        print("Bike stopped.")

vehicles = [Car(), Bike()]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()
