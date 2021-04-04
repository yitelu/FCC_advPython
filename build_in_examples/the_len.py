# len()	Returns the length of an object
#
# len(obj, /)
# Return the number of items in a container.

"""
len(obj, /)
    Return the number of items in a container.
"""

# beware need to check if such object has __len__ method or len would fail on that object
# like int object doesn't have __len__ could use dir(int) to check if __len__ exists
#print(len(123))
#print(dir(int))

# the list object has the __len__ dunder methods so the len method would work on list object like following:
#print(dir(list))
print(len([1, 2, 3, 4]))

