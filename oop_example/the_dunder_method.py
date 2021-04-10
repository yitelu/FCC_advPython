#Python OOP

# dunder method: like __add__ method that could be overwrite in class

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

    # overwrite the dunder method of the __add__ dunder method
    def __add__(self, other):
        return self.salary + other.salary



# create two instance from employee class
emp1 = Employee("john", "smith", 5000)
emp2 = Employee("jane", "doe", 7000)

# use the overwrite __add__ method, otherwise the "+" won't work on employee instance
print(emp1 + emp2) # return total salary of both employee