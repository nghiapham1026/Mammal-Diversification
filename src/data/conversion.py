import csv

# Define the header based on the information starting from line 8
header = ["Time (Myr BP)", "delta_18O (0/00)", "Time_mean (Myr BP)", "delta_18O_mean (0/00)", "Tdo", "Ts", "SL"]

# Open the text file to read data
with open('../../data/raw/climate/Table.txt', 'r') as text_file:
    # Skip the first seven lines of the file
    for _ in range(7):
        next(text_file)
    # Read the rest of the lines after the header
    lines = text_file.readlines()

# Initialize a list to hold the processed data, starting with the header
data = [header]

# Process each line in the text file
for line in lines:
    # Check if the line contains numeric data. This is a basic check and assumes that valid data lines contain numbers.
    if line.strip() and any(char.isdigit() for char in line):
        # Split the line into components based on whitespace
        row = line.split()
        # Append the processed row to the data list
        data.append(row)

# Define the path for the output CSV file
csv_file_path = '../../data/processed/climate/ConvertedTable.csv'

# Write the processed data to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Write the data rows to the CSV, starting with the header
    for row in data:
        writer.writerow(row)
