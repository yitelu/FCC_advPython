# eval()	Evaluates and executes an expression

"""
eval(source, globals=None, locals=None, /)
    Evaluate the given source in the context of globals and locals.

    The source may be a string representing a Python expression
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
"""


#convert string to python execution code
my_string = "5 + 5"

print(eval(my_string))



