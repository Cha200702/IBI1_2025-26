# Set the initial number of infected students
initial_infected = 2
# Set the growth rate over 24 hrs
growth_rate = 0.5
# Set the number of all students
total_students = 91
# Set the day counter
day = 1

# Simulate the infection spread until all students are infected

import math 
  # "math" is imported to use the "ceil" function for rounding up the number of infected students

# Use a while loop to continue until all students are infected
while initial_infected < total_students:
    print(f'Day {day}, there are {initial_infected} infected students in total.')
    initial_infected += growth_rate * initial_infected
    initial_infected = math.ceil(initial_infected)  
      # "math.ceil" is used to round up to the nearest whole number of infected students
    day += 1

# Once the loop ends, it means all students are infected
print(f'On day {day}, all students are infected.')