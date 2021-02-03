# Tuple: ordered, immutable, allows duplicate elements (size smaller and more efficient)
# Lists: ordered, mutable, allows duplicate elements

# Tuple can't be change change after its created (hence immutable)

import sys, timeit

myTuple = ("Max", 28, "Boston")
print(myTuple)

#######
#if only 1 element in the Tuple and need to put the comma in the end.

myTuple2 = ("Max", )
print(type(myTuple2))

########
#build in tuple function

myTuple3 = tuple(["max", 29, "SJ"])
print(myTuple3)

item = myTuple3[2]
print(item)

for x in myTuple3:
    print(x)

if "john" in myTuple3:
    print("yes")
else:
    print("no")

#TypeError: 'tuple' object does not support item assignment (immutable)
#myTuple3[0] = "TOM"

###########

my_tuple = ('a', 'p', 'p', 'l', 'e')

print(len(my_tuple))
print(my_tuple.count("p"))

#return 1st occurrence of p
print(my_tuple.index('p'))

#convert tuple to list and convert from list back to list:
my_list = list(my_tuple)
print(type(my_list))

my_new_tuple = tuple(my_list)
print(type(my_new_tuple))

###################
#tuple slicing
a = (1,2,3,4,5,6,7,8,9)
b = a[1:3]
print(b)
####################

#unpacking in python:
my_tuple = "Max", 28, "Boston"

name, age, city = my_tuple

print(name)
print(age)
print(city)
#beware that the number of element for unpacking must match the tuple!!!
# due to valueError: too many values to unpack (expected 2)

######
#unpacking technics
my_tuple2 = (0, 1, 2,3, "JOHN",)

i1, *i2, i3 = my_tuple2

print(type(i1))
print(type(i3))
#i2 would become the list of [1,2,3] !!! good technics
print(i2)

########

#explain why TUPLE is MORE efficient than list!

my_list1 = [0,1,2,"hello", True]
my_tuple1 = (0,1,2,"hello", True)
print(sys.getsizeof(my_list1), "bytes")
print(sys.getsizeof(my_tuple1), "bytes")
# list has the same elements as the tuple, but the tuple's size is smaller

# tuple is more efficient to iterate
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1_000_000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1_000_000)) #tuple won!

########