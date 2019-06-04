# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data = pd.read_csv(path)
data.rename(columns={'Total': 'Total_Medals'}, inplace=True)
print(data.head(10))
#Code starts here



# --------------
#Code starts here




data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'], 'Summer',np.where(data['Total_Summer']==data['Total_Winter'], 'Both','Winter'))
valueCount = data['Better_Event'].value_counts()
better_event = np.where(valueCount['Summer']>valueCount['Winter'], 'Summer','Winter')
print(valueCount['Summer'])
better_event = 'Summer'


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries.iloc[0:-1,:]
def top_ten(df, column):
     country_list = []
     country_list = list(df.nlargest(10, column)['Country_Name'])
     return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))



# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
summer_df.groupby(['Country_Name', 'Total_Summer']).size().unstack().plot(kind='bar')
winter_df.groupby(['Country_Name', 'Total_Winter']).size().unstack().plot(kind='bar')
top_df.groupby(['Country_Name', 'Total_Medals']).size().unstack().plot(kind='bar')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
maxSummer = summer_df[summer_df['Golden_Ratio']==summer_df['Golden_Ratio'].max()]
summer_max_ratio = float("{0:.2f}".format(maxSummer.iloc[0]['Golden_Ratio']))
summer_country_gold = maxSummer.iloc[0]['Country_Name']
#Code starts here
winter_df['Golden_Ratio'] = summer_df['Gold_Winter']/summer_df['Total_Winter']
maxWinter = winter_df[winter_df['Golden_Ratio']==winter_df['Golden_Ratio'].max()]
winter_max_ratio = float("{0:.2f}".format(maxWinter.iloc[0]['Golden_Ratio']))
winter_country_gold = maxWinter.iloc[0]['Country_Name']

#Code starts here
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
maxTop = top_df[top_df['Golden_Ratio']==top_df['Golden_Ratio'].max()]
top_max_ratio = float("{0:.2f}".format(maxTop.iloc[0]['Golden_Ratio']))
top_country_gold = maxTop.iloc[0]['Country_Name']


# --------------





#Code starts here
data_1 = data.drop(data.tail(1).index) 
print(data_1)
data_1['Total_Points'] = ((3*data_1['Gold_Total']) + (2*data_1['Silver_Total']) + (data_1['Bronze_Total']))

#Code starts here
maxTop = data_1[data_1['Total_Points']==data_1['Total_Points'].max()]
most_points = float("{0:.2f}".format(maxTop.iloc[0]['Total_Points']))
best_country = maxTop.iloc[0]['Country_Name']


# --------------
#Code starts here
best = data[(data['Country_Name'] == best_country)][['Gold_Total','Silver_Total','Bronze_Total']]
print(best)
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation='45')


