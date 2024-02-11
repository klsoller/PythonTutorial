
# CH 6. Conditions
# https://www.learnpython.org/en/Conditions


'''
# Lesson 1
from operator import truediv


print("Lesson 1")
x = 2
print( x == 2)    # prints out True
print( x == 3)      # prints out False
print( x < 3 )    # prints out True
print( x != 2 )     # != is the "not equals" operator for python.


# Lesson 2 - Boolean Operators
print("\nLesson 2")
name = "Kaleb"
age = 23
if name == "Kaleb" and age == 23:
    print("Your name is %s, and you are also %d years old." % (name, age))
    
if name == "Kaleb" or name == "Rick":
    print("Your name is either %s or %s" % (name, "Rick"))
    
    
# Lesson 3 - The "in" operator
print("\nLesson 3")

if name in ["Kaleb", "Rick"]:
    # print(name.index())   # if, not for loop
    print("Your name is either Kaleb or Rick.")
    

# Lesson 4 - IF STATEMENTS
print("\nLesson 4")
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    print("ELIF SECTION")
    # do something else
    pass
else:
    # do a third thing
    pass


# LESSON 5
print("\nLESSON 5")
if x == 2:
    print("x equals two!")
else:
    print("x does not equal two.")


# LESSON 6 - The 'is' Operator
print("\nLESSON 6")
x = [1,2,3,]
y = [1,2,3]
print( x == y ) # Prints out True
print( x is y ) # Prints out False


# LOSSON 7 - The 'NOT' Operator
# The 'not' function inversts the boolean.
print("\nLESSON 7")
print( not False )              # prints out True
print( not False == (False) )   # prints out False
'''

# EXERCISE
# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")    
    
if first_array: # empty array is FALSE
    print("2")  # non-empty array is TRUE
    
# print(len(second_array))
if len(second_array) == 2:
    print("3")    

if len(first_array) + len(second_array) == 5:
    print("4")    
    
if first_array and first_array[1] == 1: # !! interesting. The [0] applies to both arrays.
    print("5")    

if not second_number:
    print("6")    