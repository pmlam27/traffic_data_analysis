import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('new_hourly_traffic_data_02_17_to_23.csv')

# Filter rows where detector_id is 'AID01101'
filtered_df = df[df['detector_id'] == 'AID07221']

filtered_df2 = filtered_df[filtered_df['lane_id'] == 'Fast Lane']

# Display the modified DataFrame
print(filtered_df2)

# Convert 'period_from' to datetime
filtered_df2['period_from'] = pd.to_datetime(filtered_df2['period_from']+":00:00")

# Sort by 'period_from' (optional but recommended for proper plotting)
df = df.sort_values('period_from')

# Plot the total volume over time
plt.figure(figsize=(10, 6))
plt.plot(df['period_from'], df['total_volume'], marker='o', linestyle='-', color='b')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Total Volume')
plt.title('Total Volume Over Time (Detector ID: AID07221, Lane: Fast Lane)')
plt.grid(True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()