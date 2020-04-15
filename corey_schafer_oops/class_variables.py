#Class variables are variables that are shared among each instance of# Class is basically a way to logically goup data nd methods associated with it. Basically a blueprint for creating objects.

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

emp1 = Employee("Abhinav", "Bhatt", "5000000")
emp2 = Employee("Test", "User", "70000000")

print(emp1)
print(emp2)
print(emp1.full_name())

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(Employee.hike)

print(emp1.__dict__)
