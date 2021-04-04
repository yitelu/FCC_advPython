# filter()	Use a filter function to exclude items in an iterable object

"""
class filter(object)
 |  filter(function or None, iterable) --> filter object
 |
 |  Return an iterator yielding those items of iterable for which function(item)
 |  is true. If function is None, return the items that are true.
 |
 |  Methods defined here:
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __next__(self, /)
 |      Implement next(self).
 |
 |  __reduce__(...)
 |      Return state information for pickling.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
"""

# filter(function, iterable)

num = [1, 2, 10, 11, 12, 0]

# usually use lambda if it's a simple function
my_ans = list(filter(lambda x: x >= 10, num))

print(my_ans)


# filter() could accept None as function and filter out any false value like 0
my_ans_two = list(filter(None, num))

# should print out [1, 2, 10, 11, 12] without 0
print(my_ans_two)
