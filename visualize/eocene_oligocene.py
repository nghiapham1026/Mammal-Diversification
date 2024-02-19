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

artiodactyl['mid_ma'] = (artiodactyl['max_ma'] + artiodactyl['min_ma']) / 2
ave['mid_ma'] = (ave['max_ma'] + ave['min_ma']) / 2
carnivore['mid_ma'] = (carnivore['max_ma'] + carnivore['min_ma']) / 2
cetacean['mid_ma'] = (cetacean['max_ma'] + cetacean['min_ma']) / 2
perissodactyl['mid_ma'] = (perissodactyl['max_ma'] + perissodactyl['min_ma']) / 2
primate['mid_ma'] = (primate['max_ma'] + primate['min_ma']) / 2
proboscidea['mid_ma'] = (proboscidea['max_ma'] + proboscidea['min_ma']) / 2
reptile['mid_ma'] = (reptile['max_ma'] + reptile['min_ma']) / 2
rodent['mid_ma'] = (rodent['max_ma'] + rodent['min_ma']) / 2

# Plot each taxon's diversity over time
ax1.plot(artiodactyl['mid_ma'], artiodactyl['sampled_in_bin'], label='Artiodactyl', marker='o')
ax1.plot(carnivore['mid_ma'], carnivore['sampled_in_bin'], label='Carnivore', marker='o')
ax1.plot(cetacean['mid_ma'], cetacean['sampled_in_bin'], label='Cetacean', marker='o')
ax1.plot(perissodactyl['mid_ma'], perissodactyl['sampled_in_bin'], label='Perissodactyl', marker='o')
ax1.plot(primate['mid_ma'], primate['sampled_in_bin'], label='Primate', marker='o')
ax1.plot(proboscidea['mid_ma'], proboscidea['sampled_in_bin'], label='Proboscidea', marker='o')
ax1.plot(rodent['mid_ma'], rodent['sampled_in_bin'], label='Rodent', marker='o')
ax1.plot(ave['mid_ma'], ave['sampled_in_bin'], label='Ave', marker='o')
ax1.plot(reptile['mid_ma'], reptile['sampled_in_bin'], label='Reptile', marker='o')

# Shading the epochs
ax1.axvspan(66, 56, color='green', alpha=0.3, label='Paleocene')
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