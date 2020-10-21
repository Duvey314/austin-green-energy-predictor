# Austin Energy Predictor

* [Overview](#overview)
* [Team](#team)
* [Datasets](#datasets)

## Overview

The goal of this project is to determine the peak renewable energy output in the grid, for both wind and solar. We are  going to create a predictor to calculate the mega wat output per farm. We are currently analyzing weather data from Hackberry Farm, a wind Power Plant in Northern Texas. The idea is to take historical data- such as wind poewr and wind direction- as well as geographical plant factors to train an unsupervised neural network and predict the output of wind energy. Using this as a model, we can then extrapolate it to all farms that Austin Energy encompasses. Using weather forecasts, we should be able to use our model to determine the output of power and what time that will peak.

We called on a weather API, used geographic coordinates specifically for Hackberry Farms, and will apply this directly into the neural network to help predict wind power.  

We believe this information will be vital for Austin Energy, as the idea is to create a report that can look at a particular Wind Farm and then predict the output of energy a particular plant produces. Austin Energy will have a better understanding of when to schedule power generation and can use this model to help forecast energy production from their various plants.  Down the line, this information can be vital to consumers as they will have a better understanding of when to use high-energy products, when renewable energy production is at its highest, and also where they may find options of saving money by reducing power usage. 




# Technologies Used
## Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

## Database Storage
Mongo is the database we intend to use, and we will integrate Flask to display the data.

## Machine Learning
SciKitLearn is the ML library we'll be using to create a classifier. 

## Dashboard & Presentation
We are thinking about using Github pages or Heroku to help with database hosting, integration with the repository, and also the server environment.
GoogleSlides:  https://docs.google.com/presentation/d/1bD3JhPvRM_7ClN2xdoWEC1OZS5LJlWrjyJesHR8705s/edit#slide=id.ga1bdb9328c_0_10

## Technologies Used
-Pandas

-Numphy

-DateTime

-MatPotLib

-Imblearn

-Pathlib

-MongoDB

-Python

## Team


Oshadi (github) - Circle, Front End & Market/Techology Research on Wind Power Plant in Texas

Mel (https://github.com/msindrasena) - Triangle, Analysis and Support- pull weather data from API and formatted/presented into a DF

Rahul (https://github.com/madarahr)- Square, Performed ETL Process on weather data, ETL on Hackberry Wind Farm & merged dataframe and applied machine learning algorithm

Collin (https://github.com/collinsculley) - X, ERD relationship graphs and presentation organizer, front end dashboard.

Shayna (github) -Triange- pulled weather data from API and formatted/presented into a DF

Duvey (github.com/Duvey314/) - Square, Database administrator, Market/Tech Research with Austin Energy

## Description of Communication Protocall

We have weekly zoom calls every Monday to discuss our individual progress. We committ to our individual branches and then assigned David as the master branch coordinator. 
Collin had created a presentation in which we document our weekly work. We use Trello as a project management tool to help us stay on course. 
We are using an agile project management methodology for this project.


## Datasets
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

