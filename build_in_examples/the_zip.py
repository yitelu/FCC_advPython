# zip()	Returns an iterator, from two or more iterators

"""
class zip(object)
 |  zip(*iterables) --> A zip object yielding tuples until an input is exhausted.
 |
 |     >>> list(zip('abcdefg', range(3), range(4)))
 |     [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
 |
 |  The zip object yields n-length tuples, where n is the number of iterables
 |  passed as positional arguments to zip().  The i-th element in every tuple
 |  comes from the i-th iterable argument to zip().  This continues until the
 |  shortest argument is exhausted.
"""

num_one = [1, 2, 3]
num_two = [4, 5, 6]
num_three = [7, 8, 9, 10] #10 would get ignore in zip

print(list(zip(num_one, num_two, num_three)))
