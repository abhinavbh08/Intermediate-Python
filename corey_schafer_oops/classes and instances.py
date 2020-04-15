# Class is basically a way to logically goup data nd methods associated with it. Basically a blueprint for creating objects.

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def full_name(self):
        return "{} {}".format(self.first, self.last)

emp1 = Employee("Abhinav", "Bhatt", "5000000")
emp2 = Employee("Test", "User", "70000000")

print(emp1)
print(emp2)
print(emp1.full_name())