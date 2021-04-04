# sorted()	Returns a sorted list

"""
sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
"""

num = [5, 4, 3, 2, 1]

print(sorted(num))

print(sorted(num, reverse=True))