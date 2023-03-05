# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 09:30:43 2023

@author: UritiSrikanth
"""

#Python script for Visualisation: GDP ::: Line_plot
#Importing necessary Libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Load the data into a DataFrame
df = pd.read_csv("D:\\Datasets\\Dataset\\GDP_Indicators.csv")
print(df)
#Columns
df.columns = ["Country Name", "Country Code", "Series Name", "Series Code", "2012 [2K12]", "2013 [2K13]", "2014 [2K14]", "2015 [2K15]", "2016 [2K16]", "2017 [2K17]", "2018 [2K18]", "2019 [2K19]", "2020 [2K20]", "2021 [2K21]"]
#Line Plot
df.plot(x="Country Code", y=["2012 [2K12]",  "2013 [2K13]", "2014 [2K14]","2015 [2K15]", "2016 [2K16]", "2017 [2K17]", "2018 [2K18]", "2019 [2K19]", "2020 [2K20]", "2021 [2K21]"])
plt.title("GDP and GDP per capita in Ind, UK and USA")
plt.xlabel("Countries")
plt.ylabel("GDP and GDP per capita %")
plt.show()

#Python script for Visualisation: BBC ::: Bar plot & Scatter plot
#Importing necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
def load_dataset():
    df = pd.read_csv("D:\\Datasets\\Dataset\\BBC_UK.csv")
    return df
uk_df = load_dataset()
# Add a column for article length
uk_df['length'] = uk_df['text'].apply(len)
# Bar chart function
def bar_chart():
# Set colors for each category
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    plt.figure(figsize=(8, 6))
    plt.bar(x=uk_df['category'].unique(), height=uk_df.groupby('category').size().values, color=colors)
    plt.xlabel('Category')
    plt.ylabel('Number of articles')
    plt.title('Number of articles by category')
    plt.show()
   # Scatter plot function
def scatter_plot():
       plt.figure(figsize=(8, 6))
       plt.scatter(x='length', y='category', data=uk_df)
       plt.xlabel('Article Length')
       plt.ylabel('Category')
       plt.title('Article Length by Category')
       plt.show()
# Call the functions
bar_chart()
scatter_plot()
