# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

"""
#counter
from collections import Counter

a = "aaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
#most 2 key-value pair that's the most common
print(my_counter.most_common(2))
#show all the element in the list
print(list(my_counter.elements()))
"""

"""
from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)
"""

"""
from collections import OrderedDict
#since Python 3.7 that the Dictonary could ordered

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)
"""

"""
from collections import defaultdict

d = defaultdict(int)
d["a"] = 1
d["b"] = 2
#due to the d['c'] doesn't exist that the default value for d['c'] would be 0 due to default int value 0 
print(d['c'])

#the "normal dictionary" would give a "keyError" if there's no such key.
"""

#deque pronounce as Deck, (double ended )

from collections import deque
d = deque()
d.append(1)
d.append(2)

d.appendleft(3)

d.pop()
d.popleft()

print(d)

d.extend([4,5,6])

print(d)

#move all elements to the right 2 elements
d.rotate(2)

#move all elements to the left 2 elements
d.rotate(-2)
print(d)