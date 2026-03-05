import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

HouseDF = pd.read_csv(r'F:\Pandas Learning Journey\USA_Housing.csv')

print("First 5 rows of the dataset:")
print(HouseDF.head())

print("\nDataset Information:")
print(HouseDF.info())

print("\nColumn names in the dataset:")
print(HouseDF.columns)

sns.pairplot(HouseDF)
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(HouseDF.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

