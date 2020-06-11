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

class Developer(Employee):
    hike = 1.10

    # This will enable the superclass to handle the attributes which it already handles
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees==None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("--->", emp.full_name())
# emp1 = Developer("Abhinav", "Bhatt", "5000000")
# emp2 = Developer("Test", "User", "70000000")

# print(help(Developer))

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)
# emp1 = Developer("Abhinav", "Bhatt", 10000, "Python")
# print(emp1.pay, emp1.prog_lang)

emp1 = Employee("Abhinav", "Bhatt", 3000000)
mgr1 = Manager("Abi", "Bh", 10, [emp1])
mgr1.print_emps()

print(isinstance(mgr1, Manager))
print(issubclass(Manager, Employee))
