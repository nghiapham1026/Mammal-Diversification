import pandas as pd

def add_midpoint_and_save(df, filepath):
    df['mid_ma'] = (df['min_ma'] + df['max_ma']) / 2
    df.to_csv(filepath, index=False)  # Save the dataframe without the index

# File paths for each dataset
filepaths = [
    '../data/processed/taxon/visualization/Artiodactyl.csv',
    '../data/processed/taxon/visualization/Carnivore.csv',
    '../data/processed/taxon/visualization/Cetacean.csv',
    '../data/processed/taxon/visualization/Perissodactyl.csv',
    '../data/processed/taxon/visualization/Primate.csv',
    '../data/processed/taxon/visualization/Proboscidea.csv',
    '../data/processed/taxon/visualization/Rodent.csv',
    '../data/processed/taxon/visualization/Ave.csv',
    '../data/processed/taxon/visualization/Reptile.csv',
    '../data/processed/taxon/visualization/Mammaliaformes.csv',
    '../data/processed/taxon/visualization/Multituberculate.csv',
    '../data/processed/taxon/visualization/Pantodont.csv',
    '../data/processed/taxon/visualization/Theria.csv'
]

# Load, process, and save each dataset
for filepath in filepaths:
    df = pd.read_csv(filepath)
    add_midpoint_and_save(df, filepath)