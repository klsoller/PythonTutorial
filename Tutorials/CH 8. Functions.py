# CH 8 - FUNCTIONS


'''
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
def myFunctionWithArgs(username, greeting):
    print("Hello, %s, From My Function! I wish you %s!" % (username, greeting))
    
# print a simple greeting
myFunction()

myFunctionWithArgs("John Doe", "a great year")

x = addTwoNumbers(1,2)
'''


# EXERCISE
def get_list_benefits():
    return ["More organized code,",
            "more reaable code,",
            "easier code reuse",
            "Allowing programmers to share and connect code together"]



def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit
  

def name_the_benefits_of_functions():
    list_of_benefits = get_list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))
    # print(" is a benefit of functions!")
        
name_the_benefits_of_functions()

