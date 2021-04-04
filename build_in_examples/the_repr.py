# repr()	Returns a readable version of an object

"""
repr(obj, /)
    Return the canonical string representation of the object.

    For many object types, including most builtins, eval(repr(obj)) == obj.
"""

import datetime

today = datetime.datetime.today()

print(str(today))
print(repr(today))
print("\n")

# but the str part would show error when pass to eval()
#eval(str(today))

# the repr part would be the exact object in string when pass ot eval()
print(eval(repr(today)))


