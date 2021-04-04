# callable()	Returns True if the specified object is callable, otherwise False

"""
callable(obj, /)
    Return whether the object is callable (i.e., some kind of function).

    Note that classes are callable, as are instances of classes with a
    __call__() method.
"""

#functions are callables
#Classes are callables
#Methods (which are functions) are callable
#Instances of classes can even be turned into callables.

#can check if it's callable, use the "hasattr(bool, '__call__')"

#print false due to String is data type not a class, hence not callable
print(callable("hey"))

#only class type is callable, hence type() is callable
print(callable(type("hey")))


print(hasattr("hey", "__call__")) #String not callable
print(hasattr(int, "__call__")) #integer object is callable
print(hasattr([], "__call__")) #not callable




