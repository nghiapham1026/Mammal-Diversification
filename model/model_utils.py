import pandas as pd
import matplotlib.pyplot as plt

# Assuming total_animal is already loaded as shown previously
total_animal = pd.read_csv('../data/processed/taxon/interpolated/Animal_Diversity_interpolated.csv')
climate_data = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

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

def plot_taxon_with_context(df, taxon_label, ax):
    # Determine the style based on the taxon type
    extinct_taxa = ['Multituberculates', 'Pantodonts', 'Plesiadapiformes', 'Condylarths', 'Creodonts']
    reptilian_taxa = ['Aves', 'Reptiles']
    if taxon_label in extinct_taxa:
        marker, linestyle = 'x', ':'
        ax.plot(df['mid_ma'], df['sampled_in_bin'], label=taxon_label + ' (Extinct)', marker=marker, linestyle=linestyle)
        last_point = df.iloc[0]
        ax.plot(last_point['mid_ma'], last_point['sampled_in_bin'], 'rx', markersize=12, markeredgewidth=2)
    elif taxon_label in reptilian_taxa:
        marker, linestyle = '^', '--'
        ax.plot(df['mid_ma'], df['sampled_in_bin'], label=taxon_label, marker=marker, linestyle=linestyle, alpha=0.7)
    else:  # Mammalian taxa
        marker, linestyle = 'o', '-'
        ax.plot(df['mid_ma'], df['sampled_in_bin'], label=taxon_label, marker=marker, linestyle=linestyle, alpha=0.7)

    # Plot climate data on a secondary y-axis
    ax2 = ax.twinx()
    ax2.plot(climate_data['Time (Myr BP)'], climate_data['Ts'], label='Mean Surface Temperature', color='red', marker='x', linestyle='--')
    ax2.set_ylabel('Temperature (°C)', color='red')

    # Shading epochs
    epoch_colors = {
        'Late Cretaceous': 'yellow',
        'Paleocene': 'green',
        'Eocene': 'blue',
        'Oligocene': 'orange',
        'Miocene': 'grey',
        'Pliocene': 'brown',
        'Pleistocene': 'purple',
        'Holocene': 'aqua'
    }
    epoch_spans = [(73, 66), (66, 56), (56, 33.9), (33.9, 23.03), (23.03, 5.333), (5.333, 2.58), (2.58, 0.01), (0.01, 0)]
    for span, color in zip(epoch_spans, epoch_colors.values()):
        ax.axvspan(span[0], span[1], color=color, alpha=0.3, label=list(epoch_colors.keys())[list(epoch_colors.values()).index(color)])

    # Customize plot appearance
    ax.set_xlabel('Time (Million years ago)')
    ax.set_ylabel('Number of Occurrences (Diversity)')
    ax.invert_xaxis()  # Most recent times are closer to the origin
    ax.legend(loc='upper left')
    ax.grid(True)

    # Adding legend for climate data
    handles2, labels2 = ax2.get_legend_handles_labels()
    ax2.legend(handles2, labels2, loc='upper right')

    plt.title(f'Diversity and Mean Surface Temperature Over Time: {taxon_label}')
    plt.tight_layout()