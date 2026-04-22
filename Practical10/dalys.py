#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read the content of the csv. file
dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")
#show the third and fourth colunms for the first 10 rows
print(dalys_data.iloc[0:10,2:4])
#what year reported the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistan
Afghanistan_data=dalys_data.loc[dalys_data.Entity=='Afghanistan']
Afghanistan_data_10=Afghanistan_data.head(10)
maximum_dalys=Afghanistan_data_10['DALYs'].max()
max_row_index=Afghanistan_data_10['DALYs'].idxmax()
max_year=Afghanistan_data_10.loc[max_row_index, 'Year']
print(str(max_year)+' reported the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistan.')

#find every row where entity is Zimbabwe
# > use a list to store the Boolean result
# > if entity==Zimbabwe, append True to the list
# > else store False to the list
# > then use iloc to print the result
# > print the first and last year of the data
entity_judge_list=[]
for i in dalys_data['Entity']:
    if i=="Zimbabwe":
        entity_judge_list.append(True)
    else:
        entity_judge_list.append(False)
Zimbabwe_data=dalys_data.iloc[entity_judge_list,:]
first_year=Zimbabwe_data['Year'].iloc[0]
last_year=Zimbabwe_data['Year'].iloc[-1]
print(Zimbabwe_data)
print('The first year and the last year for which these data were recorded are '+str(first_year)+' and '+str(last_year)+' respectively.')

#computed the countries with the maximum and minimum DALYs in 2019
# > store only the data from 2019
# > find the maximum and minimum DALYs
recent_data=dalys_data.loc[dalys_data.Year==2019,["Entity","DALYs"]]
maximum_dalys_2019=recent_data['DALYs'].max()
max_index_2019=recent_data['DALYs'].idxmax()
max_country=recent_data.loc[max_index_2019,'Entity']

minimum_dalys_2019=recent_data['DALYs'].min()
min_index_2019=recent_data['DALYs'].idxmin()
min_country=recent_data.loc[min_index_2019,'Entity']

print('The country with the maximum DALYs in 2019 is '+ max_country+'.')
print('The country with the minimum DALYs in 2019 is '+ min_country+'.')

#draw a plot showing the DALYs over time
# > store the dalys data of the country with the maximum DALYs
# > then draw a plot using the Year and DALYs of that country
max_country_data=dalys_data.loc[dalys_data.Entity==max_country]
plt.plot(max_country_data.Year,max_country_data.DALYs,'ro')
plt.xticks(max_country_data.Year,rotation=-90)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs over Time in '+max_country+' (1990-2019)')
plt.show()

#Answering the question : the relationship between the DALYs in China and UK
# > store all the data where entity is China and UK
China=dalys_data.loc[dalys_data.Entity=='China',['Year','DALYs']]
uk=dalys_data.loc[dalys_data.Entity=='United Kingdom',['Year','DALYs']]
# > store the data from dataframe into a list
China_dalys_list=China['DALYs']
UK_dalys_list=uk['DALYs']
# > use 'for' to calculate the difference in different years
difference_list=[]
for China_dalys,uk_dalys in zip(China_dalys_list,UK_dalys_list):
    difference=China_dalys-uk_dalys
    difference_list.append(difference)
# > calculate the mean difference of first 15 years and last 15 years respectively
mean_1990_2005=np.mean(difference_list[0:15])
mean_2005_2019=np.mean(difference_list[15:])
print('The mean difference between DALYs in China and the UK during 1990 to 2005 is '+str(mean_1990_2005))
print('The mean difference between DALYs in China and the UK during 2005 to 2019 is '+str(mean_2005_2019))
# > determine the relationship
if mean_1990_2005>mean_2005_2019:
    print('They are becoming similar.')
else:
    print('They are becoming less similar.')

