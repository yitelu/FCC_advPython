# map()	Returns the specified iterator with the specified function applied to each item

"""
class map(object)
 |  map(func, *iterables) --> map object
 |
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
"""


# ====================#

def add_func(n):
    return n + n


# print [2, 4, 6, 8]
print(list(map(add_func, [1, 2, 3, 4])))

# ====================#

# could use lambda when needed to simplify the func part

print(list(map(lambda x: x + x, [1, 2, 3, 4])))

# ====================#
