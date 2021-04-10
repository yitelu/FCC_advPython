#Python OOP

# inheritance: create subclasses that inherit from the super class

#=================================================================================================#
import datetime

class Employee:

    #class variable
    raise_amount = 1.04
    num_of_employee = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

        # the class variable of num_of_employee would increase everytime new instance/obj of employee created
        Employee.num_of_employee += 1

    def get_email(self):
        return f"{self.fname}.{self.lname}@email.com"

    def get_salary(self):
        return self.salary

    def apply_raise(self):
        self.salary *= self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # use case as the alternative contructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        # 5 is Saturday and 6 is Sunday
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# inherit from Employee class,
class Developer(Employee):
    raise_amount = 1.50

    def __init__(self, fname, lname, salary, prog_language):
        super().__init__(fname, lname, salary)
        self.prog_language = prog_language

# create two instance from Developer class
emp1 = Developer("john", "smith", 5000, "Python")
emp2 = Developer("jane", "doe", 7000, "Java")

# check help file to know the inherit level via the "Method resolution order"
#print(help(emp1))

print(emp1.get_salary())
emp1.apply_raise() # use the "raise_amount" via the Developer class
print(emp1.get_salary())

# Both developer instance display with inherit class
print(emp1.get_email())
print(emp1.prog_language)

print(emp2.get_email())
print(emp2.prog_language)


# built-in-function: isinstance
print(isinstance(emp1, Employee)) #True
print(issubclass(Employee, Developer)) #False
print(issubclass(Developer, Employee)) #True