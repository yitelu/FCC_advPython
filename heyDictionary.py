# Dictionary: Key-Value pairs, Unordered, Mutable

mydict = {"name": "Max", "age": 28, "city": "new york"}

print(mydict)

#able to create dictionary via following ways as well
#btw no need to use "" quotes for the keys
mydict2 = dict(name = "Mary", age=28, city="boston" )
print(mydict2)

#######
# get the value from the dict by providing the key
myName = mydict2['name']
print(myName)

myName2 = mydict["city"]
print(myName2)

########
#add new key-value pair to existing dict
mydict["email"] = "max@xyz.com"
print(mydict)

#####
#del dict
del mydict["city"]
print(mydict)

mydict.pop("name")
print(mydict)

#since Python3.7 that remove the last item in the dict
mydict.popitem()
print(mydict)

#######
# search if item is in dict
if 'name' in mydict2:
    print(mydict2['name'])

#######
# Use the "try and except"
try:
    print(mydict2['lastname'])
except:
    print("error")

###################
# loop through the dict

#print all the keys
for key in mydict2.keys():
    print(key)

#print all the values
for value in mydict2.values():
    print(value)

#print both key and value
for key, value in mydict2.items():
    print(key, value)

######
# copy dictionary use the copy function to make sure the TRUE copy

mydict_cpy = mydict2.copy()

mydict_cpy['name'] = "john"
mydict_cpy['address'] = "123 tom street"

print(mydict_cpy)
print(mydict2)

#######
# merge two dictionary
oh_dict = {'name': "Max", 'age': 20, 'email':"ccc@xyz.com" }
oh_dict2 = dict(name= "Marry", age=19, city="BOSTON")

oh_dict.update(oh_dict2)

#merge both dict, the existing one would get update, and none-existing would be added
print(oh_dict)

##############
# can use the Tuple as key, but unable to use List as key

myTuples = (9, 2)
heymydict = {myTuples: 333}

print(heymydict)

#TypeError: unhashable type: 'list'
#myList =[1,2]
#heymydict2= {myList: 999}  -----> can't put LIST as key
#print(heymydict2) 


