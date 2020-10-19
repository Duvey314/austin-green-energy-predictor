# Austin Energy Predictor

- [Austin Energy Predictor](#austin-energy-predictor)
  - [Overview](#overview)
  - [Data](#data)
  - [Team](#team)
  - [Datasets](#datasets)

## Overview

The goal of this project is to determine the cleanest time to use renewable energy sources in Austin by predicting short term wind power per Wind Power Plant. We would like to use historical data- such as wind power and wind direction- as well as geographical plant factors to train an unsupervised neural network to predict the output of wind energy.

We will use Hackbery Farms- a large wind power plant in North Texas as a model and then extrapolate it to all farms that Austin Energy encompasses. Using weather forecasts, we should be able to use our model to determine the output of power and what time that will peak.

We called on a weather API, used geographic coordinates specifically for Hackberry Farms, and will apply this directly into the neural network to help predict wind power. 

We believe this information to be vital to consumers as they will have a better understanding of when to use high-energy products, when renewable energy production is at its highest, and also where they may find options of saving money by reducing power usage. We also believe this is vital for energy companies, such as Austin Energy, as they will have a better understanding of when to schedule power generation and can use this model to help forecast energy production from other plants.

Although we are studying only one specific plant, we can eventually use this model to predict power generation from other plants. This project is meant to both identify the effect of weather on renewable energy generation in Austin as well as provide a tool for Austin Energy customers to make informed decisions on when and how they use energy based on the grid mix of Austin.


## Data
There are two main sources of data for this project. The first is weather data forcast for the Austin area. We will be using the [ National Weather Service public data API](https://weather-gov.github.io/api/) to gather key weather data features that effect both solar photo voltaic (PV) panel and wind turbine energy production. To train the model we will need historic weather data as well. The source for this data has not been identified. The second source of data is information on the grid mix for Austin energy. This will come from raw data provided by Austin energy or creating a web scraper to scrape the data from AE's website.

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

Collin (github) - X, ERD relationship graphs and presentation organizer

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
