from lxml import etree
import csv
import pandas as pd
import os

class TrafficData:
    def __init__(self):
        self.records = []

    def add_record(self, date, period_from, period_to, detector_id, direction, lane_id, speed, occupancy, volume, sd, valid):
        record = {
            'date': date,
            'period_from': period_from,
            'period_to': period_to,
            'detector_id': detector_id,
            'direction': direction,
            'lane_id': lane_id,
            'speed': speed,
            'occupancy': occupancy,
            'volume': volume,
            's.d.': sd,
            'valid': valid
        }
        self.records.append(record)
    
    def convert_to_data_frame(self):
        self.df = pd.DataFrame(self.records)

    def add_XML_as_record(self, file_path):
        root = etree.parse(file_path).getroot()
        # Extract the date
        date = root.find('date').text

        # Iterate over periods
        for period in root.find('periods'):
            period_from = period.find('period_from').text
            period_to = period.find('period_to').text

            # Iterate over detectors
            for detector in period.find('detectors'):
                detector_id = detector.find('detector_id').text
                direction = detector.find('direction').text
                # Iterate over lanes
                for lane in detector.find('lanes'):
                    lane_id = lane.find('lane_id').text
                    speed = lane.find('speed').text
                    occupancy = lane.find('occupancy').text
                    volume = lane.find('volume').text
                    sd = lane.find('s.d.').text
                    valid = lane.find('valid').text

                    traffic_data.add_record(
                        date, period_from, period_to, detector_id, direction, lane_id,
                        speed, occupancy, volume, sd, valid
                    )

traffic_data = TrafficData()

folder_path = "202502/"

count = 0
for filename in os.listdir(folder_path):
    if filename.endswith('.xml') and filename.startswith('202502'):
        if (filename.startswith('20250217') or 
            filename.startswith('20250218') or 
            filename.startswith('20250219') or 
            filename.startswith('20250220') or 
            filename.startswith('20250221') or 
            filename.startswith('20250222') or
            filename.startswith('20250223')):
            full_path = os.path.join(folder_path, filename)
            print(full_path)
            count += 1
            traffic_data.add_XML_as_record(full_path)

traffic_data.convert_to_data_frame()
print(traffic_data.df)

# Export the DataFrame to a CSV file
traffic_data.df.to_csv('traffic_data_2025_02_17_to_23.csv', index=False)

print(count)
