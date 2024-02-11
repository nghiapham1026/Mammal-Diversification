import pandas as pd

def filter_dataset(input_file_path, output_file_path):
    # Load the data
    data = pd.read_csv(input_file_path)
    
    # Filter out rows with "Time (kyr BP)" not ending in .00 (keeping whole numbers)
    data = data[data['Time (kyr BP)'].apply(lambda x: x == int(x))]
    
    # Now that we've ensured all values are whole numbers, convert "Time (kyr BP)" to integer
    data['Time (kyr BP)'] = data['Time (kyr BP)'].astype(int)
    
    # Filter rows to keep only those at 100 thousand years increments
    filtered_data = data[data['Time (kyr BP)'] % 100 == 0]
    
    # Save the filtered data to a new CSV file
    filtered_data.to_csv(output_file_path, index=False)

# Example usage
input_file_path = '../../data/processed/climate/40mya_climate_data.csv'  # Update this to the path of your text file
output_file_path = '../../data/processed/climate/40mya_climate_data_reduced.csv'  # Update this to your desired output CSV file path

filter_dataset(input_file_path, output_file_path)
