import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('hourly_traffic_data_02_17_to_23.csv')

# Filter rows where detector_id is 'AID01101'
filtered_df = df[df['detector_id'] == 'AID07221']

filtered_df2 = filtered_df[filtered_df['lane_id'] == 'Fast Lane']

df = filtered_df2

# Assuming your dataframe is named df
df['period_from'] = pd.to_datetime(df['period_from'])

df.set_index('period_from', inplace=True)

# Create the plot
plt.figure(figsize=(12, 6))  # Set the figure size
plt.scatter(df.index, df['total_volume'], color='blue', label='Total Volume')  # Scatter plot
plt.title('Total Volume Over Time')  # Add a title
plt.xlabel('Time')  # Label the x-axis
plt.ylabel('Total Volume')  # Label the y-axis
plt.legend()  # Add a legend
plt.grid(True)  # Add a grid for better readability
plt.show()  # Display the plot