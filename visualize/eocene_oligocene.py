import matplotlib.pyplot as plt
import pandas as pd

# Load datasets
artiodactyl = pd.read_csv('../data/processed/taxon/visualization/eocene-oligocene/Artiodactyl.csv')
carnivore = pd.read_csv('../data/processed/taxon/visualization/eocene-oligocene/Carnivore.csv')
cetacean = pd.read_csv('../data/processed/taxon/visualization/eocene-oligocene/Cetacean.csv')
perissodactyl = pd.read_csv('../data/processed/taxon/visualization/eocene-oligocene/Perissodactyl.csv')
primate = pd.read_csv('../data/processed/taxon/visualization/eocene-oligocene/Primate.csv')
proboscidea = pd.read_csv('../data/processed/taxon/visualization/eocene-oligocene/Proboscidea.csv')
rodent = pd.read_csv('../data/processed/taxon/visualization/eocene-oligocene/Rodent.csv')
ave = pd.read_csv('../data/processed/taxon/visualization/eocene-oligocene/Ave.csv')
reptile = pd.read_csv('../data/processed/taxon/visualization/eocene-oligocene/Reptile.csv')
climate = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

# Filter climate data for the Eocene and Oligocene periods (56 to 23 MYA)
climate_filtered = climate[(climate['Time (Myr BP)'] <= 66) & (climate['Time (Myr BP)'] >= 23)]

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot each taxon's diversity over time
ax1.plot(artiodactyl['min_ma'], artiodactyl['sampled_in_bin'], label='Artiodactyl', marker='o')
ax1.plot(carnivore['min_ma'], carnivore['sampled_in_bin'], label='Carnivore', marker='o')
ax1.plot(cetacean['min_ma'], cetacean['sampled_in_bin'], label='Cetacean', marker='o')
ax1.plot(perissodactyl['min_ma'], perissodactyl['sampled_in_bin'], label='Perissodactyl', marker='o')
ax1.plot(primate['min_ma'], primate['sampled_in_bin'], label='Primate', marker='o')
ax1.plot(proboscidea['min_ma'], proboscidea['sampled_in_bin'], label='Proboscidea', marker='o')
ax1.plot(rodent['min_ma'], rodent['sampled_in_bin'], label='Rodent', marker='o')
ax1.plot(ave['min_ma'], ave['sampled_in_bin'], label='Ave', marker='o')
ax1.plot(reptile['min_ma'], reptile['sampled_in_bin'], label='Reptile', marker='o')

# Customize the primary y-axis (diversity)
ax1.set_xlabel('Time (Million years ago)', fontsize=14)
ax1.set_ylabel('Number of Occurrences (Diversity)', color='black', fontsize=14)
ax1.tick_params(axis='y', labelcolor='black')
ax1.invert_xaxis()  # To display the most recent times closer to the origin
ax1.legend(loc='upper left')
ax1.grid(True)

# Create a secondary y-axis for mean surface temperature
ax2 = ax1.twinx()
ax2.plot(climate_filtered['Time (Myr BP)'], climate_filtered['Ts'], label='Mean Surface Temperature', color='red', marker='x', linestyle='--')
ax2.set_ylabel('Temperature (°C)', color='red', fontsize=14)
ax2.tick_params(axis='y', labelcolor='red')

# Show the plot with both diversity and temperature data
plt.title('Diversity and Mean Surface Temperature Over Time: Eocene and Oligocene', fontsize=16)
plt.tight_layout()  # Adjust layout to ensure everything fits without overlapping
plt.show()
