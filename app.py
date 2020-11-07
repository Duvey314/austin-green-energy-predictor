# Flask App

from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)

@app.route("/")
def index():
    # mars = mongo.db.mars.find_one()
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
