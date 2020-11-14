# %%
# Initial Imports
import pandas as pd
import numpy as np
import Forecast
from config import weather_api_key

# %%
# Request parameters
lat = "30.238333"
lon = "-97.508611"

responseJson = Forecast.makeAPIRequest(lat, lon, weather_api_key)

# %%
# Daily forecasted weather
daily_solar_DF = Forecast.forecasted_daily_solar(responseJson)

# %%
# Convert UTC time to CST time
daily_index = np.arange(0,8,1)
daily_UTC_date_time = daily_solar_DF["UTC_Time"]

date_time_DF = Forecast.convert_DateTime_UTC_to_CST(daily_UTC_date_time, daily_index)

# %%
# Clean the dataframe
daily_weather_DF = pd.merge(daily_solar_DF, date_time_DF, on='UTC_Time', how='outer')
daily_weather_DF.drop(columns=["UTC_Time"], axis=1, inplace=True)

# %%
# Calculate sunhours
daily_index = np.arange(0,8,1)
UTC_sunrise = daily_weather_DF["Sunrise"]
UTC_sunset = daily_weather_DF["Sunset"]

sunhour_DF = Forecast.calculate_sunhour(UTC_sunrise, UTC_sunset, daily_index)

# %%
# Merge sunhours into daily weather dataframe
daily_weather_DF = pd.merge(daily_weather_DF, sunhour_DF, on='Sunrise', how='outer')
daily_weather_DF.drop(columns=["Sunrise", "Sunset", "Date_Time", "Year", "Month", "Hour"], axis=1, inplace=True)

# %%
# Hourly forecasted weather
hourly_solar_DF = Forecast.forecasted_hourly_solar(responseJson)

# %%
# Convert UTC time to CST time
hourly_index = np.arange(0,48,1)
hourly_UTC_date_time = hourly_solar_DF["UTC_Time"]

hourly_date_time_DF = Forecast.convert_DateTime_UTC_to_CST(hourly_UTC_date_time, hourly_index)

# %%
# Merge CST time with the hourly dataframe
hourly_weather_DF = pd.merge(hourly_solar_DF, hourly_date_time_DF, on='UTC_Time', how='outer')
hourly_weather_DF.drop(columns=["UTC_Time"], axis=1, inplace=True)
hourly_weather_DF["Date_Time"] = pd.to_datetime(hourly_weather_DF["Date_Time"])
hourly_weather_DF = hourly_weather_DF[["Date_Time", "Year", "Month", "Day", "Hour", "Temperature_F", "Humidity_percent", "CloudCover_percent", "Weather_Description"]]

# %%
# Create the final datafram
forecasted_solar_DF = pd.merge(hourly_weather_DF, daily_weather_DF, on='Day', how='inner')
forecasted_solar_DF = forecasted_solar_DF[["Date_Time", "Year", "Month", "Day", "Hour", "Temperature_F", "Humidity_percent", "Sunhour", "CloudCover_percent", "uvIndex", "Weather_Description"]]

forecasted_solar_DF.head()

# %%
# Check the data types
# forecasted_solar_DF.dtypes

# %%
