class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("car stopped")

class ToyatCar(Car):
    def __init__(self, name , type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = ToyatCar("fortuner" , "electric")
print(car1.type)