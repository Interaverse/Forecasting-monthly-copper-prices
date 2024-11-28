import pandas as pd
from os import listdir
from os.path import isfile, join

# Assuming the provided dataset is loaded
provided_df = pd.read_csv('Copper Price clean.csv')  # Update the path as necessary

# Assuming column 0 is Year and column 1 is Month in all datasets
provided_df.rename(columns={provided_df.columns[0]: 'Year', provided_df.columns[1]: 'Month'}, inplace=True)

csv_directory = 'Processed_Dataset'  # Update this to your actual directory

# Placeholder for the merged DataFrame
merged_df = provided_df.copy()

# Iterate over CSV files in the directory
for filename in listdir(csv_directory):
    if filename.endswith('.csv'):
        file_path = join(csv_directory, filename)
        other_df = pd.read_csv(file_path)
        
        # Rename columns for merging
        other_df.rename(columns={other_df.columns[0]: 'Year', other_df.columns[1]: 'Month'}, inplace=True)
        
        # Merge using the renamed columns
        merged_df = pd.merge(merged_df, other_df, on=['Year', 'Month'], how='left')

# After merging, save to a new CSV file
merged_df.to_csv('merged_dataset.csv', index=False)


