import matplotlib.pyplot as plt
import pandas as pd

# Function to filter dataset based on 'max_ma' and create a copy to avoid SettingWithCopyWarning
def filter_dataset(df, min_ma, max_ma):
    filtered_df = df[(df['max_ma'] <= max_ma) & (df['max_ma'] >= min_ma)].copy()
    return filtered_df

# Load datasets
artiodactyl = pd.read_csv('../data/processed/taxon/visualization/Artiodactyl.csv')
carnivore = pd.read_csv('../data/processed/taxon/visualization/Carnivore.csv')
cetacean = pd.read_csv('../data/processed/taxon/visualization/Cetacean.csv')
perissodactyl = pd.read_csv('../data/processed/taxon/visualization/Perissodactyl.csv')
primate = pd.read_csv('../data/processed/taxon/visualization/Primate.csv')
proboscidea = pd.read_csv('../data/processed/taxon/visualization/Proboscidea.csv')
rodent = pd.read_csv('../data/processed/taxon/visualization/Rodent.csv')
ave = pd.read_csv('../data/processed/taxon/visualization/Ave.csv')
reptile = pd.read_csv('../data/processed/taxon/visualization/Reptile.csv')
climate = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

# Filter climate data for the Eocene and Oligocene periods (56 to 23 MYA)
climate_filtered = climate[(climate['Time (Myr BP)'] <= 59) & (climate['Time (Myr BP)'] >= 23)]

# Filter each taxon dataset for 'max_ma' within 27 and 57
datasets = [artiodactyl, ave, carnivore, cetacean, perissodactyl, primate, proboscidea, rodent, reptile]
filtered_datasets = [filter_dataset(ds, 27, 60) for ds in datasets]

# Now plotting can proceed with the 'mid_ma' values available
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each filtered taxon's diversity over time using 'mid_ma'
labels = ['Artiodactyl', 'Carnivore', 'Cetacean', 'Perissodactyl', 'Primate', 'Proboscidea', 'Rodent', 'Ave', 'Reptile']
for df, label in zip(filtered_datasets, labels):
    ax1.plot(df['mid_ma'], df['sampled_in_bin'], label=label, marker='o')

# Shading the epochs
ax1.axvspan(60, 56, color='green', alpha=0.3, label='Paleocene')
# Eocene Epoch (56 to 33.9 MYA)
ax1.axvspan(56, 33.9, color='blue', alpha=0.3, label='Eocene')
# Oligocene Epoch (33.9 to 23 MYA)
ax1.axvspan(33.9, 23, color='orange', alpha=0.3, label='Oligocene')

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

# Adjust legend to include temperature
handles, labels = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(handles + handles2, labels + labels2, loc='upper right')

# Show the plot with both diversity and temperature data, and epochs shaded
plt.title('Diversity and Mean Surface Temperature Over Time: Eocene and Oligocene', fontsize=16)
plt.tight_layout()  # Adjust layout to ensure everything fits without overlapping
plt.show()