import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
aves = pd.read_csv('../data/processed/taxon/visualization/paleocene/Ave.csv')
mammaliaformes = pd.read_csv('../data/processed/taxon/visualization/paleocene/Mammaliaformes.csv')
multituberculates = pd.read_csv('../data/processed/taxon/visualization/paleocene/Multituberculate.csv')
pantodonts = pd.read_csv('../data/processed/taxon/visualization/paleocene/Pantodont.csv')
reptiles = pd.read_csv('../data/processed/taxon/visualization/paleocene/Reptile.csv')
theria = pd.read_csv('../data/processed/taxon/visualization/paleocene/Theria.csv')
climate = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

# Filter climate data for the Paleocene period (66 to 56 MYA)
climate_filtered = climate[(climate['Time (Myr BP)'] <= 66) & (climate['Time (Myr BP)'] >= 56)]

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot each taxon's diversity over time
ax1.plot(aves['min_ma'], aves['sampled_in_bin'], label='Aves', marker='o')
ax1.plot(mammaliaformes['min_ma'], mammaliaformes['sampled_in_bin'], label='Mammaliaformes', marker='o')
ax1.plot(multituberculates['min_ma'], multituberculates['sampled_in_bin'], label='Multituberculates', marker='o')
ax1.plot(pantodonts['min_ma'], pantodonts['sampled_in_bin'], label='Pantodonts', marker='o')
ax1.plot(reptiles['min_ma'], reptiles['sampled_in_bin'], label='Reptiles', marker='o')
ax1.plot(theria['min_ma'], theria['sampled_in_bin'], label='Theria', marker='o')

# Customize the primary y-axis (diversity)
ax1.set_xlabel('Time (Million years ago)')
ax1.set_ylabel('Number of Occurrences (Diversity)', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.invert_xaxis()  # To display the most recent times closer to the origin
ax1.legend()
ax1.grid(True)

# Create a secondary y-axis for mean surface temperature
ax2 = ax1.twinx()
ax2.plot(climate_filtered['Time (Myr BP)'], climate_filtered['Ts'], label='Mean Surface Temperature', color='red', marker='x', linestyle='--')
ax2.set_ylabel('Temperature (°C)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add legend for the temperature
ax2.legend(loc='upper left')

# Show the plot with both diversity and temperature data
plt.title('Diversity and Mean Surface Temperature Over Time: Paleocene')
plt.show()
