import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'data' is your DataFrame
#data = pd.read_csv('../../data/processed/taxon/Insect_Diversity.csv')
data = pd.read_csv('../../data/processed/taxon/interpolated/Insect_Diversity_interpolated.csv')

# Sort the data by max_ma to ensure chronological order
data = data.sort_values(by='max_ma')

# Plotting
plt.figure(figsize=(10, 6))
# Scatter plot for individual data points
plt.scatter(data['max_ma'], data['n_occs'], color='blue', label='Number of Occurrences', s=20, alpha=0.5)  # Use a fixed size
# Line plot connecting the points
plt.plot(data['max_ma'], data['n_occs'], color='red', label='Trend')

plt.xlabel('Time (Million years ago)')
plt.ylabel('Number of Occurrences')
plt.title('Insect Diversity Over Time')
plt.gca().invert_xaxis()  # Invert x-axis to show recent times at the right
plt.grid(True)
plt.legend()
plt.show()
