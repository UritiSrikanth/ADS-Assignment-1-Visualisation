#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Python script for Visualisation: GDP ::: Line_plot
#Importing necessary Libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[14]:


# Load the data into a DataFrame
df = pd.read_csv("D:\\Datasets\\Dataset\\GDP_Indicators.csv")
df


# In[15]:


#Columns
df.columns = ["Country Name", "Country Code", "Series Name", "Series Code", "2012 [2K12]", "2013 [2K13]", "2014 [2K14]", "2015 [2K15]", "2016 [2K16]", "2017 [2K17]", "2018 [2K18]", "2019 [2K19]", "2020 [2K20]", "2021 [2K21]"]


# In[16]:


#Line Plot
df.plot(x="Country Code", y=["2012 [2K12]",  "2013 [2K13]", "2014 [2K14]","2015 [2K15]", "2016 [2K16]", "2017 [2K17]", "2018 [2K18]", "2019 [2K19]", "2020 [2K20]", "2021 [2K21]"])
plt.title("GDP and GDP per capita in Ind, UK and USA")
plt.xlabel("Countries")
plt.ylabel("GDP and GDP per capita %")
plt.show()


# In[17]:


#Importing necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[18]:


#Load the dataset
def load_dataset():
    df = pd.read_csv("D:\\Datasets\\Dataset\\BBC_UK.csv")
    return df
uk_df = load_dataset()


# In[19]:


# Add a column for article length
uk_df['length'] = uk_df['text'].apply(len)
uk_df


# In[20]:


# Bar chart # Scatter plot
def bar_chart():
    plt.figure(figsize=(8, 6))
    sns.countplot(data=uk_df, x='category')
    plt.xlabel('Category')
    plt.ylabel('Number of articles')
    plt.title('Number of articles by category')
    plt.show()


def scatter_plot():
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=uk_df, x='length', y='category')
    plt.xlabel('Article Length')
    plt.ylabel('Category')
    plt.title('Article Length by Category')
    plt.show()


# In[21]:


# Call the functions
bar_chart()
scatter_plot()


# In[ ]:




