# slice()	Returns a slice object

"""
class slice(object)
 |  slice(stop)
 |  slice(start, stop[, step])
"""

my_list = [1 ,2 ,3 ,4, 5]

my_slice = slice(None, None, -1)

print(my_list[::-1])

print(my_list[my_slice])



