# exec()	Executes the specified code (or object)

"""
exec(source, globals=None, locals=None, /)
    Execute the given source in the context of globals and locals.

    The source may be a string representing one or more Python statements
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
"""

# exec() is very similar to eval()


# my_string = "3 + 5"
# print(exec("print(my_string)"))

print(exec("print(min(10, 5, 9))"))


# remove all the built-in-function and only add-back the one that's needed to use, for safety purpose!
print(exec("print(1)", {"__builtins__": None}, {"print": print}))
