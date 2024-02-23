import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset for a specific taxon
animal = pd.read_csv('../data/processed/taxon/Animal_Diversity.csv')
animal['mid_ma'] = (animal['max_ma'] + animal['min_ma']) / 2

climate_data = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 6))

# Shading epochs
epoch_colors = {
    'Late Cretaceous': 'yellow',
    'Paleocene': 'green',
    'Eocene': 'blue',
    'Oligocene': 'orange',
    'Miocene': 'grey',
    'Pliocene': 'brown',
    'Pleistocene': 'purple',
    'Holocene': 'aqua'
}
epoch_spans = [(73, 66), (66, 56), (56, 33.9), (33.9, 23.03), (23.03, 5.333), (5.333, 2.58), (2.58, 0.01), (0.01, 0)]
for span, color in zip(epoch_spans, epoch_colors.values()):
    ax1.axvspan(span[0], span[1], color=color, alpha=0.3, label=list(epoch_colors.keys())[list(epoch_colors.values()).index(color)])

# Scatter plot for individual data points of the ratio
ax1.scatter(animal['mid_ma'], animal['sampled_in_bin'], color='blue', label='Animal Diversity', s=20, alpha=0.5)
# Line plot connecting the points
ax1.plot(animal['mid_ma'], animal['sampled_in_bin'], color='green', label='Trend')

# Set the primary y-axis label
ax1.set_ylabel('Number of Occurrences', color='black')
ax1.set_xlabel('Time (Million years ago)')

# Plot climate data on a secondary y-axis
ax2 = ax1.twinx()
ax2.plot(climate_data['Time (Myr BP)'], climate_data['Ts'], label='Mean Surface Temperature', color='red', marker='x', linestyle='--')
ax2.set_ylabel('Temperature (°C)', color='red')

ax1.set_title('Animal Diversity over Time')
ax1.invert_xaxis()  # Invert x-axis to show recent times at the right
ax1.grid(True)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()
