# locals()	Returns an updated dictionary of the current local symbol table

"""
locals()
    Return a dictionary containing the current scope's local variables.

    NOTE: Whether or not updates to this dictionary will affect name lookups in
    the local scope and vice-versa is *implementation dependent* and not
    covered by any backwards compatibility guarantees.
"""

#True when first check initialy, but would change based on the variable
print(globals() is locals())

def print_names():
    name = "john"

    print(name)

    print(locals())
    print(globals())

    print(locals() is globals()) # False

print_names()

