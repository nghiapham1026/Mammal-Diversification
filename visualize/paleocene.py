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

# Assuming data is already loaded, calculate the midpoints
aves['mid_ma'] = (aves['max_ma'] + aves['min_ma']) / 2
mammaliaformes['mid_ma'] = (mammaliaformes['max_ma'] + mammaliaformes['min_ma']) / 2
multituberculates['mid_ma'] = (multituberculates['max_ma'] + multituberculates['min_ma']) / 2
pantodonts['mid_ma'] = (pantodonts['max_ma'] + pantodonts['min_ma']) / 2
reptiles['mid_ma'] = (reptiles['max_ma'] + reptiles['min_ma']) / 2
theria['mid_ma'] = (theria['max_ma'] + theria['min_ma']) / 2

# Plot each taxon's diversity over time
ax1.plot(aves['mid_ma'], aves['sampled_in_bin'], label='Aves', marker='o')
ax1.plot(mammaliaformes['mid_ma'], mammaliaformes['sampled_in_bin'], label='Mammaliaformes', marker='o')
ax1.plot(multituberculates['mid_ma'], multituberculates['sampled_in_bin'], label='Multituberculates', marker='o')
ax1.plot(pantodonts['mid_ma'], pantodonts['sampled_in_bin'], label='Pantodonts', marker='o')
ax1.plot(reptiles['mid_ma'], reptiles['sampled_in_bin'], label='Reptiles', marker='o')
ax1.plot(theria['mid_ma'], theria['sampled_in_bin'], label='Theria', marker='o')

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
