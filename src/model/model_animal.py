import pandas as pd
import matplotlib.pyplot as plt

# Assuming 'data' is your DataFrame
data = pd.read_csv('../../data/processed/taxon/Animal_Diversity.csv')
#data = pd.read_csv('../../data/processed/taxon/interpolated/Animal_Diversity_interpolated.csv')

# Sort the data by max_ma to ensure chronological order
data = data.sort_values(by='max_ma')

# Calculate the midpoint of each interval
data['midpoint_ma'] = (data['max_ma'] + data['min_ma']) / 2

# Plotting
plt.figure(figsize=(10, 6))
# Scatter plot for individual data points
plt.scatter(data['midpoint_ma'], data['n_occs'], color='blue', label='Number of Occurrences', s=40)  # Use a fixed size
# Line plot connecting the points
plt.plot(data['midpoint_ma'], data['n_occs'], color='red', label='Trend')

# Highlight zero occurrences
for index, row in data.iterrows():
    if row['n_occs'] == 0:
        plt.scatter(row['midpoint_ma'], row['n_occs'], color='green', s=40, label='Zero Occurrence' if index == data[data['n_occs'] == 0].index[0] else "")

plt.xlabel('Time (Million years ago)')
plt.ylabel('Number of Occurrences')
plt.title('Animal Diversity Over Time')
plt.gca().invert_xaxis()  # Invert x-axis to show recent times at the right
plt.grid(True)
plt.legend()
plt.show()
