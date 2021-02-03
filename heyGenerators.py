# generator is to safe more memory
import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num =0
    while num < n:
        yield num
        num += 1

    return num

#print(sys.getsizeof(firstn(1_000_000)))

#generator is much smaller in size
#print(sys.getsizeof(firstn_generator(1_000_000)))

print("normal: ")
print(firstn(10))

print("generator")
print(list(firstn_generator(10)))