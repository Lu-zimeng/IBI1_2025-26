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
initial_infected=5
growth_rate=0.4
total_students=91
infected=initial_infected
day=0
print("Day infected students")
while infected<total_students:
	print(f"{day:2d} {infected:.1f}")
	infected=infected*(1+growth_rate)
	day+=1
print(f"{day:2d} {infected:.1f}")
print(f"\nAll {total_students} students are infected after {day} days.")
