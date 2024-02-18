import pandas as pd

# Define a function to map time to geological epochs
def map_time_to_epoch(time_myr):
    if time_myr <= 0.0117:
        return 'Holocene'
    elif time_myr <= 2.58:
        return 'Pleistocene'
    elif time_myr <= 5.333:
        return 'Pliocene'
    elif time_myr <= 23.03:
        return 'Miocene'
    elif time_myr <= 33.9:
        return 'Oligocene'
    elif time_myr <= 56.0:
        return 'Eocene'
    elif time_myr <= 66.0:
        return 'Paleocene'
    else:
        return 'Late Cretaceous'

# Load the dataset
file_path = '../data/processed/climate/ConvertedTable.csv'
df = pd.read_csv(file_path)

# Apply the mapping function to each row in the DataFrame
df['epoch'] = df['Time (Myr BP)'].apply(map_time_to_epoch)

# Follow the previous steps to filter and save the dataset
start_time = df['Time (Myr BP)'].min()
max_time = df['Time (Myr BP)'].max()

target_times = [start_time + 0.5*i for i in range(int((max_time - start_time) // 0.5) + 1)]

filtered_indices = []
for target_time in target_times:
    closest_index = (df['Time (Myr BP)'] - target_time).abs().idxmin()
    if closest_index not in filtered_indices:
        filtered_indices.append(closest_index)

filtered_df_continuous = df.loc[filtered_indices]

# Saving the continuously filtered dataset to a new CSV file
filtered_continuous_csv_path = '../data/processed/climate/FilteredTableContinuous5Myr.csv'
filtered_df_continuous.to_csv(filtered_continuous_csv_path, index=False)