import pandas as pd

# Load the dataset
file_path = '../../data/processed/climate/ConvertedTable.csv'
df = pd.read_csv(file_path)

start_time = df['Time (Myr BP)'].min()
# Find the max time to ensure we cover the entire range
max_time = df['Time (Myr BP)'].max()

# Generate a list of target times, starting from the first time value and adding 5 Myr continuously
target_times = [start_time + 1*i for i in range(int((max_time - start_time) // 1) + 1)]

# Find the closest actual time value in the dataset to each target time
filtered_indices = []
for target_time in target_times:
    # Find the index of the row with the time value closest to the target time
    closest_index = (df['Time (Myr BP)'] - target_time).abs().idxmin()
    if closest_index not in filtered_indices:
        filtered_indices.append(closest_index)

# Create a filtered DataFrame using the identified indices
filtered_df_continuous = df.loc[filtered_indices]

# Saving the continuously filtered dataset to a new CSV file
filtered_continuous_csv_path = '../../data/processed/climate/FilteredTableContinuous5Myr.csv'
filtered_df_continuous.to_csv(filtered_continuous_csv_path, index=False)

filtered_continuous_csv_path