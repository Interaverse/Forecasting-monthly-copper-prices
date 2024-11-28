from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Example: Load your training and testing data
train_data = pd.read_excel('../updated_training_data.xlsx')
test_data = pd.read_excel('../updated_testing_data.xlsx')

# Exclude non-numeric columns if present
exclude_columns = ['Date', 'Month', 'Year']  # Adjust based on your dataset
columns_to_scale = [col for col in train_data.columns if col not in exclude_columns]

# Initialize the MinMaxScaler
scaler = MinMaxScaler(feature_range=(-1, 1))

# Fit the scaler on the training data
scaler.fit(train_data[columns_to_scale])

# Transform the training data
train_data[columns_to_scale] = scaler.transform(train_data[columns_to_scale])

# Transform the testing data using the same scaler
test_data[columns_to_scale] = scaler.transform(test_data[columns_to_scale])

# Optionally, save the scaled data
train_data.to_excel('../scaled_training_data.xlsx', index=False)
test_data.to_excel('../scaled_testing_data.xlsx', index=False)
