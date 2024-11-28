import pandas as pd
import ast

# Function to load the dataset and split the Month column
def process_dataset(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)
    
    # Assuming the 'Month' column is the second column and contains strings of tuples
    # Convert the 'Month' column from string representations of tuples to actual tuples of floats
    df['Month'] = df.iloc[:, 1].apply(ast.literal_eval)
    
    # Split the tuples into two separate columns
    df['Month_cos'], df['Month_sin'] = zip(*df['Month'])
    
    # Drop the original 'Month' column as it's now redundant
    df.drop(columns=df.columns[1], inplace=True)
    
    # Return the updated DataFrame
    return df

#usage
file_path = "merged_dataset.csv"
processed_df = process_dataset(file_path)

# Display the first few rows of the updated dataset to verify the transformation
print(processed_df.head())

#save the new dataset to a CSV file
output_file_path = 'processed_merged.csv'  
processed_df.to_csv(output_file_path, index=False)
