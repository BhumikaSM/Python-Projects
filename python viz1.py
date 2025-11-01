import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv(r"C:\Users\India\Downloads\archive (1)\summer.csv")
medals_over_time=data.groupby('Year')['Medal'].count().reset_index()
top_countries=data['Country'].value_counts().head(10).reset_index()
top_countries.columns=['Country','Total_Medals']
medal_type=data['Medal'].value_counts().reset_index()
medal_type.columns=['Medal','count']

sns.set_theme(style="whitegrid")

fig = plt.figure(figsize=(12, 8))
fig.subplots_adjust(wspace=2.5, hspace=2.5)

plt.subplot(2,2,1)
sns.lineplot(data=medals_over_time,x='Year',y='Medal')
plt.title('Medals Over Time')
plt.xlabel('Year')
plt.ylabel('Medals')

plt.subplot(2,2,2)
sns.barplot(data=top_countries,y='Country',x='Total_Medals')
plt.title('Total number of medals per country')
plt.xlabel('Total_Medals')
plt.ylabel('Country')

plt.subplot(2,1,2)
sns.barplot(data=medal_type,x='Medal',y='count')
plt.title('Medals Type')
plt.xlabel('Medals Type')
plt.ylabel('count')

plt.tight_layout()
plt.show()