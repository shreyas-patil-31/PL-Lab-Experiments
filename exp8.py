# Class and Object example

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

# Creating objects
s1 = Student("Shreyas", 85)
s2 = Student("Rahul", 35)

print("\nStudent 1 Details:")
s1.display()
s1.check_result()

print("\nStudent 2 Details:")
s2.display()
s2.check_result()