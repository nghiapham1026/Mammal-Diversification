import matplotlib.pyplot as plt
import pandas as pd
from model_utils import plot_taxon_with_context

fig, ax1 = plt.subplots(figsize=(14, 8))
mammals_data = pd.read_csv('../data/processed/taxon/Mammal_Diversity.csv')

mammals_data['mid_ma'] = (mammals_data['max_ma'] + mammals_data['min_ma']) / 2
plot_taxon_with_context(mammals_data, 'Mammals', ax1)
plt.show()
