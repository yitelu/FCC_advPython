# bytearray()	Returns an array of bytes

"""
class bytearray(object)
 |  bytearray(iterable_of_ints) -> bytearray
 |  bytearray(string, encoding[, errors]) -> bytearray
 |  bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
 |  bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
 |  bytearray() -> empty bytes array
 |
 |  Construct a mutable bytearray object from:
 |    - an iterable yielding integers in range(256)
 |    - a text string encoded using the specified encoding
 |    - a bytes or a buffer object
 |    - any object implementing the buffer API.
 |    - an integer
"""

x = bytearray([1, 2, 3])

print(x)

x.append(1)

print(x)

x.reverse()

print(x)