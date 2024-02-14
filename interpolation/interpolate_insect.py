from interpolate_utils import read_and_sort_data, interpolate_data, save_interpolated_data

file_path = '../data/processed/taxon/Insect_Diversity.csv'
interpolated_file_path = '../data/processed/taxon/interpolated/Insect_Diversity_interpolated.csv'

data = read_and_sort_data(file_path)
interpolated_data = interpolate_data(data)
save_interpolated_data(data, interpolated_data, interpolated_file_path)
