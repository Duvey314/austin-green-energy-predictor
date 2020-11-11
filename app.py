# FLAST APP

# Import Dependencies
import os
import pymongo
import pandas as pd
import json

from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo

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
# select collection
collection = db.solar_data

# pull collection into dataframe
solar_df = pd.DataFrame(list(collection.find()))
solar_df = solar_df.drop('_id', axis=1)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
