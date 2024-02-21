import matplotlib.pyplot as plt
import pandas as pd

# Function to filter dataset based on 'max_ma' and create a copy to avoid SettingWithCopyWarning
def filter_dataset(df, min_ma, max_ma):
    filtered_df = df[(df['max_ma'] <= max_ma) & (df['max_ma'] >= min_ma)].copy()
    return filtered_df

def plot_with_extinction_mark(df, label, color, marker='x', linestyle=':'):
    ax1.plot(df['mid_ma'], df['sampled_in_bin'], label=label, color=color, marker=marker, linestyle=linestyle)
    # Check if the group is one of the specified taxa and mark its last point
    last_point = df.iloc[0]
    ax1.plot(last_point['mid_ma'], last_point['sampled_in_bin'], 'rx', markersize=12, markeredgewidth=2)

# Load the datasets
artiodactyl = pd.read_csv('../data/processed/taxon/visualization/Artiodactyl.csv')
ave = pd.read_csv('../data/processed/taxon/visualization/Ave.csv')
carnivore = pd.read_csv('../data/processed/taxon/visualization/Carnivore.csv')
cetacean = pd.read_csv('../data/processed/taxon/visualization/Cetacean.csv')
perissodactyl = pd.read_csv('../data/processed/taxon/visualization/Perissodactyl.csv')
primate = pd.read_csv('../data/processed/taxon/visualization/Primate.csv')
proboscidea = pd.read_csv('../data/processed/taxon/visualization/Proboscidea.csv')
reptile = pd.read_csv('../data/processed/taxon/visualization/Reptile.csv')
rodent = pd.read_csv('../data/processed/taxon/visualization/Rodent.csv')
creodont = pd.read_csv('../data/processed/taxon/visualization/Creodont.csv')

climate = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

# Filter climate data for the Neogene period (23 to about 2.6 MYA)
climate_filtered = climate[(climate['Time (Myr BP)'] <= 25) & (climate['Time (Myr BP)'] >= 2.6)]

# Plotting with dual-axis for temperature
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot mammalian taxa
mammalian_labels = ['Artiodactyl', 'Carnivore', 'Cetacean', 'Perissodactyl', 'Primate', 'Proboscidea', 'Rodent']
mammalian_datasets = [artiodactyl, carnivore, cetacean, perissodactyl, primate, proboscidea, rodent]
mammalian_datasets = [filter_dataset(ds, 2, 30) for ds in mammalian_datasets]
for df, label in zip(mammalian_datasets, mammalian_labels):
    ax1.plot(df['mid_ma'], df['sampled_in_bin'], label=label, marker='o', linestyle='-', alpha=0.7)

reptilian_labels = ['Aves', 'Reptiles']
reptilian_datasets = [ave, reptile]
reptilian_datasets = [filter_dataset(ds, 2, 30) for ds in reptilian_datasets]

for df, label in zip(reptilian_datasets, reptilian_labels):
    ax1.plot(df['mid_ma'], df['sampled_in_bin'], label=label, marker='^', linestyle='--', linewidth=3)

plot_with_extinction_mark(filter_dataset(creodont, 2, 30), 'Creodonts (Extinct)', 'blue')

# Shading the Miocene and Pliocene epochs
ax1.axvspan(27, 23, color='blue', alpha=0.3, label='Oligocene')
ax1.axvspan(23, 5.3, color='orange', alpha=0.3, label='Miocene')
ax1.axvspan(5.3, 2.58, color='green', alpha=0.3, label='Pliocene')
ax1.axvspan(2.58, 2, color='yellow', alpha=0.3, label='Pleistocene')

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

# Show the plot with both diversity and temperature data, and epochs shaded
plt.title('Diversity and Mean Surface Temperature Over Time: Neogene', fontsize=16)
plt.tight_layout()
plt.show()