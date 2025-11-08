#abstraction : implement detail of class and only showing essential features
class Car:   
    def __init__(self):
        self.acc = False
        self.clutch = False

    def start(self):
        self.acc = True
        self.clutch = True
        print("Car started..") 

car1 = Car()  
car1.start()
            