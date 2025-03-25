import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
# Load Iris dataset from seaborn (built-in)
df = sns.load_dataset('iris')

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Check data types and missing values
print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
# Basic statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())

# Group by species and calculate mean sepal length
print("\nMean sepal length by species:")
print(df.groupby('species')['sepal_length'].mean())

# Task 3: Data Visualization
plt.figure(figsize=(15, 10))

# 1. Line chart (example: sepal length by row index)
plt.subplot(2, 2, 1)
plt.plot(df['sepal_length'], color='green')
plt.title('Sepal Length Trend')
plt.xlabel('Row Index')
plt.ylabel('Sepal Length (cm)')

# 2. Bar chart (mean sepal length by species)
plt.subplot(2, 2, 2)
df.groupby('species')['sepal_length'].mean().plot(kind='bar', color=['red', 'blue', 'green'])
plt.title('Mean Sepal Length by Species')
plt.ylabel('Length (cm)')

# 3. Histogram (distribution of petal length)
plt.subplot(2, 2, 3)
plt.hist(df['petal_length'], bins=15, color='purple', edgecolor='black')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')

# 4. Scatter plot (sepal length vs petal length)
plt.subplot(2, 2, 4)
plt.scatter(df['sepal_length'], df['petal_length'], color='orange', alpha=0.6)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')

plt.tight_layout()  # Prevent overlapping
plt.show()
