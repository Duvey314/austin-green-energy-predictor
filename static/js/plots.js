// .ENV CONFIG VARIABLES
const dotenv = require("dotenv")
dotenv.config()

// MongoDB Client Connection
const MongoClient = require('mongodb').MongoClient;
// replace the uri string with connection string.
const uri = `mongodb+srv://${process.env.USERNAME}:${process.env.PASSWORD}@austin-green-energy.pwzpm.mongodb.net/wind_solar_data?retryWrites=true&w=majority`
const client = new MongoClient(uri, { useUnifiedTopology: true }, { useNewUrlParser: true });
client.connect(err => {
    const collection = client.db("wind_solar_data").collection("solar_data");
        collection.find().toArray()
            .then(docs => console.log("all documents", docs))
            .catch(err => console.error(`Failed to find documents: ${err}`))
    client.close();
});

// var MongoClient = require('mongodb').MongoClient;
// var uri = "mongodb://<username>:<password>@austin-green-energy-shard-00-00.pwzpm.mongodb.net:27017,austin-green-energy-shard-00-01.pwzpm.mongodb.net:27017,austin-green-energy-shard-00-02.pwzpm.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-6mh5wb-shard-0&authSource=admin&retryWrites=true&w=majority";
// MongoClient.connect(uri, function(err, client) {
//   const collection = client.db("test").collection("devices");
//   // perform actions on the collection object
//   client.close();
// });