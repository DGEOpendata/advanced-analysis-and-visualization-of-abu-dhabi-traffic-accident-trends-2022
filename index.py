python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data_path = 'Traffic_Accident_Data_Abu_Dhabi_2022.csv'
data = pd.read_csv(data_path)

# Data Overview
print(data.head())

# Data Cleaning (Example: Filling missing values for weather conditions)
data['Weather'].fillna('Unknown', inplace=True)

# Analyze peak accident times
accident_counts_by_hour = data.groupby(['Time']).size().reset_index(name='Accident Count')

# Plotting accident counts by time of day
plt.figure(figsize=(10, 6))
sns.lineplot(x='Time', y='Accident Count', data=accident_counts_by_hour)
plt.title('Traffic Accidents by Time of Day - Abu Dhabi, 2022')
plt.xlabel('Time of Day')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Correlation between weather and number of accidents
weather_accidents = data.groupby(['Weather']).size().reset_index(name='Accident Count')

# Plotting weather conditions vs accident count
plt.figure(figsize=(10, 6))
sns.barplot(x='Weather', y='Accident Count', data=weather_accidents, palette='viridis')
plt.title('Traffic Accidents by Weather Condition - Abu Dhabi, 2022')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

# Save cleaned data for further analysis
data.to_csv('Cleaned_Traffic_Accident_Data_Abu_Dhabi_2022.csv', index=False)
