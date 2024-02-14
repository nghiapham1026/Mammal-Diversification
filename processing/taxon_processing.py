import pandas as pd

def filter_and_save_dataset(input_file_path, skip_lines, output_file_path):
    # Load the dataset, skipping the specified number of lines
    df = pd.read_csv(input_file_path, skiprows=skip_lines)

    # Save the filtered data to the specified output file, without the index
    df.to_csv(output_file_path, index=False)


# Call the function with the specified parameters
filter_and_save_dataset('../data/raw/taxon/Amphibian_Diversity.csv', 23, '../data/processed/taxon/Amphibian_Diversity.csv')
filter_and_save_dataset('../data/raw/taxon/Animal_Diversity.csv', 23, '../data/processed/taxon/Animal_Diversity.csv')
filter_and_save_dataset('../data/raw/taxon/Insect_Diversity.csv', 23, '../data/processed/taxon/Insect_Diversity.csv')
filter_and_save_dataset('../data/raw/taxon/Mammal_Diversity.csv', 23, '../data/processed/taxon/Mammal_Diversity.csv')
filter_and_save_dataset('../data/raw/taxon/Reptile_Diversity.csv', 23, '../data/processed/taxon/Reptile_Diversity.csv')
