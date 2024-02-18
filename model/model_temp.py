import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Convert the string data to a DataFrame
df = pd.read_csv('../data/processed/climate/FilteredTableContinuous5Myr.csv')

# Set the plotting style for better aesthetics
sns.set_theme(style="whitegrid")

plt.figure(figsize=(12, 8))

# Create a list of unique epochs in the dataset for coloring
epochs = df['epoch'].unique()
colors = sns.color_palette("tab10", len(epochs))  # Generate a color palette

# Loop through each epoch to plot them with a different color
for epoch, color in zip(epochs, colors):
    epoch_df = df[df['epoch'] == epoch]
    plt.plot(epoch_df['Time (Myr BP)'], epoch_df['Ts'], marker='o', linestyle='-', color=color, label=epoch)

plt.title('Temperature (Ts) over Geological Time')
plt.xlabel('Time (Myr BP)')
plt.ylabel('Temperature (Ts)')
plt.legend(title="Epoch", bbox_to_anchor=(1.05, 1), loc='upper left')  # Place legend outside the plot

# Invert the x-axis to have the present time at the right
plt.gca().invert_xaxis()

plt.tight_layout()  # Adjust layout to make room for the legend
plt.show()
