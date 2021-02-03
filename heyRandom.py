import random

# seudo random

a = random.random()
print(a)

b = random.uniform(1, 10)
print(b)

c = random.randint(1, 10)
print(c)

mylist = list("ABCDEFG")
aaa = random.choice(mylist)
print(aaa)

random.shuffle(mylist)
print(mylist)

#####################

# reproducible for the random seed
random.seed(1)
print(random.random())
print(random.randint(1,10))

