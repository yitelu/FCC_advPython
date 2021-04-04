# setattr()	Sets an attribute (property/method) of an object

"""
setattr(obj, name, value, /)
    Sets the named attribute on the given object to the specified value.

    setattr(x, 'y', v) is equivalent to ``x.y = v''
"""

class car:
    brand = "toyota"
    color = "red"


print(getattr(car, 'brand'))

print(setattr(car, "brand", "BMW"))

print(getattr(car, 'brand'))
