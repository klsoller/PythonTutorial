myString=  "hello"
myFloat = 10.0
myInt = 20

# testing code
#   % is a placeholder
#   %s is used for Strings
#       You can use multiple inputs %s is a %s ('this', 'String')
#   %d is used for integers.
#   %f is used for Floating Point Integers

if myString == "hello":
    print("String: %s" % myString)
    
if isinstance(myFloat, float) and myFloat == 10.0:
    print("Float: %f" % myFloat)
    
if isinstance(myInt, int) and myInt == 20:
    print("Integer: %d" % myInt)
    