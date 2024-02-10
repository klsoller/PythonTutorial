# CH 5. Basic String Operations

'''
# Lesson 1.
astring = "HeloWorld1"      # Intentionally mispelled for unique charater order demonstrations below.
astring2 = 'Helo World2'     # Intentionally mispelled for unique charater order demonstrations below.

print(astring)
print(astring2)
print("Single quaotes are ' 'd")
print(len(astring))

# Lesson 2
# Both Work?
print(astring.index('H'))   # This are case sensitive.
print(astring.index("H"))   # This are case sensitive.

# Lesson 3
print(astring.count("l"))   # counts how many "l"'s are in the string.

# Lesson 4
print("Lesson 4:")
print(astring[3:7]) #>=3, but <7. Not to include 7.
print(astring[3:])  # All >=3.
print(astring[:7])  # All up to <7.

# Lesson 4.1
print("Lesson 4.1")
print(astring[-4])      # Fourth Letter from the end
print(astring[-4:])     # All up to <4, reverse.
print(astring[:-7])     # Removes the last <7 characters.
print(astring[:-1])     #   Removes the last entry

# Lesson 5
print("Lesson 5")
print(astring[0:11:2])   # [start:stop:step] # effectively does nothing. Return every 1 entry. 
print(astring[0:11:1])   # [start:stop:step] # skip every 2nd entry.

# Lesson 6
# [start:stop:step]
print(astring[::-1])    # prints the whole string in reverse.
print(astring[::-2])    # prints the whole string in reverse, skpping every other one. [start:stop:step]

# Lesson 7 
print("Lesson 7")
print(astring.upper())  # Print all characters UPPER case
print(astring.lower())  # Print all characters LOWER case

# Lesson 8
print("Lesson 8")
print(astring.startswith("Helo"))       # boolean operation:    TRUE
print(astring.endswith("asdfasdfasdf")) # boolean operation:   FALSE

# Lesson 9
print("Lesson 9")
afewwords = astring2.split(" ")
print(afewwords)    # splits Strings into a list of Strings.
'''

# EXERCISE
s = "Strings are awesome!"

# Length should be 20
print("Length of s = %d" % len(s))

# First occurence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("The number of a's should be %d" % s.count("a"))

# Clicing the string into bits
print("The first 5 characters are: %s" % s[:5])    # Start to 5
print("Characters 5 to 10 are: %s" % s[5:10])      # 5 to 10
print("Characters number 12 is: %s" % s[12])       # Just number 12
print("The last five characters are: %s" % s[-5:])
print("The characters with odd index are %s" % s[1::2])# (0-based indexing)

# Convert everything to UPPER & lower case
print(s.upper())
print(s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")    
    
# Check how a string ends
if s.endswith("some!"):
    print("String ends with 'some!'")
    
# Split the string into three seperate strings,
# each containing only a word
print("Split the words of th string: %s" % s.split(" "))
