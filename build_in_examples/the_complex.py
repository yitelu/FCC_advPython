# complex()	Returns a complex number

"""
class complex(object)
 |  complex(real=0, imag=0)
 |
 |  Create a complex number from a real part and an optional imaginary part.
 |
 |  This is equivalent to (real + imag*1j) where imag defaults to 0.
"""


# In mathematics, a complex number is a number that can be expressed in the form a + bi,
# where a and b are real numbers, and i is a symbol called the imaginary unit

# BTW, in python uses 'j' instead of 'i'

# print "0j"
print(complex())

a = complex(1, 2)

print(a)

# print 1.0 the real number (float type)
print(type(a.real))
print(a.real)

# print 2.0 the imaging number (float type)
print(type(a.imag))
print(a.imag)

