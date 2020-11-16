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
lat = "32.776111"
lon = "-99.476444"

# Make API call to get weather data and turn response to JSON object
responseJson = Forecast.makeAPIRequest(lat, lon, weather_api_key)

# %%
# Store JSON object as pandas dataframe
hourly_wind_DF = Forecast.forecasted_hourly_wind(responseJson)

# %%
# Will be converting UTC timestamp for next 48 hours of weather predictions
hourly_index = np.arange(0,48,1)
# Set variable equal to "UTC_Time" column from hourly_wind_DF
hourly_UTC_date_time = hourly_wind_DF["UTC_Time"]

# Convert UTC time stamp to datetime, year, month, day, and hour
hourly_date_time_DF = Forecast.convert_DateTime_UTC_to_CST(hourly_UTC_date_time, hourly_index)

# %%
# Merge the weather predictions with the date/time dataframe
forecasted_wind_DF = pd.merge(hourly_wind_DF, hourly_date_time_DF, on='UTC_Time', how='outer')
# Drop the UTC_Time column 
forecasted_wind_DF.drop(columns=['UTC_Time'], axis=1, inplace=True)
# Convert "Date-Time" column to datetime object
forecasted_wind_DF["Date_Time"] = pd.to_datetime(forecasted_wind_DF["Date_Time"])

# %%
# Load the model
scaler = load(open('Wind/wind_ml_model/scaler.pkl', 'rb'))
load_nn = tf.keras.models.load_model('Wind/wind_ml_model/wind_model')

# %%
# Define the features (X) 
X = forecasted_wind_DF.drop(['Date_Time', 'Weather_Description', 'Year'], axis=1)
# Transform the data
X_scaled = scaler.transform(X)

# %% 
# Make the MWH predictions using the forecasted weather dataframe and model parameters
nn_results = Forecast.modelPrediction(forecasted_wind_DF, X_scaled, load_nn)
# %%
