# id()	Returns the id of an object

"""
id(obj, /)
    Return the identity of an object.

    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)
"""

# return the location in memory of the object

# id(object)

#return the identify of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime.

# should be the same ID address for the immutabel objects (except the mutable object like, List, Set, Dict).

a = "hello"
b = "hello"

print(id(a))

print(id(b))

print(a == b)
#===========================


c = [1, 2, 3]
d = [1, 2, 3]
print(id(c), id(d))
print(c == d)

# both ID point to the same address in immutable object.

#================================
#python v3.9 should 
a = 123456789876543211234567891234456789
b = 123456789876543211234567891234456789

print(id(a) == id(b))