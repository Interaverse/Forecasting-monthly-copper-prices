import pandas as pd
import numpy as np

def cyclical_encode_month(df, month_col):
    # Create two new columns for the sine and cosine transforms of the month
    df['month_sin'] = np.round(np.sin(2 * np.pi * df['Month']/12), 10)
    df['month_cos'] = np.round(np.cos(2 * np.pi * df['Month']/12), 10)

    
    # Drop the original month column
    df.drop(month_col, axis=1, inplace=True)
    
    return df

def process_excel_file(input_file_path, output_file_path, month_col):
    # Read the Excel file
    df = pd.read_excel(input_file_path)
    
    # Encode the month column cyclically
    df = cyclical_encode_month(df, month_col)
    
    # Write the modified dataframe to a new Excel file
    df.to_excel(output_file_path, index=False)
    print("File processed and saved to:", output_file_path)

# Example usage
input_path = '../scaled_testing_data-11.xlsx'
output_path = '../testing_data-11.xlsx'
month_column = 'Month'  # Change this to the name of your month column if different

process_excel_file(input_path, output_path, month_column)

