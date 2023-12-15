class ex2_1:
    class ex2_2:
        def __init__(self):
            self.x = 0

        def Display(self):
            print("Результат -", self.x)

    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def VVOD(self):
        self.a = int(input("a = "))
        self.b = int(input("b = "))
        self.c = int(input("c = "))

    def Calc(self):
        self.x = (self.c - self.b) / self.a


test1 = ex2_1()
test2 = ex2_1.ex2_2()
test1.VVOD()
test1.Calc()
test2.Display()
