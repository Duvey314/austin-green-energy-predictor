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
# Get the current UTC time stamp from the json response and store as list
current_date_time_UCT = [responseJson["current"]["dt"]]
# Get the length of the list
current_weather_index = np.arange(0,len(current_date_time_UCT),1)
# Convert UTC time stamp to datetime, year, month, day, and hour
current_date_time_DF = Forecast.convert_DateTime_UTC_to_CST(current_date_time_UCT, current_weather_index)

# %%
# Get the current solar weather data and convert to dataframe
current_weather_df = Forecast.current_solar_weather(responseJson)

# %%
# Merge the current weather dataframe with the date/time dataframe
current_solar_df = pd.merge(current_weather_df, current_date_time_DF, on="UTC_Time", how="outer")
# Drop the "UTC_Time" columns
current_solar_df.drop(columns=["UTC_Time"], axis=1, inplace=True)

# %%
# Set variables equal to "Sunrise" and "Sunset" columns
UTC_sunrise = [responseJson["current"]["sunrise"]]
UTC_sunset = [responseJson["current"]["sunset"]]
# length of index will be for one day
daily_index = np.arange(0,len(UTC_sunset),1)
# Calculate sunhours
sunhour_DF = Forecast.calculate_sunhour(UTC_sunrise, UTC_sunset, daily_index)

# %%
# Merge the solar dataframe with the sunhour dataframe
current_solar_df = pd.merge(current_solar_df, sunhour_DF, on="Sunrise", how="outer")
# Drop the Sunrise column
current_solar_df.drop(columns=["Sunrise"], axis=1, inplace=True)

# %%
# Load the model
scaler = load(open('Solar/solar_ml_model/scaler.pkl', 'rb'))
load_nn = tf.keras.models.load_model('Solar/solar_ml_model/solar_model')

# %%
# Define the features (X)
X = current_solar_df.drop(['Date_Time', 'Weather_Description','Day','Year'], axis=1)

# Transform the data
X_scaled = scaler.transform(X)

# %%
# Make the MWH predictions using the forecasted weather dataframe and model parameters
nn_results = Forecast.modelPrediction(current_solar_df, X_scaled, load_nn)

# %%
