# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt

N = 10000
infected = 1
susceptible = 999
recovered = 0
beta = 0.3
gamma = 0.05
days = 1000

real_time_infected = []
real_time_susceptible = []
real_time_recovered = []

for day in range(days):

  new_infected = 0
  for i in range(susceptible):
      prob_infected = beta * infected / N
      m = np.random.choice(range(2), p=[1-prob_infected, prob_infected])
      if m == 1:
          new_infected += 1
   
  new_recovered = 0
  for j in range(infected):
      prob_cure = gamma
      n = np.random.choice(range(2), p=[1-prob_cure, prob_cure])
      if n == 1:
          new_recovered += 1
        
  susceptible -= new_infected
  infected += new_infected - new_recovered
  recovered += new_recovered

  real_time_susceptible.append(susceptible)
  real_time_infected.append(infected)
  real_time_recovered.append(recovered)

x = range(days)
y1 = real_time_susceptible
y2 = real_time_infected
y3 = real_time_recovered
plt.figure (figsize =(8,5),dpi=150)
plt.plot(x, y1, color='blue', linestyle='-', linewidth=1.2, label='Susceptible')
plt.plot(x, y2, color='orange', linestyle='-', linewidth=1.2, label='Infected')
plt.plot(x, y3, color='green', linestyle='-', linewidth=1.2, label='Recovered')
plt.xlabel('Time', fontsize = 12)
plt.ylabel('Number of People', fontsize = 12)
plt.legend(fontsize = 12)
plt.title('SIR Model', fontsize = 12)
plt.savefig ("SIR_Model.png")
plt.show()