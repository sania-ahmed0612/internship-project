# -*- coding: utf-8 -*-
"""
Created on Sun May 15 21:48:59 2022

@author: SANIA FIRDOUS
CR INTERNSHIP PROJECT
PROJECT: BOX OFFICE DATA ANALYSIS
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\SANIA\OneDrive\Desktop\2. Box Office Data Analytics-20220515T100242Z-001\box_office.csv")
data.head
data.head()
data.shape
data.info
data.describe()
data.corr()
data.isnull()
data.isnull().sum()
data.duplicated().sum()


sns.displot(data['revenue'])
sns.displot(np.log1p(data['revenue']))


sns.scatterplot(data['revenue'],data['budget'])
plt.title("relationship b/w flim revenue and flim budget")
plt.show()


data.plot(x='budget' , y='revenue', style='.')
plt.title('relationship b/w film and revenue and flim budget')
plt.xlabel('budget')
plt.ylabel('revenue')
plt.show()

plt.figure(figsize=(10,10))
sns.heatmap(data.corr())
plt.show()


relation=data[['revenue','budget']].corr
sns.heatmap(relation())
plt.show()

data['original_language'].unique()
sns.scatterplot(data['original_language'],data['revenue'],color='darkblue')


sns.scatterplot(data['original_language'],np.log1p(data['revenue']),color='peru')
plt.show()


sns.boxplot(data['original_language'],data['revenue'])
plt.show()


data[data['original_language'] == data['original_language'].max()]
 

plt.subplots(figsize=(10,10))
data.groupby(['original_language'])['revenue'].sum().sort_values(ascending = False).head(20).plot(kind='pie')
plt.title("distribution of languages in flims",fontsize=24)
plt.xlabel('original language',fontsize=18)
plt.ylabel('revenue',fontsize=18)
plt.xticks(rotation=90)
plt.show()















