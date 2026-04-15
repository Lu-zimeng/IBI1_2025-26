import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#Define basic variables
N=10000
beta=0.3
gamma=0.05
#create an array to store the different vaccination rates
vaccination_rates=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
#set up loop for different vaccination rates
for idx,rate in enumerate(vaccination_rates):
    vaccinated=int(N*rate)
    Infected=1
    Recovered=0
    Susceptible=N-vaccinated-Infected
    Infected_list=[1]
    #set up time loop
    for i in range(1000):
        infection_probability=beta*Infected/N
        if Susceptible>0:
            new_infected=np.random.choice(range(2),Susceptible,p=[1-infection_probability,infection_probability]).sum()
        else:
            new_infected=0
        if Infected>0:
            new_recovered=np.random.choice(range(2),Infected,p=[1-gamma,gamma]).sum()
        else:
            new_recovered=0

        Susceptible=Susceptible-new_infected
        Infected=Infected+new_infected-new_recovered
        Recovered=Recovered+new_recovered

    
        Infected_list.append(Infected)
    #draw the plot with nice color
    norm_idx = idx / (len(vaccination_rates) - 1)
    plt.plot(Infected_list, label=f'{int(rate*100)}%', color=cm.viridis(norm_idx))


plt.xlabel('Time')
plt.ylabel('Number of infected people')
plt.title('SIR model with different vaccination rates')
plt.legend(loc='upper right', title='Vaccination rate')
plt.show()
