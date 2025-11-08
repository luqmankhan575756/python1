class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "+", self.img, "i")

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(2, 4)
num2.showNumber()
