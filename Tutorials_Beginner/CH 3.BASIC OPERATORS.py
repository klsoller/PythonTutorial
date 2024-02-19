# CH 3.BASIC OPERATORS

'''

# PEMDAS matters
number = 1 + 2 * 3 / 4.0
print(number)

# use the (%) modulo to return integer.
remainder = 11 % 3
print(remainder)

# The ^ is not a power. Use ** for power
squared = 7 ** 2    # should be 49
cubed = 2 ** 3      # should be 8
print(squared)      # confirmed: 49
print(cubed)        # confirmed: 8

# Using Operators with Strings
# hellowWorld = "hello" - " " + "world" # this doesn't do anything: ERROR
hellowWorld = "hello" + " " + "world"
print(hellowWorld)

# Repeating Strings?
lotsOfHollos = "hello" * 10
# lotsOfHollos = "hello" ** 10  # this doesn't do anything: ERROR
print(lotsOfHollos)

# Using Operators with Lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

'''

# EXERCISE
x = object()
y = object()

# TODO: Change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list
print(x_list[0])
# print("x_list is: %d " % x_list)

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")