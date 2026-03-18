heart_rates=[72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
total_patients=len(heart_rates)
import numpy as np
mean_heart_rate=np.mean(heart_rates)
print("There are "+ str(total_patients)+" patients in the dataset. The mean heart rate is: "+ str(mean_heart_rate)+" bpm.")

#Group into categories
Low_heart_rate_patients=0
Normal_heart_rate_patients=0
High_heart_rate_patients=0
for i in range(len(heart_rates)):
    if heart_rates[i]<60:
        Low_heart_rate_patients+=1
    elif heart_rates[i]>=60 and heart_rates[i]<=120:
        Normal_heart_rate_patients+=1
    else:
        High_heart_rate_patients+=1

print("The number of low heart rate patients are:" +str(Low_heart_rate_patients))
print("The number of normal heart rate patients are:" +str(Normal_heart_rate_patients))
print("The number of high heart rate patients are:"+str(High_heart_rate_patients))

#Determine the largest
heart_rate_dict={'Low':Low_heart_rate_patients,'Normal':Normal_heart_rate_patients,'High':High_heart_rate_patients}
most=max(heart_rate_dict,key=heart_rate_dict.get)
print(most+" category contains the largest number of patients.")

#create a pie chart
import matplotlib.pyplot as plt

categories = ["Low heart rate", "Normal heart rate", "High heart rate"]
counts = [Low_heart_rate_patients, Normal_heart_rate_patients,High_heart_rate_patients] 

#calculate the percentage of each categories
def autopct_format(pct):
    total = sum(counts)
    patient_num = int(round(pct * total / 100))  
    return f"{pct:.1f}%\n({patient_num} patients)"  

#create the canva
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

#draw the pie chart
wedges, _, autotexts = ax.pie(
    counts,
    autopct=autopct_format,  
    textprops=dict(color="white", weight="bold") 
)

#add legend
ax.legend(
    wedges, categories,
    title="Heart Rate Categories",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

ax.set_title("The distribution of heart rate categories")
plt.tight_layout()
plt.show()