import pandas as pd

# Load the dataset
df = pd.read_csv('Resources_Output/storm_data.csv')

# Convert BEGIN_DATE_TIME to datetime
df['BEGIN_DATE_TIME'] = pd.to_datetime(df['BEGIN_DATE_TIME'])

# Filter out rows with BEGIN_DATE_TIME before the year 2000
df_filtered = df[df['BEGIN_DATE_TIME'].dt.year >= 2000]

# Save the filtered DataFrame to a new CSV file (optional)
df_filtered.to_csv('Resources_Output/storm_data_filtered.csv', index=False)

