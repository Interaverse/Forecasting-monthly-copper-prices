
import pandas as pd

def split_excel_data(file_path, train_ratio=0.8):
    # Load the Excel file
    df = pd.read_excel(file_path)
    
    # Calculate the split index
    split_index = int(len(df) * train_ratio)
    
    # Split the dataframe into training and testing sets
    train_df = df.iloc[:split_index]
    test_df = df.iloc[split_index:]
    
    # the training and testing sets to new Excel files
    train_df.to_excel('../training_data.xlsx', index=False)
    test_df.to_excel('../testing_data.xlsx', index=False)
    print(f"Training data saved to 'training_data.xlsx'")
    print(f"Testing data saved to 'testing_data.xlsx'")

# Example usage
split_excel_data('../raw_shortened.xlsx')  
