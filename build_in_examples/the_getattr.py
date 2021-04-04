# getattr()	Returns the value of the specified attribute (property or method)

"""
getattr(...)
    getattr(object, name[, default]) -> value

    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.
"""

# getattr(object, name, default)


class car():
    engine = 5
    doors = 2

    @staticmethod
    def start_engine():
        print("zoom zoom")

my_car = car()

#get the attribute of door from the car class
print(getattr(my_car, "doors", None))

#get the attribute of "door" that is not exist from the car class, and return None
print(getattr(my_car, "door", None))

# able to get the method from the car class, make sure to put () in the end
print(getattr(my_car, "start_engine")())



