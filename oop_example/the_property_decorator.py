#Python OOP

# property decorator: use the method as variable with @property decorator

#=================================================================================================#


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

    # use the method as variable with @property decorator
    @property
    def get_email(self):
        return f"{self.fname}.{self.lname}@email.com"

    def get_salary(self):
        return self.salary

    def apply_raise(self):
        self.salary *= self.raise_amount


# create two instance from employee class
emp1 = Employee("john", "smith", 5000)
emp2 = Employee("jane", "doe", 7000)

emp1.fname = "jim"

print(emp1.fname)
print(emp1.get_email) # use it like variable  with @property
