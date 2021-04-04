# iter()	Returns an iterator object

"""
iter(...)
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator

    Get an iterator from an object.  In the first form, the argument must
    supply its own iterator, or be a sequence.
    In the second form, the callable is called until it returns the sentinel.
"""

# help(iter)

#   iter(iterable) -> iterator
#   iter(callable, sentinel) -> iterator

#   Get an iterator from an object.  In the first form, the argument must
#   supply its own iterator, or be a sequence.
#   In the second form, the callable is called until it returns the sentinel.

# ======================================#

#   Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# print(iter([1, 2, 3]))
#
# print(iter((1, 2, 3)))
#
# print(iter({1: 'a', 2: 'b', 3: 'c'}))
#
# print(iter({1, 2, 3}))

# ======================================#

# iter(callable, sentinel) -> the sentinel is for the loop to stop when hit the sentinel

# num = [1, 2, 3, 4, 5, 6, 7, 9, 10]
#
# a = iter(num)
#
# # print 1
# print(next(a))
#
# # print 2
# print(next(a))

# ======================================#

# iter(callable, sentinel) -> the sentinel is for the loop to stop when hit the sentinel

import random

#create a lambda function that return any random number from 1 to 9, when sentinel hit 5 and it would stop
a = iter(lambda: random.randrange(1, 10, 1), 5)

game_start = True

while game_start:

    try:
        # print the next iterable item from the iterable object a
        print(next(a))

    # when the iter() sentinel catch and raised the StopIteration exception
    except StopIteration:
        game_start = False

# ======================================#