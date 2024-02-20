import pandas as pd
import matplotlib.pyplot as plt

# Function to filter dataset based on 'max_ma' and create a copy to avoid SettingWithCopyWarning
def filter_dataset(df, min_ma, max_ma):
    filtered_df = df[(df['max_ma'] <= max_ma) & (df['max_ma'] >= min_ma)].copy()
    return filtered_df

# Load the datasets
aves = pd.read_csv('../data/processed/taxon/visualization/Ave.csv')
mammaliaformes = pd.read_csv('../data/processed/taxon/visualization/Mammaliaformes.csv')
multituberculates = pd.read_csv('../data/processed/taxon/visualization/Multituberculate.csv')
pantodonts = pd.read_csv('../data/processed/taxon/visualization/Pantodont.csv')
reptiles = pd.read_csv('../data/processed/taxon/visualization/Reptile.csv')
theria = pd.read_csv('../data/processed/taxon/visualization/Theria.csv')
climate = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

# Filter climate data for the Paleocene period (66 to 56 MYA)
climate_filtered = climate[(climate['Time (Myr BP)'] <= 66) & (climate['Time (Myr BP)'] >= 56)]

datasets = [aves, mammaliaformes, multituberculates, pantodonts, reptiles, theria]
filtered_datasets = [filter_dataset(ds, 57, 73) for ds in datasets]

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot each filtered taxon's diversity over time
labels = ['Aves', "Mammaliaformes", "Multituberculates", "Pantodonts", "Reptiles", "Theria"]
for df, label in zip(filtered_datasets, labels):
    ax1.plot(df['mid_ma'], df['sampled_in_bin'], label=label, marker='o')

# Customize the primary y-axis (diversity)
ax1.set_xlabel('Time (Million years ago)')
ax1.set_ylabel('Number of Occurrences (Diversity)', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.invert_xaxis()  # To display the most recent times closer to the origin
ax1.legend()
ax1.grid(True)

# Shading the epochs
## Late Cretaceous (100.5 to 66 MYA)
ax1.axvspan(67, 66, color='yellow', alpha=0.3, label='Late Cretaceous')
## Paleocene (66 to 56 MYA)
ax1.axvspan(66, 56, color='green', alpha=0.3, label='Paleocene')
## Eocene (56 to 33.9 MYA)
ax1.axvspan(56, 55, color='blue', alpha=0.3, label='Eocene')

# Create a secondary y-axis for mean surface temperature
ax2 = ax1.twinx()
ax2.plot(climate_filtered['Time (Myr BP)'], climate_filtered['Ts'], label='Mean Surface Temperature', color='red', marker='x', linestyle='--')
ax2.set_ylabel('Temperature (°C)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add legend for the temperature
ax2.legend(loc='upper left')

# Adjust legend to include epochs
handles, labels = ax1.get_legend_handles_labels()
epoch_patches = [plt.Rectangle((0,0),1,1, color=c, alpha=0.3) for c in ['yellow', 'green', 'blue']]
handles.extend(epoch_patches)
ax1.legend(handles, labels, loc='upper right')

# Show the plot with both diversity and temperature data
plt.title('Diversity and Mean Surface Temperature Over Time: Paleocene')
plt.tight_layout()  # Adjust layout to ensure everything fits without overlapping
plt.show()
