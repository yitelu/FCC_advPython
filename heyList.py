# Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", 'cherry', 'apple']

print(mylist)

#empty list
mylist2  = list()

print(mylist2)

#allow different data type and duplicates
mylist3 = [5, False, "apple", 'apple' ]

print(mylist3)

item = mylist[-2]
print(item)

for i in mylist:
    print(i)

if False in mylist3:
    print('yes in list')
else:
    print('no in list')

print(len(mylist))

mylist.append('lemon')
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

#remove the last item in the list and return it!
item = mylist.pop()
print(item)
print(mylist)

#doesn't return "cherry"
item = mylist.remove("cherry")
print(item)
print(mylist)


mylist.reverse()
print(mylist)

mylist4 = [4,3,1,]
mylist4.sort()
print(mylist4)

#sorted method won't affect the original list.
mylist5 = [2,1,3,7,0]
newlist = sorted(mylist5)
print(newlist)
print(mylist5)

#create a list with multiple of same elements in the list
mylist6 = [0] *5
print(mylist6)

#able to add two list together
mylist7 = [1,2,3,4,5]
mynewlist = mylist6 + mylist7
print(mynewlist)

#slicing in list

mylist8 = [1,2,3,4,5,6,7,8,9]
a = mylist8[1:5]
print(a)

#if not specify the start or end and always start from 0 or no end and alway stop at last item.
b = mylist8[:5]
c = mylist8[0:]
print(b)
print(c)
d = mylist8[::2]
print(d)
#nice way to reverse the list
e = mylist8[::-1]
print(e)

#make sure don't just use assign that would make both varible assign to the same address.
#use list_org.copy() method to copy
list_org = ['banana', 'cherry', 'apple']

#(1) use the copy method.
#list_cpy = list_org.copy()

#(2) ust the list function to ocpy
#list_cpy = list(list_org)

#(3) use the sliciing to actually copy
list_cpy = list_org[:]

list_cpy.append("lemon")
print(list_cpy)
print(list_org)

#######

#squre root the list in one sentence
mylist9 = [1,2,3,4,5,6]
b = [x*x for x in mylist9]

print(mylist)
print(b)

###############

