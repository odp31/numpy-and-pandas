import pandas as pd 

# several methods to load data from various sources:
# 1: CSV
df = pd.read_csv('your_data.csv')

# 2: Excel
df = pd.read_excel('your_data.xlsx')

# 3: JSON
df = pd.read_json('your_data.json')

# display first few rows:
print(df.head())

# display last few rows:
print(df.tail())

# getting info about the dataframe 
print(df.info())

# statistical summary
print(df.describe())

# Data Cleaning and Manipulation

# handling missing values:
df.fillna(value, inplace=True) # fill missing values with a specific value
df.dropna(inplace=True) # drop rows with missing values 

# selecting columns:
selected_columns = df[['column1', 'column2']]

# filtering rows
filtered_df = df[df['column1'] > 10]

# sorting data
sorted_df = df.sort_values(by='column1', ascending=False)

# grouping and aggregating data
grouped_df = df.groupby('category').mean()

