import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

# Load the necessary datasets
climate_data_path = '../data/processed/climate/ConvertedTable.csv'
reptile_data_path = '../data/processed/taxon/interpolated/Reptile_Diversity_interpolated.csv'
animal_data_path = '../data/processed/taxon/interpolated/Animal_Diversity_interpolated.csv'

climate_df = pd.read_csv(climate_data_path)
reptile_df = pd.read_csv(reptile_data_path)
animal_df = pd.read_csv(animal_data_path)

# Preprocessing
climate_df = climate_df[['Time (Myr BP)', 'Ts']].dropna()  # Ensure there are no NaN values in 'Ts'
reptile_df = reptile_df[['max_ma', 'sampled_in_bin']].dropna()  # Ensure no NaN values in 'sampled_in_bin' for reptiles
animal_df = animal_df[['max_ma', 'sampled_in_bin']].dropna()  # Same for total animal data

# Merge reptile and total animal data on 'max_ma' to calculate the diversity ratio
diversity_ratio_df = pd.merge(reptile_df, animal_df, on='max_ma', suffixes=('_reptile', '_total'))
diversity_ratio_df['diversity_ratio'] = diversity_ratio_df['sampled_in_bin_reptile'] / diversity_ratio_df['sampled_in_bin_total']

# Merge the ratio data with climate data
merged_df = pd.merge_asof(diversity_ratio_df.sort_values('max_ma'), climate_df.sort_values('Time (Myr BP)'), left_on='max_ma', right_on='Time (Myr BP)', direction='nearest')

# Compute Pearson correlation coefficient between 'Ts' and the diversity ratio
correlation_coef, p_value = pearsonr(merged_df['Ts'], merged_df['diversity_ratio'])

print(f"Pearson correlation coefficient: {correlation_coef}")
print(f"P-value: {p_value}")

# Plotting
sns.set_style('whitegrid')  # Set seaborn style for better aesthetics
plt.figure(figsize=(10, 6))  # Set figure size

# Create scatter plot and regression line for 'Ts' vs. the diversity ratio
scatter_plot = sns.scatterplot(data=merged_df, x='Ts', y='diversity_ratio', color='blue', alpha=0.6, label='Diversity Ratio')
reg_line = sns.regplot(data=merged_df, x='Ts', y='diversity_ratio', scatter=False, color='red')

# Adding titles and labels
plt.title('Correlation between Surface Temperature and Reptile-to-Total Animal Diversity Ratio')
plt.xlabel('Surface Temperature (Ts)')
plt.ylabel('Reptile-to-Total Animal Diversity Ratio')

plt.legend()
plt.show()
