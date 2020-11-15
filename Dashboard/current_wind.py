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
# Get the current UTC time stamp from the json response and store as list
current_date_time_UCT = [responseJson["current"]["dt"]]
# Get the length of the list
current_weather_index = np.arange(0,len(current_date_time_UCT),1)
# Convert UTC time stamp to datetime, year, month, day, and hour
current_date_time_DF = Forecast.convert_DateTime_UTC_to_CST(current_date_time_UCT, current_weather_index)

# %%
# Get the current weather variables from the json response and store as pandas dataframe
current_weather_df = Forecast.current_wind_weather(responseJson)

# %%
# Merge the current weather dataframe with the date/time dataframe
current_wind_df = pd.merge(current_weather_df, current_date_time_DF, on='UTC_Time', how='inner')
# Drop the "UTC_Time" columns
current_wind_df.drop(columns=["UTC_Time"], axis=1, inplace=True)
# Covert "Date_Time" column to a datetime object
current_wind_df["Date_Time"] = pd.to_datetime(current_wind_df["Date_Time"])

# %%
# Load the model
scaler = load(open('Wind/wind_ml_model/scaler.pkl', 'rb'))
load_nn = tf.keras.models.load_model('Wind/wind_ml_model/wind_model')

# %%
# Define the features (X)
X = current_wind_df.drop(['Date_Time', 'Weather_Description', 'Year'], axis=1)
# Transform the data
X_scaled = scaler.transform(X)

# %%
# Make the MWH predictions using the current weather dataframe and model parameters
nn_results = Forecast.modelPrediction(current_wind_df, X_scaled, load_nn)

# %%
