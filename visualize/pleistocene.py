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

# Adjust climate data filter for the Pleistocene period (approximately 2.58 MYA to 0.01 MYA)
climate_filtered = climate[(climate['Time (Myr BP)'] <= 4.5) & (climate['Time (Myr BP)'] >= 0.01)]
datasets = [artiodactyl, ave, carnivore, cetacean, perissodactyl, primate, proboscidea, reptile]
filtered_datasets = [filter_dataset(ds, 0, 5.5) for ds in datasets]

# Plotting with dual-axis for temperature
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot each filtered taxon's diversity over time
labels = ['Artyodactyl', 'Ave', 'Carnivora', 'Cetacean', 'Perissodactyl', 'Primate', 'Proboscidea', 'Reptile']
for df, label in zip(filtered_datasets, labels):
    ax1.plot(df['mid_ma'], df['sampled_in_bin'], label=label, marker='o')

# Shading the epochs
# Pliocene Epoch (5.3 to 2.58 MYA)
ax1.axvspan(5, 2.58, color='orange', alpha=0.3, label='Pliocene')
# Pleistocene Epoch (2.58 MYA to 0.0117 MYA)
ax1.axvspan(2.58, 0.0117, color='blue', alpha=0.3, label='Pleistocene')
# Holocene Epoch (0.0117 MYA to present)
ax1.axvspan(0.0117, 0, color='green', alpha=0.3, label='Holocene')

# Customize the primary y-axis (diversity)
ax1.set_xlabel('Time (Million years ago)', fontsize=14)
ax1.set_ylabel('Number of Occurrences (Diversity)', color='black', fontsize=14)
ax1.tick_params(axis='y', labelcolor='black')
ax1.invert_xaxis()  # Invert x-axis to show the most recent times closer to the origin
ax1.legend(loc='upper left')
ax1.grid(True)

# Create a secondary y-axis for mean surface temperature
ax2 = ax1.twinx()
ax2.plot(climate_filtered['Time (Myr BP)'], climate_filtered['Ts'], label='Mean Surface Temperature', color='red', marker='x', linestyle='--')
ax2.set_ylabel('Temperature (°C)', color='red', fontsize=14)
ax2.tick_params(axis='y', labelcolor='red')

# Show the plot with both diversity and temperature data, and epochs shaded
plt.title('Diversity and Mean Surface Temperature Over Time: Pleistocene', fontsize=16)
plt.tight_layout()  # Adjust layout to make sure everything fits without overlapping
plt.show()