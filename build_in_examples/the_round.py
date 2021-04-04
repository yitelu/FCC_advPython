# round()	Rounds a numbers

"""
round(number, ndigits=None)
    Round a number to a given precision in decimal digits.

    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.
"""

my_float = 3.141516

print(round(my_float, 3))

# following is the limitation for the round() that both return 2....
print(round(1.5))
print(round(2.5))
