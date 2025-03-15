

import pandas as pd
import folium
from folium.plugins import HeatMapWithTime
from folium.plugins import HeatMap

# Step 1: Load the CSV file into a DataFrame
df_traffic = pd.read_csv('hourly_traffic_data_02_17_to_23.csv')


# Step 1: Load the CSV file into a DataFrame
df_location = pd.read_csv('detectors.csv')

# Assuming df_traffic is your traffic data and df_location is your location data
df_merged = pd.merge(df_traffic, df_location, left_on='detector_id', right_on='AID_ID_Number', how='left')

# Group by the specified columns and perform aggregations
df_merged = df_merged.groupby(['period_from', 'detector_id', 'direction']).agg(
    average_speed=('average_speed', 'mean'),
    average_occupancy=('average_occupancy', 'mean'),
    total_volume=('total_volume', 'sum'),
    Latitude=('Latitude', 'mean'),
    Longitude=('Longitude', 'mean')
).reset_index()

print(df_merged)

df_merged = df_merged[df_merged['period_from'] == "2025-02-17 15"]
# Assuming your dataframe is named df
df_merged['period_from'] = pd.to_datetime(df_merged['period_from']+":00:00")


# Create a base map centered around the mean latitude and longitude
map_center = [df_merged['Latitude'].mean(), df_merged['Longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=12)

# Add smaller CircleMarkers for each location
for idx, row in df_merged.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=0.75,  # Adjust the size of the marker
        color='blue',  # Outline color
        fill=True,
        fill_color='blue',  # Fill color
        fill_opacity=0.7,  # Transparency of the fill
        popup=f"Detector: {row['detector_id']}<br>Speed: {row['average_speed']}"
    ).add_to(m)

# Display the map
m.save('small_markers_map.html')
