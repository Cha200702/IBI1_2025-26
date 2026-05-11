# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Make array of all susceptible population
population = np.zeros((100, 100))
# Randomly pick two numbers from 1 to 100 (not including) --> for example, here we assume the two are 23 and 42
outbreak = np.random.choice(range(100),2)
# --> outbreak[0] = 23 ; outbreak[1] = 42 ; then in 2D figure, the point (23,42) is converted from 0 to 1
population [outbreak[0],outbreak[1]] = 1

plt.figure(figsize=(6,4) , dpi = 150)
# plt.imshow() loops through every point in this array and colors it according to the value in the point.
  # population is the data source
  # cmap = 'viridis' : "cmap" stands for color map and "viridis" is the default color map officially recommended by matplotlib, a smooth gradient from dark purple → teal → bright yellow.
  # "interpolation" determines how the edges between points are handled when the image is scaled up or down
  # "nearest" means nearest-neighbor interpolation. The effect is: each point retains its solid color, with sharp, clear edges and no blurring.
plt.imshow(population, cmap = 'viridis', interpolation = 'nearest')
plt.title('t = 0')
# plt.pause() means each image stays for 0.5 seconds
plt.pause(0.5)

# Set values
N = 10000
infected = 1
susceptible = 999
recovered = 0
beta = 0.3
gamma = 0.05
days = 100

# Loop through all time points
for t in range(days):
    # Create a completely independent copy of the population array
    current = population.copy()
    # np.where() is used to find all infected individuals
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
      # get x, y coordinates for each point
      x = infectedIndex[0][i]
      y = infectedIndex[1][i]
      # infect each neighbour with probability beta
      # infect all 8 neighbours
      for xNeighbour in range(x-1,x+2):
        for yNeighbour in range(y-1,y+2):
            # avoid infecting the infected himself
            if (xNeighbour,yNeighbour) != (x,y):
                # make sure do not fall off an edge
                if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected
                    if population[xNeighbour,yNeighbour]==0:
                        population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
                        # np.random.choice() returns a 1D array like (1) and [0] is used to extract the number 0.

    current = population.copy()
    # find infected points
    infectedIndex = np.where(population == 1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
         # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # examine whether each individual is recovered or not
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]

    # plt.clf() is used to completely erase all content from the current matplotlib figure
    plt.clf()  
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f't = {t+1}')  
    plt.pause(0.1)  

plt.show()