import pandas as pd

# Load CSV
df = pd.read_csv('uber.csv')

# Show basic data
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Convert datetime
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

# Extract time features
df['hour'] = df['pickup_datetime'].dt.hour
df['day'] = df['pickup_datetime'].dt.day_name()

# Create pickup location column
df['pickup_location'] = df['pickup_latitude'].astype(str) + "," + df['pickup_longitude'].astype(str)

# Most frequent pickup points
print(df['pickup_location'].value_counts().head())

# Group by location
pickup_counts = df.groupby('pickup_location').size()
print(pickup_counts)
