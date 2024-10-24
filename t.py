import pandas as pd

# Load the CSV file
df = pd.read_csv('repositories.csv')

# Rename the column
df.rename(columns={'license': 'license_name'}, inplace=True)

# Save the updated DataFrame back to a CSV file
df.to_csv('repositories.csv', index=False)