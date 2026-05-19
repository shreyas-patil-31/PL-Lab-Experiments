# Single Inheritance

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

c = Child()
c.show()
c.display()

# Multiple Inheritance

class A:
    def methodA(self):
        print("We are currently in method A")

class B:
    def methodB(self):
        print("We are currently in method B")

class C(A, B):
    def methodC(self):
        print("We are currently in method C")

obj = C()
obj.methodA()
obj.methodB()
obj.methodC()