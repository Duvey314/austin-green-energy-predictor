import config
import pymongo
import pandas as pd

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient(f"mongodb+srv://admin:{config.PASSWORD}@austin-green-energy.pwzpm.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
db = client.get_database('sample_airbnb')
data = db.listingsAndReviews
list(data.find())

df = pd.DataFrame(list(data.find()))
print(df.head())