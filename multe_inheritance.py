#multi level inheritance
class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped")

class ToyatCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyatCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start()
