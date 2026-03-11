# What does this piece of code do?
# Answer:

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint
#Imports the randint function to generate random integers within a range

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
#Imports the ceil function to round a number up to the next integer

total_rand = 0
#Initializes a variable to accumulate the sum of all random numbers
progress=0
#Initialzes a counter to track how many times the loop has run
while progress<=10:
	progress+=1 #Increments the counter by 1 each time the loop runs (counts from 1 to 11)
	n = randint(1,10) #Generates a random integer between 1 and 10 and stores it in variable n
	total_rand+=n #Adds the newly generated random number to the total sum

print(total_rand) #Prints the final accumulated sum of all 10 random numbers

