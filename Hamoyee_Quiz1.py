#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.graph_objs as go
from plotly.offline import iplot
sns.set()
pd.options.display.max_columns = 999


# In[5]:


pd.read_csv


# In[9]:


df = pd.read_csv(r"C:\Users\jayap\anaconda3\BPPD\FoodBalanceSheets_E_Africa_NOFLAG.csv", encoding = "latin-1")


# In[10]:


df.size


# In[11]:


df.columns


# In[12]:


df.head()


# In[13]:


import pandas as pd
madagascar_2015 = df[(df['Area'] == 'Madagascar') & (df['Element'] == 'Protein supply quantity (g/capita/day)') & (df['Unit'] == 'g/capita/day') & (df['Y2015'].notna())]

total_protein_supply_2015 = madagascar_2015['Y2015'].sum()

print("Total Protein supply quantity in Madagascar in 2015:", total_protein_supply_2015, "g/capita/day")


# In[16]:


import pandas as pd

relevant_columns = ['Element Code', 'Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']
df_relevant = df[relevant_columns]
correlations = df_relevant.corr()['Element Code'].drop('Element Code')

year_least_correlation = correlations.abs().idxmin()
least_correlation_value = correlations.abs().min()

print("Year with the least correlation with 'Element Code':", year_least_correlation)
print("Least correlation value:", least_correlation_value)


# In[ ]:


import pandas as pd

print(df.columns)


wine_production = df[df['Item'] == 'Wine'].groupby('Element Code')['Value'].sum()

wine_2015_sum = wine_production.loc[2015]
wine_2018_sum = wine_production.loc[2018]

print("Total Wine produced in 2015:", wine_2015_sum)
print("Total Wine produced in 2018:", wine_2018_sum)

print(df.columns)


# In[34]:


import pandas as pd

missing_data_2014 = df['Y2014'].isnull().sum()

total_entries = len(df)

percentage_missing_2014 = (missing_data_2014 / total_entries) * 100

print("Total number of missing data in 2014:", missing_data_2014)
print("Percentage of missing data in 2014: {:.3f}%".format(percentage_missing_2014))


# In[27]:


import pandas as pd

selected_columns = df[['Y2017', 'Area']]

sum_by_area_2017 = selected_columns.groupby('Area')['Y2017'].sum()

area_highest_sum_2017 = sum_by_area_2017.idxmax()
highest_sum_2017 = sum_by_area_2017.max()

print("Area with the highest sum in 2017:", area_highest_sum_2017)
print("Sum in 2017:", highest_sum_2017)


# In[29]:


import pandas as pd

sum_by_year = df.groupby('Element')[['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']].sum()

year_highest_sum = sum_by_year.sum(axis=0).idxmax()
highest_sum = sum_by_year.sum(axis=0).max()

print("Year with the highest sum of stock variation:", year_highest_sum)
print("Highest sum of stock variation:", highest_sum)


# In[30]:


import pandas as pd

total_unique_countries = df['Area'].nunique()

print("Total number of unique countries in the dataset:", total_unique_countries)


# In[31]:


import pandas as pd

sum_by_element_2017 = df.groupby('Element')['Y2017'].sum()

sum_processing_2017 = sum_by_element_2017.get('Processing', 0)  # Get the sum for 'Processing' or default to 0 if not found

print("Total sum of Processing in 2017:", sum_processing_2017)


# In[32]:


import pandas as pd

selected_columns = df[['Y2017', 'Area']]

sum_by_area_2017 = selected_columns.groupby('Area')['Y2017'].sum()

seventh_lowest_sum = sum_by_area_2017.sort_values().iloc[6]

area_seventh_lowest_sum = sum_by_area_2017[sum_by_area_2017 == seventh_lowest_sum].index[0]

print("Area with the 7th lowest sum in 2017:", area_seventh_lowest_sum)
print("7th lowest sum in 2017:", seventh_lowest_sum)


# In[33]:


import pandas as pd

df_2017 = df[['Y2017']]

mean_2017 = df_2017.mean().values[0]
std_dev_2017 = df_2017.std().values[0]

mean_2017 = round(mean_2017, 2)
std_dev_2017 = round(std_dev_2017, 2)

print("Mean for the year 2017:", mean_2017)
print("Standard deviation for the year 2017:", std_dev_2017)


