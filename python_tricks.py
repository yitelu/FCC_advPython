
#=================#
# Swap the two variable without temp variable

# a = 10
# b = 30
# a, b = b, a
# print(a, b)

#=================#
# list comprehension.
#eg. from 0~20, put all even number in a list

# even = [n for n in range(21) if n % 2 == 0]
# print(even)

#=================#
# list manipulation

#python has 2 methods of list manipulation
# 1: MAP
# 2: Filter

# numbers = [1, 2, 3]
#
# def square(n):
#     return n * n
#
# def even(n):
#     return n % 2 == 0
#
# def multiply(x, y):
#     return x * y

#apply all element in the list to the function via the MAP function
# squares = list(map(square, numbers))
# print(squares)

#apply all element in list and only add those that could get filter.
# even = list(filter(even, numbers))
# print(even)

#=================#
#ternary condition
# check if the condition is true or false
#
# condition = False
# print("True" if condition else "False")

#=================#
# calculate large number and print out large number
# num1 = 1_000_000_000
# num2 = 1_000_000
#
# total = num1 + num2

# the out put number would have comma
# print(f"{total:,}")

#=================#
# "context manager" to open and close

# with open('text.txt', 'r') as f:
#     file_contents = f.read()

#=================#
# use the enumerate to access both index and element in the same time

# name = ['a', 'b', 'c']
#
# for index, n in enumerate(name, start=1):
#     print(index, n)

#=================#
# looping through two list and unpack those list
# beware that ZIP would stop after the shortest list exhausted

# names = ['a', 'b', 'c']
# nums = ['1', '2', '3']
#
# for name, num in zip(names, nums):
#     print(f"{name} is corresponding to {num}")


#=================#
# Unpacking example

# a, b, *c = (1, 2, 3, 4, 5)
# print(f"{a}\n{b}\n{c}\n")

#=================#
# "setattr" & "getattr" usage in the class

# class Person():
#     pass
#
# person = Person()
#
# first_key = 'first'
# first_val = "Mike"
#
# setattr(person, first_key, first_val)
#
# first = getattr(person, first_key)
#
# print(person.first)
#
# print(first)


#=================#
# use the help() & dir() to check particular usage of the function.