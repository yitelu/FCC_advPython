# vars()	Returns the __dict__ property of an object

"""
vars(...)
    vars([object]) -> dictionary

    Without arguments, equivalent to locals().
    With an argument, equivalent to object.__dict__.
"""

print(vars(dict))

# vars() is same as following dict.__dict__
print(dict.__dict__)