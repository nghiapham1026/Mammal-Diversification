import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

# Load the necessary datasets
reptile_data_path = '../data/processed/taxon/interpolated/Reptile_Diversity_interpolated.csv'
mammal_data_path = '../data/processed/taxon/interpolated/Mammal_Diversity_interpolated.csv'
animal_data_path = '../data/processed/taxon/interpolated/Animal_Diversity_interpolated.csv'

reptile_df = pd.read_csv(reptile_data_path)
mammal_df = pd.read_csv(mammal_data_path)
animal_df = pd.read_csv(animal_data_path)

# Ensure no NaN values in 'sampled_in_bin' for both datasets
reptile_df = reptile_df[['max_ma', 'sampled_in_bin']].dropna()
mammal_df = mammal_df[['max_ma', 'sampled_in_bin']].dropna()
animal_df = animal_df[['max_ma', 'sampled_in_bin']].dropna()

# Calculate diversity ratios
reptile_ratio_df = pd.merge(reptile_df, animal_df, on='max_ma', suffixes=('_reptile', '_total'))
reptile_ratio_df['diversity_ratio_reptile'] = reptile_ratio_df['sampled_in_bin_reptile'] / reptile_ratio_df['sampled_in_bin_total']

mammal_ratio_df = pd.merge(mammal_df, animal_df, on='max_ma', suffixes=('_mammal', '_total'))
mammal_ratio_df['diversity_ratio_mammal'] = mammal_ratio_df['sampled_in_bin_mammal'] / mammal_ratio_df['sampled_in_bin_total']

# Merge reptile and mammal ratios on 'max_ma'
merged_diversity_df = pd.merge(reptile_ratio_df[['max_ma', 'diversity_ratio_reptile']], mammal_ratio_df[['max_ma', 'diversity_ratio_mammal']], on='max_ma')

# Compute Pearson correlation coefficient between reptile and mammal diversity ratios
correlation_coef, p_value = pearsonr(merged_diversity_df['diversity_ratio_reptile'], merged_diversity_df['diversity_ratio_mammal'])

print(f"Pearson correlation coefficient between reptile and mammal diversity ratios: {correlation_coef}")
print(f"P-value: {p_value}")

# Plotting
sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))

# Scatter plot for reptile vs. mammal diversity ratios
sns.scatterplot(data=merged_diversity_df, x='diversity_ratio_reptile', y='diversity_ratio_mammal', color='blue', alpha=0.6, label='Diversity Ratios')

# Optional: Add regression line
sns.regplot(data=merged_diversity_df, x='diversity_ratio_reptile', y='diversity_ratio_mammal', scatter=False, color='red')

# Adding titles and labels
plt.title('Correlation between Reptile and Mammal Diversity Ratios Over Time')
plt.xlabel('Reptile Diversity Ratio')
plt.ylabel('Mammal Diversity Ratio')

plt.legend()
plt.show()
