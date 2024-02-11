# CH 12. Pandas Basics
print("CH 12. Pandas Basics")

import pandas as pd



# Lesson 1
print("\nLESSON 1")


dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

brics = pd.DataFrame(dict)
print(brics)


# LESSON 2 - Index Data Frame
print("\nLESSON 2")
# set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# print out brics with new index values
print(brics)

# LESSON 3 - .csv file imports
print("\nLESSON 3")
 # Import the cars.csv('cars.csv')
cars = pd.read_csv("./scripts/cars.csv", index_col = 0)
print(cars)
# print out cars


# LESSON 4 - Indexing DataFrames
print("\nLESSON 4")

# Print out country column as Pandas *Series*
print(cars["country"])

# Print out country column as Pandas *DataFrame*
print(cars[["country"]])

# Print out DataFrame with country and drives_right columns
print(cars[["country","drives_right"]])

# Print out first 4 observations
print(cars[0:4])

# Print out fifth and sixth observation
print(cars[4:6])


# LESSON 5 - loc & iloc features
print("\nLESSON 5")

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])
print(cars.loc[['AUS', 'EG'], ['country', 'drives_right']])
print(cars.loc[['AUS', 'EG'], "drives_right"])

