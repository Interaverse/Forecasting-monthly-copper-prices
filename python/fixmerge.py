import pandas as pd

# Load the combined CSV file
file_path = '../combined_sorted.csv'
combined_data = pd.read_csv(file_path)

# Convert the 'Date' column to datetime format, coercing any parsing errors to NaT (not a time)
combined_data['Date'] = pd.to_datetime(combined_data['Date'], errors='coerce')

# Check for any rows where date conversion might have failed (resulting in NaT values)
if combined_data['Date'].isna().any():
    print("There are rows with date parsing issues.")
else:
    print("All dates have been converted successfully.")

# Save the DataFrame with corrected dates to a new CSV file
corrected_file_path = '../corrected_combined_sorted.csv'
combined_data.to_csv(corrected_file_path, index=False)

print(f"Data saved to {corrected_file_path}.")
