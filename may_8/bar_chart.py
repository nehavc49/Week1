import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('sales_data.csv')

# Bar chart for Total Sales by Region
plt.figure(figsize=(10, 6))
df.groupby('Region')['Total'].sum().plot(kind='bar', color='skyblue')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.savefig('total_sales_by_region.png')  # Save the plot as a PNG file
plt.close()  # Close the plot to free memory

print("Bar chart saved as 'total_sales_by_region.png'.")
