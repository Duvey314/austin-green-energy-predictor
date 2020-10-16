# Austin Energy Predictor

- [Austin Energy Predictor](#austin-energy-predictor)
  - [Overview](#overview)
  - [Data](#data)
  - [Team](#team)
  - [Datasets](#datasets)

## Overview
The goal of this project is to determine the cleanest time to use energy as a consumer in Austin. The idea is to combine weather data and power generation peak outputs from renewable energy contribution predict during what time each day the power grid in Austin will contain the highest percentage of renewable energy.

The idea for the project is based off of the EcoBee thermostat. This product makes slight temperature adjustments to the owners thermostat when electricity demand in their community peaks. This reduces strain on the grid and saves the users money by reducing power usage when the grid power is more expensive. The project aims to complement this model by allowing home owners to also base their power usage on when the grid is producing the largest percentage of its energy from renewable sources.

This project is meant to both identify the effect of weather on renewable energy generation in Austin as well as provide a tool for Austin Energy customers to make informed decisions on when and how they use energy based on the grid mix of Austin.

## Data
There are two main sources of data for this project. The first is weather data forcast for the Austin area. We will be using the [ National Weather Service public data API](https://weather-gov.github.io/api/) to gather key weather data features that effect both solar photo voltaic (PV) panel and wind turbine energy production. To train the model we will need historic weather data as well. The source for this data has not been identified. The second source of data is information on the grid mix for Austin energy. This will come from raw data provided by Austin energy or creating a web scraper to scrape the data from AE's website.


## Team

Oshadi (github) - blurb and role

Mel (github) - blurb and role

Rahul (github) - blurb and role

Collin (github) - blurb and role

Shayna (github) - blurb and role

Duvey (github) - Updated

## Datasets
* [Thermostat Contol](https://data.austintexas.gov/Utilities-and-City-Services/Power-Partner-Thermostat-Program/7jgb-hbdr) - Could be used to interpolate the peak demand.
* [Grid Mix](https://austinenergy.com/ae/about/environment/renewable-power-generation) - Widget containing grid mix. Webscraper could collect this data.
* Weather https://www.goes.noaa.gov/

Austin Energy System Peak Demand
* https://data.austintexas.gov/resource/a6pm-qynf.json
