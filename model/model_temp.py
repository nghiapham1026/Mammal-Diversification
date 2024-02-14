import matplotlib.pyplot as plt
import pandas as pd

# Convert the string data to a DataFrame
df = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

# Plotting with inverted x-axis
plt.figure(figsize=(10, 6))
plt.plot(df['Time (Myr BP)'], df['Ts'], marker='o', linestyle='-', color='b')
plt.title('Temperature (Ts) over Geological Time')
plt.xlabel('Time (Myr BP)')
plt.ylabel('Temperature (Ts)')
plt.grid(True)
plt.gca().invert_xaxis()  # Inverting the x-axis
plt.show()