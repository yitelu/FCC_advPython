# memoryview()	Returns a memory view object

"""
class memoryview(object)
 |  memoryview(object)
 |
 |  Create a new memoryview object which references the given object.
"""

a = bytearray(b'hey')
print(a)

b = memoryview(a)
print(b.obj)
print(b[0: 1].tobytes())
b[0: 1] = b'B'
print(b.obj)

# useage is to change the b's value without making another copy

