import numpy as np
import matplotlib.pyplot as plt
#Define basic variables
Susceptible=9999
Infected=1
Recovered=0
N=10000
beta=0.3
gamma=0.05
#create arrays for each variables to track how they evolve over time
Susceptible_list=[9999]
Infected_list=[1]
Recovered_list=[0]
#Set up the loop
#>define the infection probability
#>use random.choice to determine the number of infected and recovered number
#>use .sum() to sum up all the 1 in the random list which means the total number of new infected/recovered
#>add the change to the list(append)
for i in range(1000):
    infection_probability=beta*Infected/N
    new_infected=np.random.choice(range(2),Susceptible,p=[1-infection_probability,infection_probability]).sum()
    new_recovered=np.random.choice(range(2),Infected,p=[1-gamma,gamma]).sum()

    Susceptible=Susceptible-new_infected
    Infected=Infected+new_infected-new_recovered
    Recovered=Recovered+new_recovered

    Susceptible_list.append(Susceptible)
    Infected_list.append(Infected)
    Recovered_list.append(Recovered)

#draw the plot
plt.figure(figsize=(6,4),dpi=150)
plt.plot(Susceptible_list, label='Susceptible')
plt.plot(Infected_list, label='Infected')
plt.plot(Recovered_list, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model')
plt.legend()
plt.savefig("SIR_model_figure.png",dpi=150)
plt.show()

