# bool()	Returns the boolean value of the specified object

"""
class bool(int)
 |  bool(x) -> bool
 |
 |  Returns True when the argument x is true, False otherwise.
 |  The builtins True and False are the only two instances of the class bool.
 |  The class bool is a subclass of the class int, and cannot be subclassed.
 |
 |  Method resolution order:
 |      bool
 |      int
 |      object
"""

num = [1, 2, 3, 4, 5]

print(bool(6 in num))

print(bool(3 in num))
