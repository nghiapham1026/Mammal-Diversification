import matplotlib.pyplot as plt
import pandas as pd
from model_utils import plot_taxon_with_context

fig, ax1 = plt.subplots(figsize=(14, 8))
multituberculates_data = pd.read_csv('../data/processed/taxon/visualization/Multituberculate.csv')

plot_taxon_with_context(multituberculates_data, 'Multituberculates', ax1)
plt.show()
