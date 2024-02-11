# CH 9 - Classes and Objects


'''
# LESSON 1
class MyClass:
    variable = "blah"
    
    def function(self):
        print("This is a message in the class|function.")
        
myObjectX = MyClass()
# print(myObjectX)
myObjectX.variable
print(myObjectX.variable)
# print(myObjectX.variable)

# LESSON 2
print("\nLESSON 2")
myObjectY = MyClass()
myObjectY.variable = "yackity"


print("X Object should be blah: %s" % myObjectX.variable)
print("Y Object should be yakity: %s" % myObjectY.variable)


# LESSON 3 - ACCESSING OBJECT FUNCTIONS
print("\nLESSON 3")

myObjectX.function()    # testing calling functions inside a class.


# LESSON 4 - init()
print("\nLESSON 4")
class NumberHolder:
    def  __init__(self, number): #called when the class is being initiated
        self.number = number    
        
    def returnNumber(self):
        return self.number
        
var = NumberHolder(7)
# print(var.returnNumber)   # ERROR: Don't forget the function parenthesis ()
print(var.returnNumber())
'''

# EXERCISE
print("\nEXERCISE")
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 10000.00
    def __init__(self, vName, vKind, vColor, vValue):
        self.name = vName
        self.kind = vKind
        self.color = vColor
        self.value = vValue
        
    def description(self):
        desc_str = ("The %s is a %s "+ # the '+' isn't needed. I used it to learn how to split text on a print line.
            "%s worth $%.2f.") % (  # you need to add the parenthesis to wrapp the entire text.
            self.kind, 
            self.color, 
            self.name, 
            self.value)
        return desc_str
    
'''
Instead of calling all of these at initialization, I could 
have called them individually. This would initialize the car
without know the parameters ahead of time.
My tutorial doesn't describe which methos is best practice under which circumstances.
'''
car1 = Vehicle("Honda", "Accord", "Blue", 25123)
car2 = Vehicle("Ford", "F-150", "Red", 54979)
print(car1.description())
print(car2.description())