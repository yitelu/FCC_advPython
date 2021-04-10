#Python OOP

# class is the blueprint to create the instance of that class (object)

# each object created from the class could have attributes (variable) and method (functions)

# instance variable (object) and class variable (the blueprint)

class Employee:

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def get_email(self):
        return f"{self.fname}.{self.lname}@email.com"

    def get_salary(self):
        return self.salary

#=================================================================================================#
'''
create two objects from employee class without using the class attribute and method
'''
# em1 = employee()
# em2 = employee()
#
# print(em1)
# print(em2)
#
# em1.firstname = "john"
# em1.lastname = "smith"
# em1.email = "john.smith@email.com"
# em1.salary = 5000
#
# em2.firstname = "jane"
# em2.lastname = "doe"
# em2.email = "jane.doe@email.com"
# em2.salary = 6000
#
# print(em1.email)
# print(em2.email)

#=================================================================================================#
'''
create two objects from employee class using the class predefined attribute and method
'''

emp1 = Employee(fname="john", lname="smith", salary=5000)
print(f"employee {emp1.fname} has email of {emp1.get_email()} and the salary is {emp1.get_salary()}")

emp2 = Employee(fname="jane", lname="doe", salary=6000)
print(f"employee {emp2.fname} has email of {emp2.get_email()} and the salary is {emp2.get_salary()}")

#=================================================================================================#

'''
# call the object with following ways that both ways works the same
'''

# call the instance(self) object's own method directly
print(emp1.get_salary())

# call the class method directly and pass in the instance(self)
print(Employee.get_salary(emp1))
