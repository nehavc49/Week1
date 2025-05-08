import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Select the numeric columns you want to analyze (e.g., Quantity and Total)
quantity = df['Quantity'].values
total = df['Total'].values

print("🔢 Quantity Stats:")
print("Mean:", np.mean(quantity))
print("Median:", np.median(quantity))
print("Standard Deviation:", np.std(quantity))
print()

print("💰 Total Sales Stats:")
print("Mean:", np.mean(total))
print("Median:", np.median(total))
print("Standard Deviation:", np.std(total))
