# hasattr()	Returns True if the specified object has the specified attribute (property/method)

"""
hasattr(obj, name, /)
    Return whether the object has an attribute with the given name.

    This is done by calling getattr(obj, name) and catching AttributeError.
"""

# hasattr(object, name)

# checks if the object has the attribute or not, return True or False

class bike():
    brand = "Giant"
    wheels = 4

my_bike = bike()

# return True
print(hasattr(my_bike, "brand"))
