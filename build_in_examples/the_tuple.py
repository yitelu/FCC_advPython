# tuple()	Returns a tuple

"""
class tuple(object)
 |  tuple(iterable=(), /)
 |
 |  Built-in immutable sequence.
 |
 |  If no argument is given, the constructor returns an empty tuple.
 |  If iterable is specified the tuple is initialized from iterable's items.
 |
 |  If the argument is a tuple, the return value is the same object.
 |
 |  Built-in subclasses:
 |      asyncgen_hooks
 |      UnraisableHookArgs
"""

num = [1 ,2, 3]

a = tuple(num)

print(a)

# cast tuple object to list, change the value and cast back to tuple due to immutability
a = list(a)
a[1] = 99

a = tuple(a)
print(a)
