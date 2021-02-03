# Sets: unordered, mutable, no duplicates!
# like dict use {} but no key-value pair, just separate with comma

#not allow duplicates, so only 1,2,3 would print
myset = {1, 2, 3, 1, 2}
print(myset)

########
# nice trick to find out how many different characters in a words.

myset = set("hello")
print(len(myset))
# print 4 due to l is dup and order doesn't matter

#####
# if what to have a empty set need to use a SET method
emptySet = set()
print(type(emptySet))

#####
# add and remove the set
addtheset = set()
addtheset.add(1)
addtheset.add(2)
addtheset.add(3)

#no error if no such element in the set
addtheset.discard(4)
print(addtheset)

##############

for i in addtheset:
    print(i)

#############
# union and intersection method in SET

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

i = evens.intersection(primes)
print(i)

##################
# return diff

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)
print(type(diff))
###################

# frozenset is just the normal set but it's a immutable version of set.
# can't change the frozenset after its created.

a = frozenset([1,2,3,4])
print(a)

#add or remove won't work on the frozenset
#a.remove()
#a.add()