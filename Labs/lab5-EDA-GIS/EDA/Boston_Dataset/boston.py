import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os, sys
# pip install sklearn
import sklearn.datasets
from scipy import stats

currentDirectory = os.getcwd()
print(f'currentDirectory: {currentDirectory}')
os.chdir(currentDirectory + '/GMI28V_IoT/EDA/Boston_Dataset')
workDirectory = os.getcwd()
print(f'workDirectory: {workDirectory}')

# get available seaborn data sets to play with
# print(sns.get_dataset_names())

# available sklearn datasets
# https://scikit-learn.org/stable/datasets/index.html

# https://www.edureka.co/blog/exploratory-data-analysis-in-python/

print('\nLoad the Boston house-prices dataset')
boston = sklearn.datasets.load_boston()
x = boston.data
y = boston.target
columns = boston.feature_names
# creating dataframes
boston_df = pd.DataFrame(boston.data)
boston_df.columns = columns
# describe
print(boston_df.describe())

print('\nEDA')

# Drop NULL or missing values
print(boston_df.shape)
boston_df = boston_df.dropna()
print(boston_df.shape)
# Fill NULL or missing values with 30
boston_df['AGE'] = boston_df['AGE'].fillna(30)
print(boston_df.shape)

# Handling outliers

# BoxPlot:
sns.boxplot(x=boston_df['DIS'])
plt.show()

# Scatterplot:
fig, ax = plt.subplots(figsize=(16, 8))
ax.scatter(boston_df['INDUS'] , boston_df['TAX'])
ax.set_xlabel('proportion of non-retail business acre per town')
ax.set_ylabel('full-value property-tax per $10000')
plt.show()

# Z-score:
z = np.abs(stats.zscore(boston_df))
print(z)
boston_df_outlier_zscore = boston_df[(z<3).all(axis=1)]
print(f'\nZ-shape: {boston_df_outlier_zscore.shape}')

# IQR:
q1 = boston_df.quantile(0.25)
q3 = boston_df.quantile(0.75)
iqr = q3 - q1
print(f'\nIQR:\n {iqr}')

boston_df_outlier_iqr = boston_df[~((boston_df < (q1-1.5*iqr)) |
    (boston_df > (q3 + 1.5 * iqr))).any(axis=1)]

print(f'\nIQR-shape: {boston_df_outlier_iqr.shape}')

# Histogram:
plt.figure(figsize=(4, 3))
plt.hist(boston.target)
plt.xlabel('Price($1000s)')
plt.ylabel('Count')
plt.tight_layout
plt.show()

# HeatMaps:
correlation_matrix = boston_df.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)
plt.show()
