import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
aves = pd.read_csv('../data/processed/taxon/visualization/paleocene/Ave.csv')
mammaliaformes = pd.read_csv('../data/processed/taxon/visualization/paleocene/Mammaliaformes.csv')
multituberculates = pd.read_csv('../data/processed/taxon/visualization/paleocene/Multituberculate.csv')
pantodonts = pd.read_csv('../data/processed/taxon/visualization/paleocene/Pantodont.csv')
reptiles = pd.read_csv('../data/processed/taxon/visualization/paleocene/Reptile.csv')
theria = pd.read_csv('../data/processed/taxon/visualization/paleocene/Theria.csv')

# Plotting
plt.figure(figsize=(12, 8))

# Plot each taxon's diversity over time
plt.plot(aves['max_ma'], aves['sampled_in_bin'], label='Aves', marker='o')
plt.plot(mammaliaformes['max_ma'], mammaliaformes['sampled_in_bin'], label='Mammaliaformes', marker='o')
plt.plot(multituberculates['max_ma'], multituberculates['sampled_in_bin'], label='Multituberculates', marker='o')
plt.plot(pantodonts['max_ma'], pantodonts['sampled_in_bin'], label='Pantodonts', marker='o')
plt.plot(reptiles['max_ma'], reptiles['sampled_in_bin'], label='Reptiles', marker='o')
plt.plot(theria['max_ma'], theria['sampled_in_bin'], label='Theria', marker='o')

# Customize the plot
plt.title('Diversity Over Time: Late Cretaceous to Paleocene')
plt.xlabel('Time (Million years ago)')
plt.ylabel('Number of Occurrences (Diversity)')
plt.gca().invert_xaxis()  # To display the most recent times closer to the origin
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
