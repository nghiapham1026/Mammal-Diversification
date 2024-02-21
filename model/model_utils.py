import pandas as pd
import matplotlib.pyplot as plt

# Assuming total_animal is already loaded as shown previously
total_animal = pd.read_csv('../data/processed/taxon/interpolated/Animal_Diversity_interpolated.csv')

def plot_diversity_over_time(data_path, plot_title):
    # Load the dataset for a specific taxon
    taxon_data = pd.read_csv(data_path)
    
    # Sort the taxon data by max_ma to ensure chronological order
    taxon_data.sort_values(by='max_ma', inplace=True)
    
    # Merge the taxon data with the total animal data to align them by max_ma
    merged_data = pd.merge(taxon_data, total_animal[['max_ma', 'sampled_in_bin']], on='max_ma', suffixes=('_taxon', '_total'))
    
    # Calculate the ratio of taxon occurrences to total animal occurrences
    merged_data['ratio'] = merged_data['sampled_in_bin_taxon'] / merged_data['sampled_in_bin_total']
    
    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Scatter plot for individual data points of the ratio
    plt.scatter(merged_data['max_ma'], merged_data['ratio'], color='blue', label='Taxon/Total Ratio', s=20, alpha=0.5)
    # Line plot connecting the points
    plt.plot(merged_data['max_ma'], merged_data['ratio'], color='red', label='Trend')
    
    plt.xlabel('Time (Million years ago)')
    plt.ylabel('Ratio of Taxon to Total Animal Occurrences')
    plt.title(plot_title)
    plt.gca().invert_xaxis()  # Invert x-axis to show recent times at the right
    plt.grid(True)
    plt.legend()
    plt.show()
