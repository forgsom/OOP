class ex1_1:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def VVOD(self):
        self.a = int(input("a = "))
        self.b = int(input("b = "))
        self.c = int(input("c = "))


class ex1_2(ex1_1):
    def __init__(self):
        self.x = 0

    def Calc(self):
        self.x = (self.c - self.b) / self.a

    def Display(self):
        print("Результат -", self.x)


test = ex1_2()
test.VVOD()
test.Calc()
test.Display()
