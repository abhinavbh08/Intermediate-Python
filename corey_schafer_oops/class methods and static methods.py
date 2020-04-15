# Class Methods are initiated with @classmethod annotation.
# instance methods automatically pass self(the object) as an argument
# class methods automatically pass cls(the class) as an argument
# static methods do not pass self or clas, they are just like regular methods.
# class methods can be used as alternate constructors.

class Employee:

    hike = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + "." + last + "@company.com"

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(int(self.pay) * self.hike)

    @classmethod
    def set_raise(cls, amount):
        cls.hike = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

emp1 = Employee("Abhinav", "Bhatt", "5000000")
emp2 = Employee("Test", "User", "70000000")

print(Employee.hike)
Employee.set_raise(1.05)
print(Employee.hike)
print(emp1.__dict__)

emp3 = Employee.from_string("John-Doe-600")
print(emp3.first, emp3.last, emp3.pay)