import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load data
df = pd.read_csv('sales_data.csv')

# clean and preprocess data
df.fillna(method='ffill', inplace=True)
df['Date'] = pd.to_datetime(df['Date'])

# group data by product category and calculate sales
grouped_df = df.groupby('Product_Category').sum()

# visualize sales by category
plt.figure(figsize=(10,6))
sns.barplot(x=grouped_df.index, y='Sales', data=grouped_df)
plt.title('sales by product category')
plt.show()

# time series analysis
df.set_index('Date', inplace=True)
monthly_sales = df.resample('M').sum()
monthly_sales.plot()
plt.title('monthly sales')
plt.show()
