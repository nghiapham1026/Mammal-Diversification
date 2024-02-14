import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = pd.read_csv('../data/processed/climate/40mya_climate_data_reduced.csv');

# Convert time from kyr BP to MYA (Million years ago)
data['Time (MYA)'] = data['Time (kyr BP)'] / -1000

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data['Time (MYA)'], data['T_NH(deg C)'], label='T_NH (Mean Temperature Northern Hemisphere)', color='blue', marker='o')
plt.xlabel('Time (Million years ago)')
plt.ylabel('T_NH (°C)')
plt.title('Mean Temperature of the Northern Hemisphere Over Time')
plt.legend()
plt.grid(True)

# Invert the x-axis to show time from past to present
plt.xlim(max(data['Time (MYA)']), min(data['Time (MYA)']))

plt.show()
