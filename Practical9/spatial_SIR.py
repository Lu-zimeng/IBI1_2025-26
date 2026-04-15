#import necessay libraries
import numpy as np
import matplotlib.pyplot as plt
#make an array of all susceptible population
population=np.zeros((100,100))
#define basic variables
beta=0.3
gamma=0.05
#randomly select the outbreak point
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
#prepare the heat map
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
#set up time loop
for i in range(100):
    # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for j in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][j]
        y = infectedIndex[1][j]
        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
            # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    #determine the recover population
    #>find all coordinates of the infected population
    #>use random.choice to determine whether they will recover
    #>if recover, change the value to 2 in the heat map
    infected_pos=np.where(population==1)
    for e in range(len(infected_pos[0])):
        x_r = infected_pos[0][e]
        y_r = infected_pos[1][e]
        recover = np.random.choice(range(2), 1, p=[1-gamma, gamma])[0]
        if recover == 1:
            population[x_r, y_r] = 2
    #draw heat map for each time point
    if i == 9 or i == 49 or i == 99:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Time {i+1}")
        plt.show()
