# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

'''
from itertools import product

a = [1, 2]
b = [3]

prod = product(a, b, repeat=2)

print(list(prod))


from itertools import permutations

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

from itertools import combinations, combinations_with_replacement

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

from itertools import accumulate
import operator

a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))


from itertools import groupby

def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value))
'''

from itertools import count, cycle, repeat

a = [1,2,3]

for i in count(10):
    print(i)
    if i == 15:
        break

#infinite loop for "count" , "cycle" and "repeat"
