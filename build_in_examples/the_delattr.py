# delattr()	Deletes the specified attribute (property or method) from the specified object

"""
delattr(obj, name, /)
    Deletes the named attribute from the given object.

    delattr(x, 'y') is equivalent to ``del x.y''
"""

class fruit:
    price = 300
    kind = "banana"


# display all the attribute of the fruit class before delete attribute
print('fruit', fruit.__dict__)

# delete the "price" attribute from that fruit class
delattr(fruit, 'price')

# display all the attribute of the fruit class after delete attribute
print('fruit', fruit.__dict__)


#print all the dict in class
for key, value in fruit.__dict__.items():
    print(key+"\n")
    print(value)