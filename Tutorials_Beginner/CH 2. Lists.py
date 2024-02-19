'''

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3



# prints out 1,2,3
for x in mylist:
    print(x)
'''


# LISTS

'''
# EXERSIZE ONE

myList = []

myList.append(1)
myList.append(2)
myList.append(3)

print(myList)
print(myList[0])
print(myList[1])
print(myList[12])

for x in myList:
    print(x)

'''

# EXERSIZE 2
'''
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
'''
numbers = []
strings = []
listONames = []
names = ["John", "Eric", "Jessica"]

# write your own code here
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")
listONames.append(names[0])
listONames.append(names[1])
listONames.append(names[2])
second_name = "Stephen King"

# this code should write out the filled arrays and the second name in the names list (Erid)
print(numbers)
print(strings)
print("Print the list of names:" and listONames)
print("The second name on the names list is %s" %listONames[1])