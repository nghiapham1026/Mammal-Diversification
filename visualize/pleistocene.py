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

# Prepare figure
plt.figure(figsize=(12, 8))

# Plot each taxon's diversity over time
plt.plot(artiodactyl['max_ma'], artiodactyl['sampled_in_bin'], label='Artiodactyl', marker='o')
#plt.plot(ave['max_ma'], ave['sampled_in_bin'], label='Ave', marker='o')
plt.plot(carnivore['max_ma'], carnivore['sampled_in_bin'], label='Carnivore', marker='o')
plt.plot(cetacean['max_ma'], cetacean['sampled_in_bin'], label='Cetacean', marker='o')
plt.plot(perissodactyl['max_ma'], perissodactyl['sampled_in_bin'], label='Perissodactyl', marker='o')
plt.plot(primate['max_ma'], primate['sampled_in_bin'], label='Primate', marker='o')
plt.plot(proboscidea['max_ma'], proboscidea['sampled_in_bin'], label='Proboscidea', marker='o')
plt.plot(reptile['max_ma'], reptile['sampled_in_bin'], label='Reptile', marker='o')

# Customize the plot
plt.title('Diversity Over Time During the Pleistocene')
plt.xlabel('Time (Million years ago)')
plt.ylabel('Number of Occurrences (Diversity)')
plt.legend()
plt.gca().invert_xaxis()  # To display the most recent times closer to the origin
plt.grid(True)

# Show plot
plt.show()
