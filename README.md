# Austin Energy Predictor

* [Overview](#overview)
* [Team](#team)
* [Datasets](#datasets)

## Overview
The problem statement is, "To determine the cleanest time to use energy as a consumer in Austin based on peak power generation", The idea is to combine weather data, power generation peak outputs, renewable energy contribution to the peak power generation and tell consumers when the energy on the grid will be the "cleanest."
Need to answer:
* Selected topic
* Reason they selected the topic
* Description of the source of data
* Questions they hope to answer with the data

mels edits: 
The goal of this project is to determine the cleanest time to use renewable energy sources in Austin by predicting short term wind power per Wind Power Plant. We would like to use historical data- such as wind power and wind direction- as well as geographical plant factors to train an unsupervised neural network to predict the output of wind energy. We will use Huckbery Farms- a large wind power plant in North Texas as a model and then extrapolate it to all farms that Austin Energy encompasses. Using weather forecasts, we should be able to use our model to determine the output of power and what time that will peak.

We called on a weather API, used geographic coordinates specifically for Huckberry Farms, and will apply this directly into the neural network to help predict wind power.  

We believe this information to be vital to consumers as they will have a better understanding of when to use high-energy products, when renewable energy production is at its highest, and also where they may find options of saving money by reducing power usage. We also believe this is vital for energy companies, such as Austin Energy, as they will have a better understanding of when to schedule power generation and can use this model to help forecast energy production from other plants.
Although we are studying only one specific plant, we can eventually use this model to predict power generation from other plants. This project is meant to both identify the effect of weather on renewable energy generation in Austin as well as provide a tool for Austin Energy customers to make informed decisions on when and how they use energy based on the grid mix of Austin.

## Team

Oshadi (github) - blurb and role

Mel (https://github.com/msindrasena) - Analysis

Rahul (github) - blurb and role

Collin (github) - blurb and role

Shayna (github) - blurb and role

Duvey (github) - blurb and role

## Datasets
* [Thermostat Contol](https://data.austintexas.gov/Utilities-and-City-Services/Power-Partner-Thermostat-Program/7jgb-hbdr) - Could be used to interpolate the peak demand.
* [Grid Mix](https://austinenergy.com/ae/about/environment/renewable-power-generation) - Widget containing grid mix. Webscraper could collect this data.
* Weather https://www.goes.noaa.gov/

Austin Energy System Peak Demand
* https://data.austintexas.gov/resource/a6pm-qynf.json
