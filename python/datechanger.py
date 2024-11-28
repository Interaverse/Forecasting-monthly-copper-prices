import pandas as pd
from datetime import datetime

# Define the path to the input and output CSV files
input_csv_path = '../Original_Dataset/Iron.csv'
output_csv_path = '../Iron.csv'

# Read the CSV file
df = pd.read_csv(input_csv_path)

# Function to change date format from day/month/year to month/day/year
def convert_date_format(date_str):
    try:
        return datetime.strptime(date_str, '%d/%m/%Y').strftime('%m/%d/%Y')
    except ValueError:
        return date_str  # Return the original string if conversion fails

# Apply the date format conversion to the first column
df.iloc[:, 0] = df.iloc[:, 0].apply(convert_date_format)

# Write the modified DataFrame back to a new CSV file
df.to_csv(output_csv_path, index=False)

print('CSV file has been processed and the new file is saved.')
