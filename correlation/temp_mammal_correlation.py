import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import seaborn as sns

# Load climate data
climate_data_path = '../data/processed/climate/ConvertedTable.csv'
climate_df = pd.read_csv(climate_data_path)

# Load mammal data
mammal_data_path = '../data/processed/taxon/interpolated/Mammal_Diversity_interpolated.csv'
mammal_df = pd.read_csv(mammal_data_path)

# Preprocessing
# Assuming 'Time (Myr BP)' from climate data matches with 'max_ma' from mammal data
# Adjust the columns as necessary based on how you wish to merge (e.g., mean, max, or specific time points)
climate_df = climate_df[['Time (Myr BP)', 'Ts']].dropna()  # Drop rows where Ts is NaN
mammal_df = mammal_df[['max_ma', 'n_occs']].dropna()  # Drop rows where n_occs is NaN

# Simple merge (example, might need adjustment for exact match)
# This example assumes an exact match is not required, and uses the closest available time point
# For a more sophisticated merge strategy, consider interpolating or matching based on nearest values

# Convert climate time to a format that can match mammal_df's max_ma for direct comparison
climate_df['Time (Myr BP)'] = climate_df['Time (Myr BP)'].round(2)

# Merge on closest time value
merged_df = pd.merge_asof(mammal_df.sort_values('max_ma'), climate_df.sort_values('Time (Myr BP)'), left_on='max_ma', right_on='Time (Myr BP)', direction='nearest')

# Compute Pearson correlation coefficient
correlation_coef, p_value = pearsonr(merged_df['Ts'], merged_df['n_occs'])

print(f"Pearson correlation coefficient: {correlation_coef}")
print(f"P-value: {p_value}")

# Set the style of seaborn for better aesthetics
sns.set_style('whitegrid')

# Create a scatter plot with a regression line
plt.figure(figsize=(10, 6))  # Set figure size
scatter_plot = sns.scatterplot(data=merged_df, x='Ts', y='n_occs', color='blue', alpha=0.6)
reg_line = sns.regplot(data=merged_df, x='Ts', y='n_occs', scatter=False, color='red')

# Adding titles and labels
plt.title('Correlation between Surface Temperature and Mammal Diversity')
plt.xlabel('Surface Temperature (Ts)')
plt.ylabel('Mammal Diversity (Number of Occurrences)')

# Show plot
plt.show()
