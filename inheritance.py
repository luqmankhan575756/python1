class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped")

class ToyatCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyatCar("fortuner")
car2 = ToyatCar("prius")

print(car1.name)
print(car1.start())

       
