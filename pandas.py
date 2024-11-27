# popular python library for data analysis and manipulation
# provides high-performance, easy-to-ues data structures and data analysis tools 

# core data structures:
# 1; series- a 1D array like object containing an array of data and an associated array of labels called an index
# 2; dataframe- a 2d labeled data structrue with columns that can hold different data types 

import pandas as pd

# create a series
series = pd.Series([1, 2, 3, 4, 5])

# create a dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# display first 5 rows
print(df.head())
# get info about data frame
print(df.info())
# statistical summary 
print(df.describe())


# 1; data manipulation
# selecting columns
print(df['Name'])
# selecting rows
print(df.iloc[1]) # select second row
# filtering data
filtered_df = df[df['Age'] > 25]
print(filtered_df)
# sorting data
sorted_df = df.sort_values(by='Age')
print(sorted_df)



#2; data cleaning and preparation
# handling missing values
df.fillna(0, inplace=True) #fill missing values with 0
# removing duplicates
df.drop_duplicates(inplace=True)
# converting data types 
df['Age'] = df['Age'].astype('float')


# 3; data visualization
import matplotlib.pyplot as plt
# create a simple plot
df.plot(kind='bar', x='Name', y='Age')
plt.show()
