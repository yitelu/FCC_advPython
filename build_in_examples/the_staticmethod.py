# @staticmethod()	Converts a method into a static method

"""
class staticmethod(object)
 |  staticmethod(function) -> method
 |
 |  Convert a function to be a static method.
 |
 |  A static method does not receive an implicit first argument.
 |  To declare a static method, use this idiom:
 |
 |       class C:
 |           @staticmethod
 |           def f(arg1, arg2, ...):
 |               ...
 |
 |  It can be called either on the class (e.g. C.f()) or on an instance
 |  (e.g. C().f()). Both the class and the instance are ignored, and
 |  neither is passed implicitly as the first argument to the method.
 |
 |  Static methods in Python are similar to those found in Java or C++.
 |  For a more advanced concept, see the classmethod builtin.
"""

class Car:
    def my_instance_method(self):
        return 'my_instance_method', self

    @classmethod
    def my_class_method(cls):
        return 'my_class_method', cls

    @staticmethod
    def my_static_method():
        return "my_static_method"


the_car = Car()

print(the_car.my_instance_method())
print(Car.my_class_method())
print(Car.my_static_method())

