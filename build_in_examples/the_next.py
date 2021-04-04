# next()	Returns the next item in an iterable

"""
next(...)
    next(iterator[, default])

    Return the next item from the iterator. If default is given and the iterator
    is exhausted, it is returned instead of raising StopIteration.
"""

# beware that iterable object can only be loop through once

num = [1 , 2, 3]

a = iter(num)

while True:
    try:
        print(next(a))
    except StopIteration:
        print("end of iterable item")
        break
