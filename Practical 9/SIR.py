# Import necessary libraries
import numpy as np
import matplotlib . pyplot as plt

# Set values
N = 10000
infected = 1
susceptible = 999
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
  # Create a new variable to record individuals who are newly infected
  new_infected = 0
  # Examine each susceptible individual whether he will be infected
  for i in range(susceptible):
    # Calculate the probability of infection
      prob_infected = beta * infected / N
    # Random choose numbers
      # range(2) = choose from 0 to 2 (not including) [all integers] --> choose either 0 or 1
      # "1" represents choose one number only
      # "p=[a,b]" means "a% will choose 0 while b% will choose 1" (corresponding)
      m = np.random.choice(range(2), 1, p=[1-prob_infected, prob_infected])
      # 0 = not infected   1 = infected
      if m == 1:
          new_infected += 1
  # Create a new variable to record individuals who are newly recovered 
  new_recovered = 0
  # Examine each infected individual whether he will be recovered
  for j in range(infected):
    # Define the probability of being recovered
      prob_cure = gamma
      n = np.random.choice(range(2), p=[1-prob_cure, prob_cure])
      # 0 = not recovered   1 = recovered
      if n == 1:
          new_recovered += 1

  # Update real-time data (this step is really important !!!)    
  susceptible -= new_infected
  infected += new_infected - new_recovered
  recovered += new_recovered

  # Add real-time data into arrays using append()
  real_time_susceptible.append(susceptible)
  real_time_infected.append(infected)
  real_time_recovered.append(recovered)

# Draw the line chart
x = range(days)

# Three lines will be plotted
y1 = real_time_susceptible
y2 = real_time_infected
y3 = real_time_recovered

# Set the size and dpi of the figure
plt.figure (figsize =(8,5),dpi=150)

# Draw each line (include colors, line patterns, linewidth and label)
plt.plot(x, y1, color='blue', linestyle='-', linewidth=1.2, label='Susceptible')
plt.plot(x, y2, color='orange', linestyle='-', linewidth=1.2, label='Infected')
plt.plot(x, y3, color='green', linestyle='-', linewidth=1.2, label='Recovered')

plt.xlabel('Time', fontsize = 12)
plt.ylabel('Number of People', fontsize = 12)

# plt.legend() is used to add legends (Notice: plt.plot(label=...) is needed for this)
plt.legend(fontsize = 12)

plt.title('SIR Model', fontsize = 12)

# Save the figure as .png
plt.savefig ("SIR_Model.png")

plt.show()

# Notice:
# Why new_infected is applied here rather than directly  "infected += 1" (line 20 - line 34):
  # Because SIR model defaults that the states of all individuals are fixed within the same time step.
  # If "infected += 1", then it means when the first one is considered infected, then while the second individual is examining, the probability of infection will change.
  # In this way, the number of infected will be exaggerated. (All state changes should occur at the end of the time step and take effect simultaneously.)