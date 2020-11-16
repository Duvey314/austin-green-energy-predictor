# %%
# Initial Imports
import pandas as pd
import numpy as np
import Forecast
from config import weather_api_key
from pickle import load
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

# %%
# Request parameters
lat = "30.238333"
lon = "-97.508611"

# Make API call to get weather data and turn response to JSON object
responseJson = Forecast.makeAPIRequest(lat, lon, weather_api_key)

# %%
# Get the daily weather variables from json response and store as pandas dataframe
daily_solar_DF = Forecast.forecasted_daily_solar(responseJson)

# %%
# Will be converting UTC time stamp for next 7 days of weather predictions
daily_index = np.arange(0,8,1)

# Set variable equal to "UTC_Time" column from daily_solar_DF
daily_UTC_date_time = daily_solar_DF["UTC_Time"]
# Convert UTC time to CST time
date_time_DF = Forecast.convert_DateTime_UTC_to_CST(daily_UTC_date_time, daily_index)

# Set variables equal to "Sunrise" and "Sunset" columns
UTC_sunrise = daily_solar_DF["Sunrise"]
UTC_sunset = daily_solar_DF["Sunset"]
# Calculate sunhours
sunhour_DF = Forecast.calculate_sunhour(UTC_sunrise, UTC_sunset, daily_index)

# %%
# Merge the weather predictions with the date/time dataframe
daily_weather_DF = pd.merge(daily_solar_DF, date_time_DF, on='UTC_Time', how='outer')
# Drop the UTC_Time column 
daily_weather_DF.drop(columns=["UTC_Time"], axis=1, inplace=True)

# %%
# Merge sunhours into daily weather dataframe
daily_weather_DF = pd.merge(daily_weather_DF, sunhour_DF, on='Sunrise', how='outer')
# Drop the following columns so daily weather dataframe can merge with hourly weather dataframe
daily_weather_DF.drop(columns=["Sunrise", "Sunset", "Date_Time", "Year", "Month", "Hour"], axis=1, inplace=True)

# %%
# Get the hourly weather variables from json response and store as pandas dataframe
hourly_solar_DF = Forecast.forecasted_hourly_solar(responseJson)

# %%
# Will be converting UTC timestamp for next 48 hours of weather predictions
hourly_index = np.arange(0,48,1)
# Set variable equal to "UTC_Time" column from hourly_wind_DF
hourly_UTC_date_time = hourly_solar_DF["UTC_Time"]

# Convert UTC time stamp to datetime, year, month, day, and hour
hourly_date_time_DF = Forecast.convert_DateTime_UTC_to_CST(hourly_UTC_date_time, hourly_index)

# %%
# Merge the weather predictions with the date/time dataframe
hourly_weather_DF = pd.merge(hourly_solar_DF, hourly_date_time_DF, on='UTC_Time', how='outer')
# Drop the UTC_Time column 
hourly_weather_DF.drop(columns=["UTC_Time"], axis=1, inplace=True)
# Convert "Date-Time" column to datetime object
hourly_weather_DF["Date_Time"] = pd.to_datetime(hourly_weather_DF["Date_Time"])

# %%
# Create the final dataframe: merge the hourly weather DF with the daily weather DF
forecasted_solar_DF = pd.merge(hourly_weather_DF, daily_weather_DF, on='Day', how='inner')

# %%
# Load the model
scaler = load(open('Solar/solar_ml_model/scaler.pkl', 'rb'))
load_nn = tf.keras.models.load_model('Solar/solar_ml_model/solar_model')

# %%
# Define the features (X) and transform the data
X = forecasted_solar_DF.drop(['Date_Time', 'Weather_Description','Day','Year'], axis=1)

# Transform the data
X_scaled = scaler.transform(X)

# %% 
# Make the MWH predictions using the forecasted weather dataframe and model parameters
nn_results = Forecast.modelPrediction(forecasted_solar_DF, X_scaled, load_nn)
# %%
