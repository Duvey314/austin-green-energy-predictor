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

responseJson = Forecast.makeAPIRequest(lat, lon, weather_api_key)

# %%
hourly_wind_DF = Forecast.forecasted_hourly_wind(responseJson)

# %%
hourly_index = np.arange(0,48,1)
hourly_UTC_date_time = hourly_wind_DF["UTC_Time"]

hourly_date_time_DF = Forecast.convert_DateTime_UTC_to_CST(hourly_UTC_date_time, hourly_index)

# %%
forecasted_wind_DF = pd.merge(hourly_wind_DF, hourly_date_time_DF, on='UTC_Time', how='outer')
forecasted_wind_DF.drop(columns=['UTC_Time'], axis=1, inplace=True)
forecasted_wind_DF["Date_Time"] = pd.to_datetime(forecasted_wind_DF["Date_Time"])
forecasted_wind_DF = forecasted_wind_DF[["Date_Time", "Year", "Month", "Day", "Hour", "Temperature_F", "Humidity_percent", "WindSpeed_mph", "WindDirection_degrees", "Weather_Description"]]

# %%
# Load the model
scaler = load(open('Wind/wind_ml_model/scaler.pkl', 'rb'))
load_nn = tf.keras.models.load_model('Wind/wind_ml_model/wind_model')

# %%
# Define the features (X) and transform the data
X = forecasted_wind_DF.drop(['Date_Time', 'Weather_Description', 'Year'], axis=1)

# Transform the data
X_scaled = scaler.transform(X)

# %% 
nn_results = Forecast.modelPrediction(forecasted_wind_DF, X_scaled, load_nn)