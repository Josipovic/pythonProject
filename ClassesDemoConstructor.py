class SecondClass:
    def m1(self):
        print("good morning")
        self.values(100,100)  # call a method in another method

    def values(self, val1, val2):
        print(val1)
        print(val2)
        self.val1 = val1  # local variable stored as a class variable
        self.val2 = val2

    def __init__(self):
        print("this is a constructor")



c = SecondClass()
c.m1()
c.values(1,2)
