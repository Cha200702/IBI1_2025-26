import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print("The third and fourth columns (the year and the DALYs) for the first 10 rows:")
print(dalys_data.iloc[0:10,2:5])
# iloc[] is used to select rows and columns by inputting numbers.
  # "0:10" means that we want to select the first 10 rows (from index 0 to index 9)
  # "2:5" means that we want to select the columns from index 2 to index 4 (the column with index 5 is not included).

# The year 1998 reported the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistan.

print ("All years for which DALYs were recorded in Zimbabwe:")
# Create an empty Boolean list
result = [] 
Booleans = dalys_data.iloc[:,0]
for i in range(len(Booleans)):
    # Check if the value in the "Entity" column (which is the first column, index 0) is "Zimbabwe"
    if Booleans [i] == "Zimbabwe":
      # If it is, add the corresponding year (which is in the "Year" column, index 2) to the result list
      result.append(str(dalys_data.loc[i,"Year"]))
      # loc() is used to select rows and columns by inputting labels.
print(",".join(result)) # join() is used to concatenate the elements in the result list into a single string, with a comma and a space as the separator.

# The first and last year for which these data were recorded are respectively 1990 and 2019.

recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
max = recent_data.loc[recent_data['DALYs'].idxmax(), 'Entity'] # idxmax() returns the index of the maximum value in the "DALYs" column
print(f"The country with the highest DALYs in 2019 is {max}.")
# The country with the highest DALYs in 2019 is Lesotho.
min = recent_data.loc[recent_data['DALYs'].idxmin(), 'Entity']
print(f"The country with the lowest DALYs in 2019 is {min}.")
# The country with the lowest DALYs in 2019 is Singapore.

Singapore = dalys_data.loc[dalys_data.Entity == "Singapore", ["Year", "DALYs"]]
plt.figure (figsize =(8,5),dpi=150)
plt.plot(Singapore.Year, Singapore.DALYs, 'ro') # "ro": "r" means red color and "o" means circle marker.
plt.xlabel("Year", fontsize = 12)
plt.ylabel("Yearly DALYs", fontsize = 12)
plt.title("The DALYs over time in Singapore", fontsize = 14)
plt.xticks(Singapore.Year,rotation=-90)
plt.tight_layout() # tight_layout() is used to prevent the labels from being cut off.
plt.show()

China = dalys_data.loc[dalys_data.Entity == "China", ["Year", "DALYs"]]
United_Kingdom = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["Year", "DALYs"]]
plt.figure (figsize =(8,5),dpi=150)
plt.plot(China.Year, China.DALYs, 'bo', label = "China")
plt.plot(United_Kingdom.Year, United_Kingdom.DALYs, 'r+', label = "United Kingdom")
plt.xlabel("Year", fontsize = 12)
plt.ylabel("Yearly DALYs", fontsize = 12)
plt.title("The DALYs over time in China and United Kingdom", fontsize = 14)
plt.legend(fontsize = 12) # legend() needs "label=" in the plot() part in order to work.
plt.tight_layout() 
plt.show()