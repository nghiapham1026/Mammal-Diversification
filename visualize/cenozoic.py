import matplotlib.pyplot as plt
import pandas as pd

def plot_with_extinction_mark(df, label, color, marker='x', linestyle=':'):
    ax1.plot(df['mid_ma'], df['sampled_in_bin'], label=label, color=color, marker=marker, linestyle=linestyle)
    # Check if the group is one of the specified taxa and mark its last point
    last_point = df.iloc[0]
    ax1.plot(last_point['mid_ma'], last_point['sampled_in_bin'], 'rx', markersize=12, markeredgewidth=2)

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
plesiadapiformes = pd.read_csv('../data/processed/taxon/visualization/Plesiadapiformes.csv')
condylarths = pd.read_csv('../data/processed/taxon/visualization/Condylarth.csv')
creodonts = pd.read_csv('../data/processed/taxon/visualization/Creodont.csv')
multituberculate = pd.read_csv('../data/processed/taxon/visualization/Multituberculate.csv')
pantodont = pd.read_csv('../data/processed/taxon/visualization/Pantodont.csv')
theria = pd.read_csv('../data/processed/taxon/visualization/Theria.csv')

multituberculates = pd.read_csv('../data/processed/taxon/visualization/Multituberculate.csv')
pantodonts = pd.read_csv('../data/processed/taxon/visualization/Pantodont.csv')
plesiadapiformes = pd.read_csv('../data/processed/taxon/visualization/Plesiadapiformes.csv')
condylarths = pd.read_csv('../data/processed/taxon/visualization/Condylarth.csv')
creodont = pd.read_csv('../data/processed/taxon/visualization/Creodont.csv')

climate = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

datasets = [artiodactyl, carnivore, cetacean, perissodactyl, primate, proboscidea, rodent, theria]
non_mammals = [ave, reptile]

# Plotting
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot mammalian taxa
for df, label in zip(datasets, ['Artiodactyl', 'Carnivore', 'Cetacean', 'Perissodactyl', 'Primate', 'Proboscidea', 'Rodent', 'Theria']):
    ax1.plot(df['mid_ma'], df['sampled_in_bin'], label=label, marker='o', linestyle='-', alpha=0.7)

reptilian_labels = ['Aves', 'Reptiles']
reptilian_datasets = [ave, reptile]

for df, label in zip(reptilian_datasets, reptilian_labels):
    ax1.plot(df['mid_ma'], df['sampled_in_bin'], label=label, marker='^', linestyle='--', linewidth=3)

plot_with_extinction_mark(multituberculates, 'Multituberculates (Extinct)', 'blue')
plot_with_extinction_mark(pantodonts, 'Pantodonts (Extinct)', 'green')
plot_with_extinction_mark(plesiadapiformes, 'Plesiadapiformes (Extinct)', 'orange')
plot_with_extinction_mark(condylarths, 'Condylarths (Extinct)', 'purple')
plot_with_extinction_mark(creodont, 'Creodonts (Extinct)', 'blue')

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
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True)

# Create a secondary y-axis for mean surface temperature
ax2 = ax1.twinx()
ax2.plot(climate['Time (Myr BP)'], climate['Ts'], label='Mean Surface Temperature', color='red', marker='x', linestyle='--')
ax2.set_ylabel('Temperature (°C)', color='red', fontsize=14)
ax2.tick_params(axis='y', labelcolor='red')

# Show the plot with both diversity and temperature data, and epochs shaded
plt.title('Diversity and Mean Surface Temperature Over Time', fontsize=16)
plt.tight_layout()
plt.show()