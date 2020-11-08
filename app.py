# Flask App

# import dependencies
import os
import pymongo
import pandas as pd
import json

from flask import Flask, render_template
from flask_pymongo import PyMongo

from bokeh.io import show, output_file
from bokeh.plotting import figure, show
from bokeh.models import CustomJS, DatePicker
from bokeh.embed import components
from bokeh.resources import INLINE
# from bokeh.util.string import encode_utf8

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
solar_df


output_file('output_file_test.html',
    title='Empty Bokeh Figure')

fig = figure()

# show(fig)

# @app.route("/", methods=("POST", "GET"))
# def index():
#     return render_template("index.html", tables=[wind_df.to_html(classes='data')], titles=wind_df.columns.values,)
@app.route("/", methods=("POST", "GET"))
def bokeh():

    def date_picker_handler(attr, old, new):
        print("Previous date: " + old)
        print("Updated date: " + new)

    date_picker = DatePicker(title='Select date', value="2019-09-20", min_date="2019-08-01", max_date="2019-10-30")
    date_picker.on_change("value", date_picker_handler)
    

    from dashboard import firstplot
    p = firstplot(2017,4,20)

    # FirstPlot = json.dumps(json_item(p, "firstplot"))
    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(p)
    date_picker_script, date_picker_div = components(date_picker)
    html = render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
        date_picker_div=date_picker_div,
        date_picker_script=date_picker_script
    )
    return html.encode(encoding='UTF-8')


if __name__ == "__main__":
    app.run()
