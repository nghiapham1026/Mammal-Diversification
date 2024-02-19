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

# Plotting
plt.figure(figsize=(14, 8))

# Plot each taxon's diversity over time
plt.plot(artiodactyl['max_ma'], artiodactyl['sampled_in_bin'], label='Artiodactyl', marker='o')
plt.plot(carnivore['max_ma'], carnivore['sampled_in_bin'], label='Carnivore', marker='o')
plt.plot(cetacean['max_ma'], cetacean['sampled_in_bin'], label='Cetacean', marker='o')
plt.plot(perissodactyl['max_ma'], perissodactyl['sampled_in_bin'], label='Perissodactyl', marker='o')
plt.plot(primate['max_ma'], primate['sampled_in_bin'], label='Primate', marker='o')
plt.plot(proboscidea['max_ma'], proboscidea['sampled_in_bin'], label='Proboscidea', marker='o')
plt.plot(rodent['max_ma'], rodent['sampled_in_bin'], label='Rodent', marker='o')
plt.plot(ave['max_ma'], ave['sampled_in_bin'], label='Ave', marker='o')
plt.plot(reptile['max_ma'], reptile['sampled_in_bin'], label='Reptile', marker='o')

# Customize the plot
plt.title('Diversity Over Time During the Eocene and Oligocene')
plt.xlabel('Time (Million years ago)')
plt.ylabel('Number of Occurrences (Diversity)')
plt.gca().invert_xaxis()  # To display the most recent times closer to the origin
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
