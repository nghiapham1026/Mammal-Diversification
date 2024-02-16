import pandas as pd
import numpy as np

def read_and_sort_data(file_path):
    data = pd.read_csv(file_path)
    data.sort_values(by='max_ma', inplace=True)
    return data

def linear_interpolation(row1, row2, new_max_ma):
    ratio = (new_max_ma - row1['max_ma']) / (row2['max_ma'] - row1['max_ma'])
    interpolated_values = {}
    for col in ['sampled_in_bin']:  # Extend this list to include other columns you want to interpolate
        interpolated_values[col] = row1[col] + ratio * (row2[col] - row1[col])
    return interpolated_values

def interpolate_data(data):
    interpolated_rows = []
    for i in range(len(data) - 1):
        row1 = data.iloc[i]
        row2 = data.iloc[i + 1]
        step = (row2['max_ma'] - row1['max_ma']) / 10
        new_max_mas = np.arange(row1['max_ma'] + step, row2['max_ma'], step)
        for new_max_ma in new_max_mas:
            interpolated_values = linear_interpolation(row1, row2, new_max_ma)
            interpolated_row = {'interval_name': f'Interpolated between {row1["interval_name"]} and {row2["interval_name"]}',
                                'max_ma': new_max_ma,
                                'min_ma': new_max_ma - step,
                                **interpolated_values}
            interpolated_rows.append(interpolated_row)
    interpolated_data = pd.DataFrame(interpolated_rows)
    return interpolated_data

def save_interpolated_data(original_data, interpolated_data, file_path):
    final_data = pd.concat([original_data, interpolated_data], ignore_index=True).sort_values(by='max_ma')
    final_data.to_csv(file_path, index=False)
