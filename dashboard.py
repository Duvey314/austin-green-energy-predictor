#%%
# import dependencies
import config
import pymongo
import pandas as pd
import json

from flask import Flask, render_template
from flask_pymongo import PyMongo

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource


# set string variables
DEFAULT_DATABASE = 'wind_solar_data' 
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD

#%%
#create connection to database
client = pymongo.MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@austin-green-energy.pwzpm.mongodb.net/{DEFAULT_DATABASE}?retryWrites=true&w=majority")
try:
    client.server_info()
    print("Mongodb connected")
except:
    print("The Mongodb failed to connect. Check username/password in connection string.")


# %%
# Select database
db = client.get_database('wind_solar_data')
# sSlect collection
collection = db.solar_data

# Pull collection into dataframe
solar_df = pd.DataFrame(list(collection.find()))
solar_df = solar_df.drop('_id', axis=1)


# %%
YEAR = 2018
MONTH = 4
DAY = 20
solarDayDF = solar_df.loc[(solar_df['Year'] == YEAR) & (solar_df['Month'] == MONTH) & (solar_df['Day'] == DAY)]

solarDayDS = ColumnDataSource(solarDayDF)


def firstplot():
    p = figure(title='FirstPlot', x_axis_label='Hour', y_axis_label='MWH')
    p.line(x='Hour', y='MWH', source=solarDayDS)
    # p.line(x=[1,2,3], y=[1,2,3])
    return p