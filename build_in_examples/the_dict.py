# dict()	Returns a dictionary (Array)

"""
class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
"""

# use it as **kwargs
print(dict(a=1, b=2))

# use it as mapping, **kwargs
print(dict({'a': 1, 'b': 2}, c=3))

# use it as Iterable, **kwargs
print(dict([('a', 1), ('b', 2)], c=88))

