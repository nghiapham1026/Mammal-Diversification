import matplotlib.pyplot as plt
import pandas as pd
from model_utils import plot_taxon_with_context

fig, ax1 = plt.subplots(figsize=(14, 8))
plesiadapiformes_data = pd.read_csv('../data/processed/taxon/visualization/Plesiadapiformes.csv')

plot_taxon_with_context(plesiadapiformes_data, 'Plesiadapiformes', ax1)
plt.show()
