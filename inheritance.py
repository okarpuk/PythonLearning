class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def work(self):
        print(f"{self.name} works")

tom = Employee("Tom")
tom.work()

# Множественное наследование

class Employee:
    def work(self):
        print("Employee works")
class Student:
    def study(self):
        print("Student studies")
class Working_student(Employee, Student):
    pass

tom = Working_student()
tom.work()
tom.study()
