# min()	Returns the smallest item in an iterable

"""
min(...)
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value

    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the smallest argument.
"""

#======================#

# 1st way of using min:
# min(iterable, *[, default = obj, key = func]) -> value

#print 1
print(min([1, 2, 3, 4]))

# when iterable is empty and would use the default obj that's None
print(min([], default= None))

# or use the key function method in the max
print(min([4, 2, 3], key=lambda x: x**2))

#======================#

# 2nd way of using min: (use none-iterable)
# min(arg1, arg2, *args, *[, key = func]) -> value

print(min(1, 2, 3, 4, key=lambda x: x/2))

#======================#