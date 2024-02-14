import pandas as pd
import matplotlib.pyplot as plt

def plot_diversity_over_time(data_path, plot_title):
    # Load the dataset
    data = pd.read_csv(data_path)
    
    # Sort the data by max_ma to ensure chronological order
    data.sort_values(by='max_ma', inplace=True)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    # Scatter plot for individual data points
    plt.scatter(data['max_ma'], data['n_occs'], color='blue', label='Number of Occurrences', s=20, alpha=0.5)
    # Line plot connecting the points
    plt.plot(data['max_ma'], data['n_occs'], color='red', label='Trend')
    
    plt.xlabel('Time (Million years ago)')
    plt.ylabel('Number of Occurrences')
    plt.title(plot_title)
    plt.gca().invert_xaxis()  # Invert x-axis to show recent times at the right
    plt.grid(True)
    plt.legend()
    plt.show()