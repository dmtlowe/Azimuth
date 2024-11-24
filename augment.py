import os
import pandas as pd
import numpy as np
from glob import glob
from tqdm import tqdm

# Define the data folder
data_folder = 'data'  # Change this to your data folder path

# Get all CSV files in the data folder
path = os.path.join(data_folder, '*.csv')
csv_files = glob(os.path.join(data_folder, '*.csv'))
print(os.path.exists(path))
# Initialize a list to store data from all CSV files
data_list = []

# Read each CSV file and append to the data list
for file in csv_files:
    df = pd.read_csv(file)
    data_list.append(df)

# Concatenate all data into a single DataFrame
data = pd.concat(data_list, ignore_index=True)

# Define feature columns and label column
feature_columns = [col for col in data.columns if col != 'Label']
label_column = 'Label'

# Function to add Gaussian noise with a specified standard deviation
def add_gaussian_noise(signal, std_dev):
    noise = np.random.normal(0, std_dev, signal.shape)
    augmented_signal = signal + noise
    # Clip the values to stay within the 8-bit signed integer range
    augmented_signal = np.clip(augmented_signal, -128, 127)
    return augmented_signal.astype(np.int8)

# Levels of Gaussian noise to add (standard deviations)
noise_levels = [2]  # You can adjust these values as needed

# Initialize a list to store augmented data
augmented_data = []

# Loop over each sample and apply Gaussian noise at different levels
for idx, row in tqdm(data.iterrows(), total=data.shape[0], desc="Augmenting data"):
    signal = row[feature_columns].values.astype(np.int8)
    label = row[label_column]
    augmented_data.append(row.to_dict())  # Include original data

    for std_dev in noise_levels:
        augmented_signal = add_gaussian_noise(signal, std_dev)
        # Create a new augmented data row
        augmented_row = {feature_columns[i]: augmented_signal[i] for i in range(len(feature_columns))}
        augmented_row[label_column] = label
        augmented_data.append(augmented_row)

# Create a DataFrame from the augmented data
augmented_df = pd.DataFrame(augmented_data)

# Save the augmented data to a new CSV file
augmented_df.to_csv('augmented_data.csv', index=False)

print("Data augmentation complete. Augmented data saved to 'augmented_data.csv'.")