#Python OOP

# regular method: take "self" as default argument in the regular method. eg. def get_email(self):

# class method: need to add @classmethod decorator and receive class(cls) as 1st argument instead of instance(self)

# static methods: need to add @staticmethod decorator but don't pass "self" or "cls" in as the default 1st argument

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


# the default raise_amount in the namespace should be 1.04
print(Employee.__dict__)

# create two instance from employee class
emp1 = Employee("john", "smith", 5000)
emp2 = Employee("jane", "doe", 7000)

# change the class variable "raise_amount" to 1.50 via the class method
Employee.set_raise_amt(1.50)
# same as change the class variable directly
#Employee.raise_amount = 1.70

# all Employee class variable and instance's raise_amount value should get updated to 1.50
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp_str_1 = "John-Doe-7000"
# call the class method of from_string as alternative constructor
new_emp_1 = Employee.from_string(emp_str_1)
print(f"{new_emp_1.fname} email acc is {new_emp_1.get_email()}")
print(f"{new_emp_1.fname} salary amount is {new_emp_1.get_salary()}")


# validate if the static method of is_workday works or not
my_date = datetime.date(2021, 4, 10)
print(Employee.is_workday(my_date))
