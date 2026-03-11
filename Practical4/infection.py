#Define constant variables
#total student=91
#initial infected students=5
#daily growth rate=0.4
#Initialize simulation variables
#current infected=initial infected
#days passed=o
#Start simulation loop
	#Display the current day and current number of infected students
	#Calculate new infections for the next day
	#next infected=current infected*(1+daily growth rate)
	#update current infected to next infected
	#add day passed by 1
#End while
#Print final results


initial_infected=5 	#Define constant:initial number of infected students
growth_rate=0.4 	#Define constant: daily infection growth rate (40%)
total_students=91	#Define constant: total number of students in the class
infected=initial_infected #Initialize simulation variable: current infected = initial infected
day=0 #Initialize simulation variable: days passed
print("Day infected students")

#Start simulation loop: run until all students are infected
while infected<total_students:
	print(f"{day:2d} {infected:.1f}")	#Print current day and infected count
	infected=infected*(1+growth_rate)	#Calculate infected count for the next day
	day+=1		#Increment day counter by 1

#print the results
print(f"{day:2d} {infected:.1f}")
print(f"\nAll {total_students} students are infected after {day} days.")
