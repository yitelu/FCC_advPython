# object()	Returns a new object

"""
class object
 |  The base class of the class hierarchy.
 |
 |  When called, it accepts no arguments and returns a new featureless
 |  instance that has no instance attributes and cannot be given any.
 |
 |  Built-in subclasses:
 |      async_generator
 |      BaseException
 |      builtin_function_or_method
 |      bytearray
 |      ... and 87 other subclasses
"""

# usage as Sentinel pattern
# when user entered "Q" and iter() would stop

sentinel = object()


def step():

    ans = input("please enter: ")

    if ans == "Q":
        return sentinel
    return ans


for feedback in iter(step, sentinel):
    print("you've entered", feedback)
