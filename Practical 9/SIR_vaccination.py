# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt
# cm is used to automatically generate evenly distributed colors from the same color palette, with a unified style and easy distinction.
from matplotlib import cm

vac_rate = [0 ,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

plt.figure(figsize=(8, 5), dpi=150)
# cm.viridis()  takes a value between 0 and 1 and returns the corresponding RGBA color value (RGBA: Red-Green-Blue-Alpha)
  # np.linspace(start, end, num) is a numpy function that generates "num" evenly spaced numbers between "start" and "end"
  # 0.1, 0.9: only take the middle 80% of the viridis colormap
  # 0, 1 : banned since they are either too dark or too light 
colors = cm.viridis(np.linspace(0.1, 0.9, len(vac_rate)))

# enumerate() allows to get both the vaccination rate and its corresponding color index at the same time
  # "idx += 1" is omitted here since enumerate() helps to do this in the loop by default
for idx, rate in enumerate(vac_rate):
    # Set values 
    N = 10000
    infected = 1
    # Vaccinated here may not be an integer so int() is needed.
    vaccinated = int(N * rate)
    susceptible = N - vaccinated - infected
    recovered = 0
    beta = 0.3
    gamma = 0.05
    days = 1000
    
    # Create arrays [] for each variable to track their evolution over time
    real_time_infected = []
    real_time_susceptible = []
    real_time_recovered = []

    # Loop through required times
    for day in range(days):
        new_infected = 0
        # Examine each susceptible individual whether he will be infected
        for i in range(susceptible):
            prob_infected = beta * infected / N
            m = np.random.choice(range(2), p=[1-prob_infected, prob_infected])
            if m == 1:
                new_infected += 1
        
        new_recovered = 0
        # Examine each infected individual whether he will be recovered
        for j in range(infected):
            prob_cure = gamma
            n = np.random.choice(range(2), p=[1-prob_cure, prob_cure])
            if n == 1:
                new_recovered += 1
        # Update real-time data
        susceptible -= new_infected
        infected += new_infected - new_recovered
        recovered += new_recovered
        # Add real-time data into arrays using append()
        real_time_susceptible.append(susceptible)
        real_time_infected.append(infected)
        real_time_recovered.append(recovered)

    # Draw the line chart (this needs to be in the loop because 11 lines should all be drawn rather than only one)
    x = range(days)
    y = real_time_infected
    plt.plot(
    real_time_infected, 
    # apply similar colors
    color=colors[idx], 
    linewidth=1.5, 
    alpha=0.9, 
    # Transfer the expression of 0.1 into 10%
      # f"..." is used to insert variables directly into strings
      # ":.0f" formats the number to 0 decimal places
    label=f"{rate*100:.0f}%"
   )

plt.xlabel('Time', fontsize=12)
plt.ylabel('Number of People', fontsize=12)
plt.title('SIR Model With Different Vaccination Rates', fontsize=12)
plt.legend(loc="upper right", fontsize=10, framealpha=0.9)
plt.tight_layout()
plt.show()