#calculate the percent change of each country
pop2020 = {'UK':66.7,'China':1426,'Italy':59.4,'Brazil':208.6,'USA':331.6}
pop2024 = {'UK':69.2,'China':1410,'Italy':58.9,'Brazil':212.0,'USA':340.1}

#put the percent change into a list
pop_changes=[]
for country in pop2020:
    change = (pop2024[country] - pop2020[country]) * 100 / pop2020[country]
    print("The percentage population change for " + country + " is " + str(change))
    pop_changes.append([country,change])
#print the population change in the descending order
pop_changes_sorted = sorted(pop_changes, key=lambda x: x[1], reverse=True)

print("Population change rates (descending order):")
for country, change in pop_changes_sorted:
    print(country + ": " + str(round(change, 2)) + "%")

#identify the countries with the largest increase and the largest decrease
largest_increase = pop_changes_sorted[0]  
largest_decrease = pop_changes_sorted[-1] 


print("Country with the largest increase: " + largest_increase[0])
print("Country with the largest decrease: " + largest_decrease[0])
#draw the bar chart
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

countries = ['UK', 'China', 'Italy', 'Brazil','USA']
change = [item[1] for item in pop_changes_sorted]
bar_labels = ['UK', 'China', 'Italy', 'Brazil','USA']
bar_colors = ['tab:red', 'tab:blue', 'tab:purple', 'tab:orange','olive']

bars=ax.bar(countries, change, label=bar_labels, color=bar_colors)

ax.set_ylabel('Population percent change')
ax.set_title('The population percent change of 5 countries')
ax.set_xlabel('Country name')
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5) #add the 0 line
ax.legend(title='countries')
#show value of every bar
for bar in bars:
    height = bar.get_height()
    # calculate the location of the label
    if height > 0:
        # chart above 0: put the label at 80% height of the chart
        y_pos = height * 0.8
        va = 'center'
    else:
        # chart below 0
        y_pos = height * 0.8
        va = 'center'
    
    plt.text(
        bar.get_x() + bar.get_width()/2.,  
        y_pos,                          
        f"{height:.2f}%",                
        ha='center', va=va,              
        color='white',                   
        fontweight='bold',               
        fontsize=10                      
    )
plt.show()