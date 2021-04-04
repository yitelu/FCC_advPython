# hash()	Returns the hash value of a specified object

"""
hash(obj, /)
    Return the hash value for the given object.

    Two objects that compare equal must also have the same hash value, but the
    reverse is not necessarily true.
"""


#     Return the hash value for the given object.
#     Two objects that compare equal must also have the same hash value, but the
#     reverse is not necessarily true.

# hash(object)

# Hash values are integers.
# Hash are used to quickly compare dictionary keys during a dictionary lookup.

# very importable that it only works on "Immutable" objects

# bool -> immutable
# int -> immutable
# float -> immutable
# list -> mutable
# tuple -> immutable
# str -> immutable
# set -> mutable
# frozenset -> immutable
# dict -> mutable

# only "list" , "set" and "dict" are mutable, hence not hashable! (error: TypeError: unhashable)

my_list = [1, 2, 3]
my_set = {1, 2, 3, 3}
my_dict = {1: "a", 2: "b", 3: "c"}

#print(type(hash(my_list)))
#print(hash(my_set))
#print(hash(my_dict))


#======================================#
# type of hash is always int
#print(type(hash(str(1))))
