# Austin Energy Predictor

* [Overview](#overview)
* [Team](#team)
* [Datasets](#datasets)

## Overview

The goal of this project is to determine the peak renewable energy output in the grid, for both wind and solar. We are  going to create a predictor to calculate the mega wat output per farm. We are currently analyzing weather data from Hackberry Farm, a wind Power Plant in Northern Texas. The idea is to take historical data- such as wind poewr and wind direction- as well as geographical plant factors to train an unsupervised neural network and predict the output of wind energy. Using this as a model, we can then extrapolate it to all farms that Austin Energy encompasses. Using weather forecasts, we should be able to use our model to determine the output of power and what time that will peak.

We called on a weather API, used geographic coordinates specifically for Hackberry Farms, and will apply this directly into the neural network to help predict wind power.  

We believe this information will be vital for Austin Energy, as the idea is to create a report that can look at a particular Wind Farm and then predict the output of energy a particular plant produces. Austin Energy will have a better understanding of when to schedule power generation and can use this model to help forecast energy production from their various plants.  Down the line, this information can be vital to consumers as they will have a better understanding of when to use high-energy products, when renewable energy production is at its highest, and also where they may find options of saving money by reducing power usage. 

This project is meant to both identify the effect of weather on renewable energy generation in Austin as well as provide a tool for Austin Energy customers to make informed decisions on when and how they use energy based on the grid mix of Austin.


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

