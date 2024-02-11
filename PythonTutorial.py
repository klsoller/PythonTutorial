# CH 8 - FUNCTIONS

# LESSON 1
print("\nLESSON 1")
# definition of functions are defined by the word 'def'
def myFunction():
    print("Hello, from myFunction!")
    

# functions can also contain arguments
def addTwoNumbers(a, b):
    return a + b


# LESSON 2 - Calling a function
print("\nLESSON 2")
def myFunctionWithArgs(usernmae, greeting):
    print("Hello, %s, From My Function! I wish you %s" % (username, greeting))
    
# print a simple greeting
myFunction()