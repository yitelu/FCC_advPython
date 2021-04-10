#Python OOP

# class variable are the variable that share amount all instance (object),
# class variable using the "class.variable" to access directly.

# instance variable are only specific viable to that specific instance (object), using the "self.variable" way

# instance always use "instance variable" first and then "class variable" if both variable is the same variable name.


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


# class variable has the variable of raise_amount in the namespace
print(Employee.__dict__)

# create two instance from employee class
emp1 = Employee("john", "smith", 5000)
emp2 = Employee("jane", "doe", 7000)

# instance doesn't have the instance variable of "raise_amount" in namespace that is in the class variable scope only.
print(emp1.__dict__)
print(emp2.__dict__)

print("before apply raise")
print(f"{emp1.fname} is getting salary of {emp1.salary}")
print(f"{emp2.fname} is getting salary of {emp2.salary}")

# create the emp2's obj own instance variable of raise_amount locally with x2 times
emp2.raise_amount = 2
print(emp2.__dict__)
# call emp2's apply_raise and it use emp2's own raise_amount of "2" instead of the class variable "1.04" (priority!)
emp2.apply_raise()

# specify the instance that would get raise with the class variable of 1.04 in following 2 ways:
#employee.apply_raise(emp1)
emp1.apply_raise()


print("after apply raise")
print(f"{emp1.fname} is getting salary of {emp1.salary}")
print(f"{emp2.fname} is getting salary of {emp2.salary}")

# call the "class variable" and emp1 & emp2 instance/obj do not see the class variable of "num_of_employee"
print(Employee.num_of_employee)

