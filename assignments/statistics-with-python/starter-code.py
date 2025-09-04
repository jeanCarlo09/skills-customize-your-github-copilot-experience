import pandas as pd
import numpy as np

# Load your dataset here
def load_dataset(file_path):
    return pd.read_csv(file_path)

# Perform basic statistical calculations
def calculate_statistics(data):
    stats = {
        'mean': data.mean(),
        'median': data.median(),
        'std_dev': data.std(),
        'correlation': data.corr()
    }
    return stats

# Example usage
if __name__ == "__main__":
    # Replace 'data.csv' with your dataset file
    dataset = load_dataset('data.csv')
    print("Dataset Head:")
    print(dataset.head())

    print("\nStatistics:")
    stats = calculate_statistics(dataset)
    for key, value in stats.items():
        print(f"{key.capitalize()}:\n{value}\n")
