import matplotlib.pyplot as plt
import pandas as pd
from model_utils import plot_taxon_with_context

fig, ax1 = plt.subplots(figsize=(14, 8))
condylarths_data = pd.read_csv('../data/processed/taxon/visualization/Condylarth.csv')

plot_taxon_with_context(condylarths_data, 'Condylarths', ax1)
plt.show()
