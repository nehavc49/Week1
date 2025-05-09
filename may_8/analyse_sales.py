import pandas as pd
import numpy as np

# 1. Load the CSV file
df = pd.read_csv('sales_data.csv')

# 2. Show first 5 rows
print(" HEAD:\n", df.head(), "\n")

# 3. Check for missing values
print("MISSING VALUES:\n", df.isnull().sum(), "\n")

# 4. Summary statistics
print(" SUMMARY STATS:\n", df.describe(), "\n")

# 5. Total sales by Region
print(" SALES BY REGION:\n", df.groupby('Region')['Total'].sum(), "\n")

# 6. Filter sales > 2000
print(" SALES > 2000:\n", df[df['Total'] > 2000], "\n")

# 7. Apply 10% discount if Quantity > 10
df['Discount'] = np.where(df['Quantity'] > 10, df['Total'] * 0.10, 0)
print(" DISCOUNTS:\n", df[['Product', 'Quantity', 'Total', 'Discount']], "\n")

# 8. Create a pivot table for sales by Region and Product
print(" PIVOT TABLE:\n", pd.pivot_table(df, values='Total', index='Region', columns='Product', aggfunc='sum', fill_value=0), "\n")
