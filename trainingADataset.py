# pandas; often used as a precursor to mahcine learning model training
# example of how to use Pandas to prepare a dataset for a machine learning model

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load data
data = pd.read_csv('data.csv')

# explore data
print(data.head())
print(data.info())
print(data.describe())

# handle missing values if any
data.fillna(method='ffill', inplace=True)

# feature engineering if needed
data['new_feature'] = data['feature1'] * data['feature2']

# split data into features (X) and target variable (y)
X = data[['feature1', 'feature2', 'new_feature']]
y = data['target']

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create and train machine learning model
model = LinearRegression()
model.fit(X_train, y_train)

# make predictions on the test set
y_pred = model.predict(X_test)
