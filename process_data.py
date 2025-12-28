import pandas as pd
import os

# Path to the data folder
data_folder = "data"

# List all CSV files
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

# Empty list to store processed dataframes
dfs = []

for file in csv_files:
    path = os.path.join(data_folder, file)
    df = pd.read_csv(path)
    
    # Keep only Pink Morsels
    df = df[df['product'] == 'Pink Morsel']
    
    # Create Sales column
    df['Sales'] = df['quantity'] * df['price']
    
    # Keep only needed columns
    df = df[['Sales', 'date', 'region']]
    
    # Rename columns to match output
    df = df.rename(columns={'date': 'Date', 'region': 'Region'})
    
    dfs.append(df)

# Combine all files into one
final_df = pd.concat(dfs, ignore_index=True)

# Save to a new CSV
final_df.to_csv('formatted_output.csv', index=False)

print("Formatted CSV created: formatted_output.csv")