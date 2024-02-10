# CH 4. String Formatting.

'''
# Introduction
myName= "Kaleb"     # use the %s operator for Strings
print("Hello. My name is %s!" % myName)

# 2 or more aguments
myAge = 33              # use the %d operator for Integers
myLastName = "Soller"   # use the %s operator for Strings
print("Together now. I am %d years old. My name is %s %s." % (myAge, myName, myLastName))

# Other types
myList = [1,2,3]        # This uses the %s operator as well. "ANY OTHER OBJECT" uses the %s operator.
print("A list: %s" % myList)

# 
myNumber = 1.23456789
print("Two digits please: %.2f" % myNumber) #number of digitals

# %s - String
# %d - Integers
# %f - Floating Point Numbers
# %.<digit>f - Floating Point & decimal places
# %x or %X - Integers in HEX (lowercase / UPPERCASE)
'''

# EXERSIZE
data = ("John", "doe", 53.44)
format_string = "Hello"
print(format_string + " %s %s. Your current balance is $%.2f" % data)