# String: ordered, immutable, text representation

#single quote or double quote is fine
my_string = "Hello"

print(my_string)

##########
myString = "Hello World"

#quick way to reverse a string
char = myString[::-1]
print(char)

#can't access a charactor and change it
#myString[0] = 'A'

#########
# remove the white spaces before and after the string

myStr = '     Hello World    '
print("before strip: " + myStr)
myStr = myStr.strip()
print("after strip: " + myStr)
print(myStr[0])

########
myUpStr = "hello"
print(myUpStr.upper())
######

# Split the String into a List of separate string.
my_strings = "how are you doing"
my_list = my_strings.split(" ") #default split by space
print(my_list)

#join the list of String back to a String (*** very important, easier than for loop method)
new_string = " ".join(my_list)
print(new_string)

################

# %, .format(), f-Strings
var = "TOM"
varNum = 555
varFloat = 3.12
myT_string = "the variable is %s" % var
myN_string = "the varialbe is %d" % varNum
myF_string = "the varialbe is %f" % varFloat
print(myT_string)
print(myN_string)
print(myF_string)

# Newer .format() method for the placement order {}
myStrs = "the variable is {:.2f} and {}".format(varFloat, var)
print(myStrs)

# since Python 3.6 that could use the f-Strings, highly recommended to use!
myStrs2 = f"the variable is {var} , {varNum} and {varFloat}"
print(myStrs2)
#f-String could do runtime var calculation
myStrs2 = f"the variable is {var*2} , {varNum*3} and {varFloat*10}"
print(myStrs2)
