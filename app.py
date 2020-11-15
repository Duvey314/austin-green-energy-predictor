# FLASK APP

# Import Dependencies
import os
import pymongo
import pandas as pd
import json
import numpy as np

import config

from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
import Forecast

from pickle import load
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

app = Flask(__name__)


# set string variables
DEFAULT_DATABASE = 'wind_solar_data' 
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD

#create connection to database
client = pymongo.MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@austin-green-energy.pwzpm.mongodb.net/{DEFAULT_DATABASE}?retryWrites=true&w=majority")
try:
    client.server_info()
    print("Mongodb connected")
except:
    print("The Mongodb failed to connect. Check username/password in connection string.")

# select database
db = client.get_database('wind_solar_data')

# SOLAR collection
collection = db.solar_data

# pull SOLAR collection into dataframe
solar_df = pd.DataFrame(list(collection.find()))
solar_df = solar_df.drop('_id', axis=1)

# WIND collection
collection = db.wind_data
# pull WIND collection into DF
wind_df = pd.DataFrame(list(collection.find()))
wind_df = wind_df.drop('_id', axis=1)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/getSolar")
def getSolarData():
    # Request parameters
    lat = "30.238333"
    lon = "-97.508611"

    # Make API call to get weather data and turn response to JSON object
    responseJson = Forecast.makeAPIRequest(lat, lon, config.weather_api_key)

    # Get the daily weather variables from json response and store as pandas dataframe
    daily_solar_DF = Forecast.forecasted_daily_solar(responseJson)

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

    # Merge the weather predictions with the date/time dataframe
    daily_weather_DF = pd.merge(daily_solar_DF, date_time_DF, on='UTC_Time', how='outer')
    # Drop the UTC_Time column 
    daily_weather_DF.drop(columns=["UTC_Time"], axis=1, inplace=True)

    # Merge sunhours into daily weather dataframe
    daily_weather_DF = pd.merge(daily_weather_DF, sunhour_DF, on='Sunrise', how='outer')
    # Drop the following columns so daily weather dataframe can merge with hourly weather dataframe
    daily_weather_DF.drop(columns=["Sunrise", "Sunset", "Date_Time", "Year", "Month", "Hour"], axis=1, inplace=True)

    # Get the hourly weather variables from json response and store as pandas dataframe
    hourly_solar_DF = Forecast.forecasted_hourly_solar(responseJson)

    # Will be converting UTC timestamp for next 48 hours of weather predictions
    hourly_index = np.arange(0,48,1)
    # Set variable equal to "UTC_Time" column from hourly_wind_DF
    hourly_UTC_date_time = hourly_solar_DF["UTC_Time"]

    # Convert UTC time stamp to datetime, year, month, day, and hour
    hourly_date_time_DF = Forecast.convert_DateTime_UTC_to_CST(hourly_UTC_date_time, hourly_index)

    # Merge the weather predictions with the date/time dataframe
    hourly_weather_DF = pd.merge(hourly_solar_DF, hourly_date_time_DF, on='UTC_Time', how='outer')
    # Drop the UTC_Time column 
    hourly_weather_DF.drop(columns=["UTC_Time"], axis=1, inplace=True)
    # Convert "Date-Time" column to datetime object
    hourly_weather_DF["Date_Time"] = pd.to_datetime(hourly_weather_DF["Date_Time"])

    # Create the final dataframe: merge the hourly weather DF with the daily weather DF
    forecasted_solar_DF = pd.merge(hourly_weather_DF, daily_weather_DF, on='Day', how='inner')

    forecasted_solar_DF = forecasted_solar_DF[["Date_Time", "Year", "Month", "Day", "Hour", "Temperature_F", "Humidity_percent", "Sunhour", "CloudCover_percent", "uvIndex", "Weather_Description"]]

    # Load the model
    scaler = load(open('Solar/solar_ml_model/scaler.pkl', 'rb'))
    load_nn = tf.keras.models.load_model('Solar/solar_ml_model/solar_model')

    # Define the features (X) and transform the data
    X = forecasted_solar_DF.drop(['Date_Time', 'Weather_Description','Day','Year'], axis=1)

    # Transform the data
    X_scaled = scaler.transform(X)

    # Predict values for test set
    nn_results = Forecast.modelPrediction(forecasted_solar_DF, X_scaled, load_nn)
    return nn_results.to_json(orient='table',index=False)
    

@app.route("/getwind", methods=['POST', 'GET'])
def getWindData():
    # Request parameters
    lat = "32.776111"
    lon = "-99.476444"

    # Make API call to get weather data and turn response to JSON object
    responseJson = Forecast.makeAPIRequest(lat, lon, config.weather_api_key)
    
    # Store JSON object as pandas dataframe
    hourly_wind_DF = Forecast.forecasted_hourly_wind(responseJson)
    
    # Will be converting UTC timestamp for next 48 hours of weather predictions
    hourly_index = np.arange(0,48,1)
    # Set variable equal to "UTC_Time" column from hourly_wind_DF
    hourly_UTC_date_time = hourly_wind_DF["UTC_Time"]

    # Convert UTC time stamp to datetime, year, month, day, and hour
    hourly_date_time_DF = Forecast.convert_DateTime_UTC_to_CST(hourly_UTC_date_time, hourly_index)
    
    # Merge the weather predictions with the date/time dataframe
    forecasted_wind_DF = pd.merge(hourly_wind_DF, hourly_date_time_DF, on='UTC_Time', how='outer')
    # Drop the UTC_Time column 
    forecasted_wind_DF.drop(columns=['UTC_Time'], axis=1, inplace=True)
    # Convert "Date-Time" column to datetime object
    forecasted_wind_DF["Date_Time"] = pd.to_datetime(forecasted_wind_DF["Date_Time"])
    forecasted_wind_DF = forecasted_wind_DF[["Date_Time", "Year", "Month", "Day", "Hour", "Temperature_F", "Humidity_percent", "WindSpeed_mph", "WindDirection_degrees", "Weather_Description"]]

    # Load the model
    scaler = load(open('Wind/wind_ml_model/scaler.pkl', 'rb'))
    load_nn = tf.keras.models.load_model('Wind/wind_ml_model/wind_model')
    
    # Define the features (X) 
    X = forecasted_wind_DF.drop(['Date_Time', 'Weather_Description', 'Year'], axis=1)
    # Transform the data
    X_scaled = scaler.transform(X)
    
    # Make the MWH predictions using the forecasted weather dataframe and model parameters
    nn_results = Forecast.modelPrediction(forecasted_wind_DF, X_scaled, load_nn)

    return nn_results.to_json(orient='table',index=False)

@app.route("/solarPredict/<YEAR>/<MONTH>/<DAY>", methods=['POST', 'GET'])
def solarPredict(YEAR=2019, MONTH=4, DAY=20):
    MONTH = int(MONTH)
    DAY = int(DAY)
    YEAR = int(YEAR)
    solar_df_copy = solar_df.copy()
    solarDayDF = solar_df_copy.loc[(solar_df_copy['Year'] == YEAR) & (solar_df_copy['Month'] == MONTH) & (solar_df_copy['Day'] == DAY)]

    # load in the scaler
    scaler = load(open('Solar/solar_ml_model/scaler.pkl', 'rb'))

    # how to load the model
    load_nn = tf.keras.models.load_model('Solar/solar_ml_model/solar_model')

    X = solarDayDF.drop(['Date_Time', 'Weather_Description','Day','Year','MWH'], axis=1)
 
    # Scaling the data.
    X_scaled = scaler.transform(X)
  
     # Make the MWH predictions using the forecasted weather dataframe and model parameters
    y_pred = load_nn.predict(X_scaled)
    y_pred = y_pred.ravel()

    solarDayDF['pred'] = y_pred

    return solarDayDF.to_json(orient='table',index=False)

@app.route("/windPredict/<YEAR>/<MONTH>/<DAY>", methods=['POST', 'GET'])
def windPredict(YEAR=2019, MONTH=4, DAY=20):
    MONTH = int(MONTH)
    DAY = int(DAY)
    YEAR = int(YEAR)
    windDayDF = wind_df.loc[(wind_df['Year'] == YEAR) & (wind_df['Month'] == MONTH) & (wind_df['Day'] == DAY)]

    # load in the scaler
    scaler = load(open('Wind/wind_ml_model/scaler.pkl', 'rb'))

    # how to load the model
    load_nn = tf.keras.models.load_model('Wind/wind_ml_model/wind_model')

    X = windDayDF.drop(['MWH', 'WindDirection_compass', 'Year','Weather_Description', 'Date_Time','WindGust_mph'], axis=1)
 
    # Scaling the data.
    X_scaled = scaler.transform(X)
    
    # Make the MWH predictions using the forecasted weather dataframe and model parameters
    y_pred = load_nn.predict(X_scaled)
    y_pred = y_pred.ravel()

    # Create dataframe for results
    windDayDF['pred'] = y_pred

    return windDayDF.to_json(orient='table',index=False)


if __name__ == "__main__":
    app.run()
