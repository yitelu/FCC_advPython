# pow()	Returns the value of x to the power of y

"""
pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.
"""

# power func
print(pow(5, 2, 12))

# same as
print((5 ** 2) % 12)
