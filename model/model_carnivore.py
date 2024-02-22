import matplotlib.pyplot as plt
import pandas as pd
from model_utils import plot_taxon_with_context

fig, ax1 = plt.subplots(figsize=(14, 8))
carnivores_data = pd.read_csv('../data/processed/taxon/visualization/Carnivore.csv')

plot_taxon_with_context(carnivores_data, 'Carnivores', ax1)
plt.show()
