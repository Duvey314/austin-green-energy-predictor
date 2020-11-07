# Flask App

# import dependencies
import config
import pymongo
import pandas as pd
import json

from flask import Flask, render_template
from flask_pymongo import PyMongo

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
# select collection
collection = db.wind_data

# pull collection into dataframe
wind_df = pd.DataFrame(list(collection.find()))
wind_df

@app.route("/", methods=("POST", "GET"))
def index():
    return render_template("index.html", tables=[wind_df.to_html(classes='data')], titles=wind_df.columns.values)

if __name__ == "__main__":
    app.run()
