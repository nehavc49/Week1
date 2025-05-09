import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Base Class
class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Load data from CSV into DataFrame"""
        try:
            self.df = pd.read_csv(self.file_path)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("Error: CSV file not found.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def show_summary(self):
        """Display basic statistics"""
        if self.df is not None:
            print("\n--- Data Summary ---")
            print(self.df.describe())
        else:
            print("Data not loaded.")

    def calculate_statistics(self):
        """Return mean and median of Age and Income"""
        if self.df is not None:
            mean_age = np.mean(self.df['Age'])
            median_income = np.median(self.df['Income'])
            print(f"\nMean Age: {mean_age}")
            print(f"Median Income: {median_income}")
        else:
            print("Data not loaded.")

# Subclass with additional student-specific methods
class StudentDataAnalyzer(DataAnalyzer):
    def filter_by_gender(self, gender):
        """Return filtered data by gender"""
        if self.df is not None:
            filtered = self.df[self.df['Gender'].str.lower() == gender.lower()]
            print(f"\nFiltered Data (Gender = {gender}):\n", filtered)
        else:
            print("Data not loaded.")

    def plot_distribution(self):
        """Plot age and income distribution"""
        if self.df is not None:
            plt.figure(figsize=(12, 5))

            # Age Distribution
            plt.subplot(1, 2, 1)
            plt.hist(self.df['Age'], color='skyblue', edgecolor='black')
            plt.title("Age Distribution")
            plt.xlabel("Age")
            plt.ylabel("Count")

            # Income Distribution
            plt.subplot(1, 2, 2)
            plt.hist(self.df['Income'], color='lightgreen', edgecolor='black')
            plt.title("Income Distribution")
            plt.xlabel("Income")
            plt.ylabel("Count")

            plt.tight_layout()
            plt.show()
        else:
            print("Data not loaded.")

def main():
    analyzer = StudentDataAnalyzer("data.csv")
    analyzer.load_data()
    analyzer.show_summary()
    analyzer.calculate_statistics()
    analyzer.filter_by_gender("Female")
    analyzer.plot_distribution()

if __name__ == "__main__":
    main()

