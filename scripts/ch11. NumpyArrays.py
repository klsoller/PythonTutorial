# CH 11. Numpy Arrays

import numpy as np


'''
# LESSON 1
print("\nLESSON 1")

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

print(type(height))
print(height)   # python LISTS: Seperated by commas
print(weight)   

# Create 2 numpy arrays from height and weight
np_height = np.array(height)    
np_weight = np.array(weight)

print(type(np_height))
print(np_height)    # numpy ARRAY, seperate by spaces.
print(np_weight)

# LESSON 2 - Element-wise calculations
print("\nLESSON 2")
bmi = np_weight / np_height ** 2

# print the result
print(bmi)

# LESSON 3 - Subsetting
print("\nLESSON 3")
# for a boolean response:
print(bmi)
print(bmi > 25)
print(bmi)
print(bmi[bmi > 25])
print(bmi)
'''


# EXERCISE
print("\nEXERCISE")
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Create a numpy array np_weight_kg from weight_kg

np_weight_kg = np.array(weight_kg)
    


# Create np_weight_lbs from np_weight_kg
kg_lbs_conv = 2.20462
np_weight_lbs = np_weight_kg * kg_lbs_conv


# Print out np_weight_lbs

print("weight %s" % np_weight_lbs)

