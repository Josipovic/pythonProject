class MyClass:

    # class variables
    a, b = 100, 200

# @staticmethod    # directly call it by using a class name
#  def m1(self)
#    print("")

def myfunc(self):
    print(self.a + self.b) # access class variables


# instance method
def display(self, name):
    print(name)

# Function # Method

# object
# mc = MyClass() # named object
# mc.myfunc()

MyClass() # nameless object

# static method
# MyClass.m1()

# if global and local variables are the same : print(globals() ['a'])