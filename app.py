# FLASK APP

# Import Dependencies
import os
import pymongo
import pandas as pd
import json

from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
# from forecast import forecastFunction

from pickle import load
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

app = Flask(__name__)


# set string variables
DEFAULT_DATABASE = 'wind_solar_data' 
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')

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

# @app.route("/getsolar")
# def getSolarData():
#     return solar_df.to_json(orient='table',index=False)

@app.route("/getwind", methods=['POST', 'GET'])
def getWindData():
    return wind_df.to_json(orient='table',index=False)

@app.route("/solarPredict/<YEAR>/<MONTH>/<DAY>", methods=['POST', 'GET'])
def solarPredict(YEAR=2019, MONTH=4, DAY=20):
    solarDayDF = solar_df.loc[(solar_df['Year'] == YEAR) & (solar_df['Month'] == MONTH) & (solar_df['Day'] == DAY)]
    date = (YEAR + MONTH + DAY)
# load in the scaler
scaler = load(open('../Solar/solar_ml_model/scaler.pkl', 'rb'))
print(scaler.get_params())

# # how to load the model
load_nn = tf.keras.models.load_model('../Solar/solar_ml_model/solar_model')
load_nn.summary()

    return (date)


# @app.route("/getwind/<startDate>/<endDate>", methods=['POST'])
# def getWindData(startDate='2020-01-01', endDate='2020-01-31'):

if __name__ == "__main__":
    app.run()
