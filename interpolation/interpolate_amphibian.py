import pandas as pd
import numpy as np

# Sample data (for demonstration, replace this with your actual DataFrame)
data = pd.read_csv('./data/processed/taxon/Amphibian_Diversity.csv')

# Ensure the data is sorted by 'max_ma'
data.sort_values(by='max_ma', inplace=True)

# Define a function for linear interpolation between two points
def linear_interpolation(row1, row2, new_max_ma):
    ratio = (new_max_ma - row1['max_ma']) / (row2['max_ma'] - row1['max_ma'])
    interpolated_values = {}
    for col in ['n_occs']:  # Extend this list to include other columns you want to interpolate
        interpolated_values[col] = row1[col] + ratio * (row2[col] - row1[col])
    return interpolated_values

# List to hold interpolated rows
interpolated_rows = []

# Iterate through each pair of consecutive rows in the dataset
for i in range(len(data) - 1):
    row1 = data.iloc[i]
    row2 = data.iloc[i + 1]
    
    # Define the step for interpolation based on the difference between the max_ma values
    # This example uses a quarter of the interval for interpolation; adjust as needed
    step = (row2['max_ma'] - row1['max_ma']) / 4
    
    # Generate new max_ma values for interpolation within the interval
    new_max_mas = np.arange(row1['max_ma'] + step, row2['max_ma'], step)
    
    # Perform interpolation for each new max_ma value
    for new_max_ma in new_max_mas:
        interpolated_values = linear_interpolation(row1, row2, new_max_ma)
        interpolated_row = {'interval_name': f'Interpolated between {row1["interval_name"]} and {row2["interval_name"]}',
                            'max_ma': new_max_ma,
                            'min_ma': new_max_ma - step,  # Adjust this based on your specific needs
                            **interpolated_values}
        interpolated_rows.append(interpolated_row)

# Convert the list of new rows into a DataFrame
interpolated_data = pd.DataFrame(interpolated_rows)

# Concatenate the original data with the new interpolated data and sort
final_data = pd.concat([data, interpolated_data], ignore_index=True).sort_values(by='max_ma')

final_data.to_csv('./data/processed/taxon/interpolated/Amphibian_Diversity_interpolated.csv', index=False)
