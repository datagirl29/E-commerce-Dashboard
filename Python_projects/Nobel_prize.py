#!/usr/bin/env python
# coding: utf-8

# In[19]:


#package seaborn has used for data visualization, pandas, numpy for data processing and manuipulations.
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set()


# In[20]:


nobel = pd.read_csv("F:/DATA SCIENCE/DATA/archive.csv",parse_dates=True)


# In[21]:


nobel.head(n=2)


# In[22]:


nobel.info()


# In[23]:


#Nobel Prizes by Category from 1901 to 2016
year_cat=nobel.groupby(['Year','Category'])['Laureate ID'].count().reset_index()
year_cat
g = sns.FacetGrid(year_cat, col='Category', hue='Category')
g = g.map(plt.plot, 'Year', 'Laureate ID')


# In[24]:


#  In this section plotting the nobel prize by sex, country and category
sex=nobel['Sex'].value_counts()
sns.barplot(x=sex.index,y=sex.values)
plt.xticks(rotation=90)
plt.title('Nobel Prizes by Sex')
plt.show()


# In[25]:


#Trend in Nobel Prize
year=nobel['Year'].value_counts()

sns.lineplot(x=year.index,y=year.values,color='red')

plt.xticks(rotation=90)
plt.title('Nobel Prizes by Year')
plt.show()


# In[26]:


#Categorywise - Number of Nobel Prizes
cat= nobel['Category'].value_counts()
sns.barplot(x=cat.index,y=cat.values)
plt.xticks(rotation=45)
plt.title('Nobel Prizes by Category')
plt.show()


# In[27]:


#Countrywise - Which Country got the most
ctry=nobel['Birth Country'].value_counts().head(10)
sns.barplot(x=ctry.index,y=ctry.values)
plt.xticks(rotation=90)
plt.title('Top 10 Countries, which got the nobel prizes the most')
plt.show()


# In[28]:


#Distribution of Age of Winners
nobel['Birth Year'] = nobel['Birth Date'].str[0:4] #first four no. of birth date
nobel['Birth Year'] = nobel['Birth Year'].apply(pd.to_numeric) #converting argument to numeric
nobel['Age']=nobel['Year']- nobel['Birth Year']
sns.boxplot(data=nobel,
         x='Category',
         y='Age')

plt.show()


# In[29]:


#Oldest Nobel Prize Winner
old=nobel.nlargest(5,'Age')
display(old[['Category','Full Name','Birth Country','Sex','Age']])


# In[30]:


#Youngest Nobel Prize Winner
young=nobel.nsmallest(5,'Age')
display(young[['Category','Full Name','Birth Country','Sex','Age']])


# In[31]:


# life span calculation
nobel['D Year'] = nobel['Death Date'].str[0:4]
nobel['D Year'] = nobel['D Year'].replace(to_replace="nan", value=0)
nobel['D Year'] = nobel['D Year'].apply(pd.to_numeric)
nobel['lifespan']=nobel['D Year']- nobel['Birth Year']


# In[32]:


#Laureate Types
sns.countplot(nobel['Laureate Type'])
plt.show()


# In[33]:


#Organization Toppers
#Plotting the top organization , which won the nobel prize the most.

org = nobel['Organization Name'].value_counts().reset_index().head(20)

sns.barplot(x='Organization Name',y='index',data=org)
plt.xticks(rotation=90)
plt.ylabel('Organization Name')
plt.xlabel('Count')
plt.show()


# In[ ]:




