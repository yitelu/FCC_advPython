# frozenset()	Returns a frozenset object

"""
class frozenset(object)
 |  frozenset() -> empty frozenset object
 |  frozenset(iterable) -> frozenset object
 |
 |  Build an immutable unordered collection of unique elements.
"""

# frozenset([iterable])

# set type, immutable, hashable, unordered

a = frozenset({1, 2, 3, 3})

print(a)

# add & remove is not available in the frozenset due to frozenset is immutable
#a.add(12)
#a.remove(12)



