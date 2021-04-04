# enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object

"""
class enumerate(object)
 |  enumerate(iterable, start=0)
 |
 |  Return an enumerate object.
 |
 |    iterable
 |      an object supporting iteration
 |
 |  The enumerate object yields pairs containing a count (from start, which
 |  defaults to zero) and a value yielded by the iterable argument.
 |
 |  enumerate is useful for obtaining an indexed list:
 |      (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
"""

num = ["a", "b", "c"]

for index, value in enumerate(num, start=0):
    print(f"index of {index} has the value of {value}")
