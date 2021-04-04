# sum()	Sums the items of an iterator

"""
sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers

    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
"""

num = [1, 2, 3, 4]

print(sum(num))
print(sum(num, start=5))
