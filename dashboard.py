#%%
# import dependencies
import config
import pymongo
import pandas as pd
import json

from flask import Flask, render_template
from flask_pymongo import PyMongo

from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, DatePicker


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
# Select collection
collection = db.solar_data

# Pull collection into dataframe
solar_df = pd.DataFrame(list(collection.find()))
solar_df = solar_df.drop('_id', axis=1)


#%%
def date_picker_handler(attr, old, new):
    print("Previous date: " + old)
    print("Updated date: " + new)

date_picker = DatePicker(title='Select Date', value="2019-04-20", min_date="2017-01-01", max_date="2020-07-31")
date_picker.on_change("value", date_picker_handler)


def firstplot(YEAR=2018, MONTH=4, DAY=20):

    solarDayDF = solar_df.loc[(solar_df['Year'] == YEAR) & (solar_df['Month'] == MONTH) & (solar_df['Day'] == DAY)]

    solarDayDS = ColumnDataSource(solarDayDF)

    p = figure(title='FirstPlot', x_axis_label='Hour', y_axis_label='MWH')
    p.line(x='Hour', y='MWH', source=solarDayDS)
    return p
