import pandas as pd
import numpy as np

# Sample data (for demonstration, replace this with your actual DataFrame)
data = pd.read_csv('../../data/processed/taxon/Reptile_Diversity.csv')

# Sort the data by max_ma to ensure chronological order
data = data.sort_values(by='max_ma')

# Initialize an empty list to hold new rows
new_rows = []

# Define the interpolation step (5 million years)
step = 5.0
max_value = data['max_ma'].max()
current_value = 0

while current_value <= max_value:
    # Find rows that bound the current interpolation point
    lower_bound_rows = data[data['max_ma'] <= current_value]
    upper_bound_rows = data[data['min_ma'] >= current_value]
    
    if not lower_bound_rows.empty and not upper_bound_rows.empty:
        lower_row = lower_bound_rows.iloc[-1]
        upper_row = upper_bound_rows.iloc[0]
        
        # Perform linear interpolation
        if lower_row['max_ma'] != upper_row['min_ma']:  # Avoid division by zero
            ratio = (current_value - lower_row['max_ma']) / (upper_row['min_ma'] - lower_row['max_ma'])
            interpolated_n_occs = lower_row['n_occs'] + ratio * (upper_row['n_occs'] - lower_row['n_occs'])
        else:
            interpolated_n_occs = lower_row['n_occs']
        
        new_row = {
            'interval_name': f'Interpolated at {current_value} Ma',
            'max_ma': current_value,
            'min_ma': current_value - step,
            'n_occs': interpolated_n_occs
        }
        new_rows.append(new_row)
    
    current_value += step

# Convert the list of new rows into a DataFrame
interpolated_data = pd.DataFrame(new_rows)

# Concatenate the original data with the new interpolated data
final_data = pd.concat([data, interpolated_data], ignore_index=True).sort_values(by='max_ma')

final_data.to_csv('../../data/processed/taxon/interpolated/Reptile_Diversity_interpolated.csv', index=False)

# Display the final data
print(final_data)
