# pandas: popular python library for data analysis and manipulation
# provides high-performance, easy-to-use data structures and data analysis tools 

# core data structrues:
# series: a 1D array like object containing a sequence of values and an associated index
# dataframe: 2d labeled data structure with columns that can hold different data types 


import pandas as pd

# creating a series
series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# basic operations
print(df.head()) # print first 5 rows
print(df.tail()) # print last 5 rows
print(df.shape)  # print number of rows and columns
print(df.info())  # print info about the dataframe
print(df.describe())  # print summary stats

# data manipulation

# selecting columns
print(df['Name'])
print(df[['Name', 'Age']])

# selecting rows
print(df.iloc[0]) # select first row
print(df.loc['Alice'])    # select row with index alice 

# filtering data
print(df[df['Age'] > 25])

# sorting data
print(df.sort_values(by='Age'))

# grouping and aggregating data
print(df.groupby('City')['Age'].mean())

# data visualization

import matplotlib.pyplot as plt
# create a simple plot
df.plot(kind='bar', x='Name', y='age')
plt.show()
