import matplotlib.pyplot as plt
import pandas as pd

# Function to filter dataset based on 'max_ma' and create a copy to avoid SettingWithCopyWarning
def filter_dataset(df, min_ma, max_ma):
    filtered_df = df[(df['max_ma'] <= max_ma) & (df['max_ma'] >= min_ma)].copy()
    return filtered_df

# Load the datasets
artiodactyl = pd.read_csv('../data/processed/taxon/visualization/Artiodactyl.csv')
ave = pd.read_csv('../data/processed/taxon/visualization/Ave.csv')
carnivore = pd.read_csv('../data/processed/taxon/visualization/Carnivore.csv')
cetacean = pd.read_csv('../data/processed/taxon/visualization/Cetacean.csv')
perissodactyl = pd.read_csv('../data/processed/taxon/visualization/Perissodactyl.csv')
primate = pd.read_csv('../data/processed/taxon/visualization/Primate.csv')
proboscidea = pd.read_csv('../data/processed/taxon/visualization/Proboscidea.csv')
reptile = pd.read_csv('../data/processed/taxon/visualization/Reptile.csv')
climate = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

# Filter climate data for the Neogene period (23 to about 2.6 MYA)
climate_filtered = climate[(climate['Time (Myr BP)'] <= 25) & (climate['Time (Myr BP)'] >= 2.6)]

# Filter each taxon dataset for 'max_ma' within 30 and 2
datasets = [artiodactyl, ave, carnivore, cetacean, perissodactyl, primate, proboscidea, reptile]
filtered_datasets = [filter_dataset(ds, 2, 30) for ds in datasets]

# Plotting with dual-axis for temperature
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot each filtered taxon's diversity over time
labels = ['Artiodactyl', 'Ave', 'Carnivore', 'Cetacean', 'Perissodactyl', 'Primate', 'Proboscidea', 'Reptile']
for df, label in zip(filtered_datasets, labels):
    ax1.plot(df['mid_ma'], df['sampled_in_bin'], label=label, marker='o')

# Shading the Miocene and Pliocene epochs
ax1.axvspan(23, 5.3, color='orange', alpha=0.3, label='Miocene Epoch')
ax1.axvspan(5.3, 2.58, color='green', alpha=0.3, label='Pliocene Epoch')

# Customize the primary y-axis (diversity)
ax1.set_xlabel('Time (Million years ago)', fontsize=14)
ax1.set_ylabel('Number of Occurrences (Diversity)', color='black', fontsize=14)
ax1.tick_params(axis='y', labelcolor='black')
ax1.invert_xaxis()
ax1.legend(loc='upper left')
ax1.grid(True)

# Create a secondary y-axis for mean surface temperature
ax2 = ax1.twinx()
ax2.plot(climate_filtered['Time (Myr BP)'], climate_filtered['Ts'], label='Mean Surface Temperature', color='red', marker='x', linestyle='--')
ax2.set_ylabel('Temperature (°C)', color='red', fontsize=14)
ax2.tick_params(axis='y', labelcolor='red')

# Adjust legend to include temperature and epochs
handles, labels = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(handles + handles2, labels + labels2, loc='upper right')

# Show the plot with both diversity and temperature data, and epochs shaded
plt.title('Diversity and Mean Surface Temperature Over Time: Neogene', fontsize=16)
plt.tight_layout()
plt.show()