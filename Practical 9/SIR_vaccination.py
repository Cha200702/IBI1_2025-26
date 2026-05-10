# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt
from matplotlib import cm

vac_rate = [0 ,0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

plt.figure(figsize=(8, 5), dpi=150)
colors = cm.viridis(np.linspace(0.1, 0.9, len(vac_rate)))

for idx, rate in enumerate(vac_rate):
    N = 10000
    infected = 1
    vaccinated = int(N * rate)
    susceptible = N - vaccinated
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
    y = real_time_infected
    plt.plot(
    real_time_infected, 
    color=colors[idx], 
    linewidth=1.5, 
    alpha=0.9, 
    label=f"{rate*100:.0f}%"
   )

plt.xlabel('Time', fontsize=12)
plt.ylabel('Number of People', fontsize=12)
plt.title('SIR Model With Different Vaccination Rates', fontsize=12)
plt.legend(loc="upper right", fontsize=10, framealpha=0.9)
plt.tight_layout()
plt.show()