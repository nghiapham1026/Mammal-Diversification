import matplotlib.pyplot as plt
import pandas as pd

# Load the datasets
artiodactyl = pd.read_csv('../data/processed/taxon/visualization/pleistocene/Artiodactyl.csv')
ave = pd.read_csv('../data/processed/taxon/visualization/pleistocene/Ave.csv')
carnivore = pd.read_csv('../data/processed/taxon/visualization/pleistocene/Carnivore.csv')
cetacean = pd.read_csv('../data/processed/taxon/visualization/pleistocene/Cetacean.csv')
perissodactyl = pd.read_csv('../data/processed/taxon/visualization/pleistocene/Perissodactyl.csv')
primate = pd.read_csv('../data/processed/taxon/visualization/pleistocene/Primate.csv')
proboscidea = pd.read_csv('../data/processed/taxon/visualization/pleistocene/Proboscidea.csv')
reptile = pd.read_csv('../data/processed/taxon/visualization/pleistocene/Reptile.csv')
climate = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

# Adjust climate data filter for the Pleistocene period (approximately 2.58 MYA to 0.01 MYA)
climate_filtered = climate[(climate['Time (Myr BP)'] <= 4) & (climate['Time (Myr BP)'] >= 0.01)]

# Plotting with dual-axis for temperature
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot each taxon's diversity over time
# Using 'min_ma' for a more accurate representation towards the present
ax1.plot(artiodactyl['min_ma'], artiodactyl['sampled_in_bin'], label='Artiodactyl', marker='o')
ax1.plot(carnivore['min_ma'], carnivore['sampled_in_bin'], label='Carnivore', marker='o')
ax1.plot(cetacean['min_ma'], cetacean['sampled_in_bin'], label='Cetacean', marker='o')
ax1.plot(perissodactyl['min_ma'], perissodactyl['sampled_in_bin'], label='Perissodactyl', marker='o')
ax1.plot(primate['min_ma'], primate['sampled_in_bin'], label='Primate', marker='o')
ax1.plot(proboscidea['min_ma'], proboscidea['sampled_in_bin'], label='Proboscidea', marker='o')
ax1.plot(reptile['min_ma'], reptile['sampled_in_bin'], label='Reptile', marker='o')

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

# Show the plot with both diversity and temperature data
plt.title('Diversity and Mean Surface Temperature Over Time: Pleistocene', fontsize=16)
plt.tight_layout()  # Adjust layout to make sure everything fits without overlapping
plt.show()
