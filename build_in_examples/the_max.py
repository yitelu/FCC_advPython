# max()	Returns the largest item in an iterable

"""
max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value

    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
"""

#======================#

# 1st way of using max:
# max(iterable, *[, default = obj, key = func]) -> value

#print 4
print(max([1, 2, 3, 4]))

# when iterable is empty and would use the default obj that's None
print(max([], default= None))

# or use the key function method in the max
print(max([4, 2, 3], key=lambda x: x**2))

#======================#

# 2nd way of using max: (use none-iterable)
# max(arg1, arg2, *args, *[, key = func]) -> value

print(max(1, 2, 3, 4, key=lambda x: x/2))

#======================#