# issubclass()	Returns True if a specified class is a subclass of a specified object

"""
issubclass(cls, class_or_tuple, /)
    Return whether 'cls' is a derived from another class or is the same class.

    A tuple, as in ``issubclass(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``issubclass(x, A) or issubclass(x, B)
    or ...`` etc.
"""

# issubclass(class, classinfo) return boolean

class Car:
    pass


class Ferrari(Car):
    pass


class Enzo(Ferrari):
    pass


#work on multi-level-inheritance
print(issubclass(Enzo, Ferrari))

print(issubclass(Enzo, Car))

print(issubclass(Car, Car))

# work on tuple of class
print(issubclass(Enzo, (Car, int, str)))

# work on tuple of class
print(issubclass(Enzo, (int, str)))
