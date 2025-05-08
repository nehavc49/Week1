import pandas as pd

data = {
    'Date': pd.date_range(start='2024-01-01', periods=4, freq='D'),
    'Region': ['North', 'South', 'East', 'West'],
    'Product': ['A', 'B', 'C', 'A'],
    'Quantity': [10, 15, 5, 8],
    'Unit Price': [100, 200, 150, 100]
}

df = pd.DataFrame(data)
df['Total'] = df['Quantity'] * df['Unit Price']
df.to_csv('sales_data.csv', index=False)

print("CSV file created.")

