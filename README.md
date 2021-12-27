# Surf's Up Weather Analysis
## Overview and Purpose
An entrepreneuer has the desire to open an ice cream surf shop in Oahu, Hawaii, but before committing to it needs the weather data for the months of June and Decemeber to see how seasonal weather changes may impact location suitability. All the necessary information to complete this task was provided within the hawaii.sqlite file. Pandas, numpy, matplotlib, and sqlalchemy were used to analyze the data.

## Results
### Oahu June Analysis
The Pandas 'describe()' method was used to gather the summary statistics for June, which showed:
  - 1,700 temperature records were logged between the nine weather stations
  - The average temperature was 74.9°F
  - The recorded low temperature was 64°F
  - The recorded high temperature was 85°F

![june_temp_hist](https://user-images.githubusercontent.com/92493572/147423325-a303fe12-aaac-490e-ae1c-fc1624abf369.png)
![june_temp_summary_stats](https://user-images.githubusercontent.com/92493572/147423312-b481330b-ceaf-4cf2-98a6-0753f28a7a5e.png)

#### June Precipitation
The precipitation data was queried and grouped by station ID, and then subsequently inserted into a new dataframe that also calculated the percentage of days that had rained. The new dataframe displayed the number of weather recordings because multiple stations had significantly less recordings than the most active stations.

![june_rain_by_station](https://user-images.githubusercontent.com/92493572/147423567-cde4b524-5b1a-48f8-a909-a8a8eb76a1a9.png)
![june_rainy_days](https://user-images.githubusercontent.com/92493572/147423568-547091db-54cd-461d-ac48-eb8d5fa9952d.png)

Percent of days that rained and average daily precipitation:
  - USC00517948: 21.6%   --   0.058 inches/day
  - USC00511918: 26.7%   --   0.015 inches/day
  - USC00519397: 31.4%   --   0.023 inches/day

### Oahu December Analysis
The Pandas 'describe()' method was used to gather the summary statistics for December, which showed:
  - 1,517 temperature records were logged between the nine weather stations
  - The average temperature was 71°F
  - The recorded low temperature was 56°F
  - The recorded high temperature was 83°F

![dec_temp_hist](https://user-images.githubusercontent.com/92493572/147424089-a52d2700-ad6e-40c1-ac20-2ccefc077c6a.png)
![dec_temp_summary_stats](https://user-images.githubusercontent.com/92493572/147424094-40359df5-ec07-4603-b3a1-65786a4b1d55.png)

#### December Precipitation
The precipitation data was queried and grouped by station ID, and then subsequently inserted into a new dataframe that also calculated the percentage of days that had rained. The new dataframe displayed the number of weather recordings because multiple stations had significantly less recordings than the most active stations.

![dec_rain_by_station](https://user-images.githubusercontent.com/92493572/147424125-e9f3a692-49b2-49f3-9dc6-18e7c64c0353.png)
![dec_rainy_days](https://user-images.githubusercontent.com/92493572/147424128-a9c395b7-0a72-47c3-bef2-6345322533e2.png)


Percent of days that rained and average daily precipitation:
  - USC00517948: 25.7%   --   0.058 inches/day
  - USC00511918: 36.2%   --   0.015 inches/day
  - USC00519397: 46.7%   --   0.075 inches/day

