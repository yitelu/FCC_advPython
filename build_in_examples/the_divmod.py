# divmod()	Returns the quotient and the remainder when argument1 is divided by argument2

"""
divmod(x, y, /)
    Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.
"""

#quotient = 5, remainder = 0
print(divmod(10, 2))

#quotient = 3, remainder = 1
print(divmod(10, 3))

#quotient = 2, remainder = 2
print(divmod(10, 4))

#quick assignment, a = 3, b = 1
a, b = divmod(10, 3)

print(a)
print(b)