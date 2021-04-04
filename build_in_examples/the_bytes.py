# bytes()	Returns a bytes object

"""
class bytes(object)
 |  bytes(iterable_of_ints) -> bytes
 |  bytes(string, encoding[, errors]) -> bytes
 |  bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
 |  bytes(int) -> bytes object of size given by the parameter initialized with null bytes
 |  bytes() -> empty bytes object
 |
 |  Construct an immutable array of bytes from:
 |    - an iterable yielding integers in range(256)
 |    - a text string encoded using the specified encoding
 |    - any object implementing the buffer API.
 |    - an integer
"""

print(bytes("hey", "UTF-8"))

num = [1, 2, 3]

print(bytes(num))

num.append(4)

print(bytes(num))

