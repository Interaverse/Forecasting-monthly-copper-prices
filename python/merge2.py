

import pandas as pd
import os

# Specify the directory where the CSV files are stored
directory = '../Original_Dataset'

# Initialize a DataFrame to hold the combined data
combined_df = None

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        df = pd.read_csv(filepath)
        
        # Convert the date column to datetime format (assumes your date column is named 'Date')
        df['Date'] = pd.to_datetime(df['Date'])

        # Generate a suffix from the filename (excluding the .csv extension)
        suffix = filename.replace('.csv', '')

        # Rename columns except 'Date' to include the suffix
        df.rename(columns=lambda x: x if x == 'Date' else x + '_' + suffix, inplace=True)

        # If combined_df is not None, merge, otherwise initialize it
        if combined_df is not None:
            # Merge the current df with the combined_df based on 'Date'
            combined_df = pd.merge(combined_df, df, on='Date', how='outer')
        else:
            combined_df = df

# Sort the combined DataFrame by the date column
combined_df = combined_df.sort_values(by='Date')

# Save the combined and sorted DataFrame to a new CSV file
combined_df.to_csv('../combined_sorted.csv', index=False)
