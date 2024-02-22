import matplotlib.pyplot as plt
import pandas as pd
from model_utils import plot_taxon_with_context

fig, ax1 = plt.subplots(figsize=(14, 8))
reptiles_data = pd.read_csv('../data/processed/taxon/Reptile_Diversity.csv')

reptiles_data['mid_ma'] = (reptiles_data['max_ma'] + reptiles_data['min_ma']) / 2
plot_taxon_with_context(reptiles_data, 'Reptiles', ax1)
plt.show()
