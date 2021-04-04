# isinstance()	Returns True if a specified object is an instance of a specified object

"""
isinstance(obj, class_or_tuple, /)
    Return whether an object is an instance of a class or of a subclass thereof.

    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.
"""

#check if the give object's type is correct

# True
print(isinstance("hey", str))

# False
print(isinstance("hey", int))

# True
print(isinstance({1: "hey"}, dict))

# use tuble args, which list is in the tuble
print(isinstance([1, 2], (str, int, list)))

#====================#

# real-world example: check the data object data type from the API request

data = {1: "hey"}
data_one = [1, 2, 3]

if isinstance(data_one, dict):
    print("it's dict")
elif isinstance(data_one, list):
    print("it's list")

#====================#