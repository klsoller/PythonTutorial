# CH 10 - Dictionaries


'''
# LESSON 1
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)


# LESSON 2
print("\nLESSON 2")
phonebook2 = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
    }
print(phonebook2)


# LESSON 3 - Iterating over dictionaries
print("\nLESSON 3")
# phonebook.keys
# phonebook.values
# phonebook.copy
for name, number in phonebook.items(): # iterates over KEY & ITEM, PAIRS. More research in dictionaries to learn more. SEE ABOVE.
    print("Phone number of %s is %d" % ( name, number ))

# LESSON 4 - Removin
# g a value
# print("\nLESSON 4")
# del phonebook["John"]
# print(phonebook)
phonebook.pop("John")
print(phonebook)
'''


# EXERCISE
print("\nEXERCISE")
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  
# your code goes here
phonebook["Jake"] = 938273443
phonebook.update({"Jakey" : 938273443}) # used as append, or append/new
phonebook.pop("Jill")


# testing code
if "Jake" in phonebook:
    print("Jake is list in the phonebook")    
    
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook")
    
print(phonebook)