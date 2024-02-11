# CH 7 - LOOPS
# https://www.learnpython.org/en/Loops


# LESSON 1 - 
from binascii import a2b_hex
from re import A


print("Lesson 1")
primes = [2,3,5,7]
for prime in primes:
    print(prime)
    

# LESSON 2 - RANGE & XRANGE
print("\nLesson 2")
# 'range' returns a new list
# 'xrange' returns an iterator
# print out the numbers 0,1,2,3,4
for x in range(5):
    print(x)
    
# prints out 3, 4, 5
for x in range(3,6):
    print(x)
    
# prints out 3, 5, 7
for x in range(3, 8, 2):
    print(x)
    

# LESSON 3 - 'while' loops
print("\nLESSON 3 - 'while' loops")
count = 0
while count < 5:
    print(count)
    count += 1  # this is the same as count = count +1
    

# LESSON 4 - 'brea' & 'continue' statements
print("\nLESSON 4 - break-continue")
count = 0
while True:
    if count >= 5:
        break   # the same as turning the while True, off.
    print(count)
    count += 1
    
# prints out only the odd numbers - 1,3,5,7,9

for x in range(10):
    # check if x is even
    if x % 2 == 0:
        continue    # IF 0, back to beginning.
    print(x)
    

# LESSON 5 - 'else' in for-loops
print("\nLESSON 5")