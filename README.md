# Austin Energy Predictor

![Austin Energy](https://media-exp1.licdn.com/dms/image/C560BAQFwCAuAfk5AqA/company-logo_200_200/0?e=1611187200&v=beta&t=r1dOWcgLGes2ZNJEx7RSXYUk1JmWB3vaRIcpxES6s2M)

---

# Table of Contents
* [Overview](#overview)
* [Data](#data)
* [Methodology](#methodology)
* [Administrative](#administrative)
* [Team](#team)
* [Acknowledgements](#acknowledgements)

---
# Overview

The goal of this project is to determine the peak renewable energy output in the grid, for both wind and solar. We are  going to create a predictor to calculate the mega watt output per farm. We are currently analyzing weather data from Hackberry Farm, a wind Power Plant in Northern Texas. The idea is to take historical data- such as wind poewr and wind direction- as well as geographical plant factors to train an unsupervised neural network and predict the output of wind energy. Using this as a model, we can then extrapolate it to all farms that Austin Energy encompasses. Using weather forecasts, we should be able to use our model to determine the output of power and what time that will peak.

We called on a weather API, used geographic coordinates specifically for Hackberry Farms, and will apply this directly into the neural network to help predict wind power.  

We believe this information will be vital for Austin Energy, as the idea is to create a report that can look at a particular Wind Farm and then predict the output of energy a particular plant produces. Austin Energy will have a better understanding of when to schedule power generation and can use this model to help forecast energy production from their various plants.  Down the line, this information can be vital to consumers as they will have a better understanding of when to use high-energy products, when renewable energy production is at its highest, and also where they may find options of saving money by reducing power usage. 

---

# Data
There are two types of data we will primarily be using for this project. The first is weather data that will be used as the independent variables for this model. The second is the output of the solar and wind farm in megawatt hour(Mwh) which will be our dependent variable that we are trying to predict. 

### Weather
The model uses two form of weather data. The first is historic weather data that we will use to train our model. This data is pulled from the [Open Weather API](https://openweathermap.org/api). From this API we can pull historaical weather data from any location given a data range and geographic coordinates. We pulled two data sets from this API, one for our wind farm location and one for our solar farm location. The time frame of these datasets is the same as the datasets from Austin Energy to make the data merge easier. These data sets will be split into training and test sets by using all of the 2019 data as a test set and the 2020 data as the training set. 

Once we have our model trained, we will be making calls to the open weather api to get predicted weather data. This will be used to make predictions for the output of the wind and solar farms over that time frame.

### Energy Output
We have been very fortunate to work with Austin Energy on this project and they have been kind enough to give us access to the output data from two of their energy farms for Texas. These two locations are the Hackberry windfarm west of Dallas and the Webberville solar farm just outside of Austin.

![Gen Map](https://github.com/Duvey314/austin-green-energy-predictor/blob/master/Resources/Gen%20Map.png)

Both of these data sets are provided directly by Austin Energy and contain the hourly output of the wind/solar farm in Mwh.

[Hackberry Wind Farm](https://www.thewindpower.net/windfarm_en_4012_hackberry.php) -
* City: Albany, Shackelford
* Commissioning: 2008
* 72 turbines: Siemens SWT-2.3-93 (power 2 300 kW, diameter 93 m)
* Hub height: 80 m
* Total nominal power: 165,600 kW
* Latitude: 32° 46' 34"
* Longitude: -99° 28' 35.2"

[Webberville Solar Farm](http://webbervillesolar.com/) -
* City: Manor, Texas
* Commissioning: 2012
* 127,278 PV panels
* Total nominal power: 35,000 kw
* Latitude: 30° 14' 18"
* Longitude: -97° 30' 31"



### Database
The database we will be using for this project is a Mongodb Atlas database hosted on an AWS server. The historic weather data and the energy output data are cleaned and merged on the datetime stamp before being inserted into the database. The main database is the wind-solar-database. This houses two collections, a wind data collection and a solar data collection. These collection are accessed using the pymongo driver and a connection string with a username and password generated for each team member.

---

# Methodology

### Machine Learning Model
The machine learning model we are using is a neural network from the Scikit learn module. There will be two seperate models, one will be trained for the wind farm and the other on the solar farm. 

---
# Administrative

### Description of Communication Protocall

We have weekly zoom calls every Monday to discuss our individual progress. We committ to our individual branches and then assigned David as the master branch coordinator. 
Collin had created a presentation in which we document our weekly work. We use [Trello](https://trello.com/b/S5ONp84B/ut-bootcamp-capstone) as a project management tool to help us stay on course. 
We are using an agile project management methodology for this project.

### Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

### Database Storage
Mongo is the database we intend to use, and we will integrate Flask to display the data.

### Machine Learning
SciKitLearn is the ML library we'll be using to create a classifier. 

### Dashboard & Presentation
We are thinking about using Github pages or Heroku to help with database hosting, integration with the repository, and also the server environment.
GoogleSlides:  https://docs.google.com/presentation/d/1bD3JhPvRM_7ClN2xdoWEC1OZS5LJlWrjyJesHR8705s/edit#slide=id.ga1bdb9328c_0_10

### Technologies Used
-Pandas

-Numphy

-DateTime

-MatPotLib

-Imblearn

-Pathlib

-MongoDB

-Python

---
# Team

Oshadi (github) - Circle, Front End & Market/Techology Research on Wind Power Plant in Texas

Mel (https://github.com/msindrasena) - Triangle, Analysis and Support- pull weather data from API and formatted/presented into a DF

Rahul (https://github.com/madarahr)- Square, Performed ETL Process on weather data, ETL on Hackberry Wind Farm & merged dataframe and applied machine learning algorithm

Collin (https://github.com/collinsculley) - X, ERD relationship graphs and presentation organizer, front end dashboard.

Shayna (github) -Triange- pulled weather data from API and formatted/presented into a DF

Duvey (github.com/Duvey314/) - Square, Database administrator, Market/Tech Research with Austin Energy

---
# Acknowledgements
Oshadi's Brother
Austin Energy

# Resources


* [Thermostat Contol](https://data.austintexas.gov/Utilities-and-City-Services/Power-Partner-Thermostat-Program/7jgb-hbdr) - Could be used to interpolate the peak demand.
* [Grid Mix](https://austinenergy.com/ae/about/environment/renewable-power-generation) - Widget containing grid mix. Webscraper could collect this data.
* Weather https://www.goes.noaa.gov/

Austin Energy System Peak Demand
* https://data.austintexas.gov/resource/a6pm-qynf.json

A popular weather API seems to be the below
https://rapidapi.com/community/api/open-weather-map?endpoint=apiendpoint_9efd93b5-a454-4619-9ff8-bd3465aeebe1

An option for weather data which appears to be quite popular is
https://rapidapi.com/community/api/open-weather-map?endpoint=apiendpoint_9efd93b5-a454-4619-9ff8-bd3465aeebe1



http://www.ercot.com/gridinfo/generation
