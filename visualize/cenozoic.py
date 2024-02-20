import matplotlib.pyplot as plt
import pandas as pd

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

mammaliaformes = pd.read_csv('../data/processed/taxon/visualization/Mammaliaformes.csv')
multituberculate = pd.read_csv('../data/processed/taxon/visualization/Multituberculate.csv')
pantodont = pd.read_csv('../data/processed/taxon/visualization/Pantodont.csv')
theria = pd.read_csv('../data/processed/taxon/visualization/Theria.csv')

climate = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

# Calculate 'mid_ma' for each dataset
datasets = [artiodactyl, carnivore, cetacean, perissodactyl, primate, proboscidea, rodent, ave, reptile, mammaliaformes, multituberculate, pantodont, theria]
for df in datasets:
    df['mid_ma'] = (df['max_ma'] + df['min_ma']) / 2

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each taxon's diversity over time using 'mid_ma'
labels = ['Artiodactyl', 'Carnivore', 'Cetacean', 'Perissodactyl', 'Primate', 'Proboscidea', 'Rodent', 'Ave', 'Reptile', 'Mammaliaformes', 'Multituberculate', 'Pantodont', 'Theria']
for df, label in zip(datasets, labels):
    ax1.plot(df['mid_ma'], df['sampled_in_bin'], label=label, marker='o')

# Shading the epochs remains unchanged as it provides context to the visualization
ax1.axvspan(73, 66, color='yellow', alpha=0.3, label='Late Cretaceous')
ax1.axvspan(66, 56, color='green', alpha=0.3, label='Paleocene')
ax1.axvspan(56, 33.9, color='blue', alpha=0.3, label='Eocene')
ax1.axvspan(33.9, 23.03, color='orange', alpha=0.3, label='Oligocene')
ax1.axvspan(23.03, 5.333, color='grey', alpha=0.3, label='Miocene')
ax1.axvspan(5.333, 2.58, color='brown', alpha=0.3, label='Pliocene')
ax1.axvspan(2.58, 0.01, color='purple', alpha=0.3, label='Pleistocene')

# Customize the primary y-axis (diversity)
ax1.set_xlabel('Time (Million years ago)', fontsize=14)
ax1.set_ylabel('Number of Occurrences (Diversity)', color='black', fontsize=14)
ax1.tick_params(axis='y', labelcolor='black')
ax1.invert_xaxis()
ax1.legend(loc='upper left')
ax1.grid(True)

# The secondary y-axis for temperature does not need adjustments
ax2 = ax1.twinx()
ax2.plot(climate['Time (Myr BP)'], climate['Ts'], label='Mean Surface Temperature', color='red', marker='x', linestyle='--')
ax2.set_ylabel('Temperature (°C)', color='red', fontsize=14)
ax2.tick_params(axis='y', labelcolor='red')

# Adjust legend to include temperature
handles, labels = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(handles + handles2, labels + labels2, loc='upper right')

# Show the plot with both diversity and temperature data, and epochs shaded
plt.title('Diversity and Mean Surface Temperature Over Time', fontsize=16)
plt.tight_layout()
plt.show()
