import re

def convert_txt_to_csv(input_file_path, output_file_path):
    # Open the input file and the output file
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        # Write the CSV header
        outfile.write("Time (kyr BP),Sea level (m),T_NH(deg C),T_dw (deg C),delta_w,delta_T\n")
        
        # Read through each line in the file
        for line in infile:
            # Skip lines that do not contain data values (i.e., start with a non-numeric character)
            if re.match(r'^\s*-', line):
                # Remove multiple spaces and replace them with a single comma
                cleaned_line = re.sub(r'\s+', ',', line.strip())
                # Write the cleaned line to the output file
                outfile.write(cleaned_line + "\n")

# Example usage
input_file_path = '../data/raw/climate/BdeBoer_etal_1Dmodel_output.txt'  # Update this to the path of your text file
output_file_path = '../data/processed/climate/40mya_climate_data.csv'  # Update this to your desired output CSV file path

convert_txt_to_csv(input_file_path, output_file_path)
