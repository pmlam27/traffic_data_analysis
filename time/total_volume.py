import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('hourly_traffic_data_02_17_to_23.csv')

# Group by the specified columns and perform aggregations
df = df.groupby(['period_from']).agg(
    total_volume=('total_volume', 'sum')
).reset_index()

print(df)

# Convert 'period_from' to datetime and extract date and hour
df['period_from'] = pd.to_datetime(df['period_from']+":00:00")
df['date'] = df['period_from'].dt.date
df['hour'] = df['period_from'].dt.hour

print(df)

# Scale the total_volume to represent thousands
df['total_volume'] = df['total_volume'] / 1000

# Pivot the data to create a table with dates as rows, hours as columns, and total_volume as values
pivot_table = df.pivot_table(index='date', columns='hour', values='total_volume', aggfunc='sum')

# Create the heatmap
plt.figure(figsize=(15, 8))  # Increase the figure size (width, height)
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap="YlGnBu", linewidths=0.5)
plt.title('Total Volume by Date and Hour (in Thousands)')
plt.xlabel('Hour')
plt.ylabel('Date')
# Save the heatmap as an image
plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')  # Saves as a PNG file
plt.show()
