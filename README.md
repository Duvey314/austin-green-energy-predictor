# Austin Energy Predictor

* [Overview](#overview)
* [Team](#team)
* [Datasets](#datasets)

## Overview
The problem statement is, "To determine the cleanest time to use energy as a consumer in Austin based on peak power generation", The idea is to combine weather data, power generation peak outputs, renewable energy contribution to the peak power generation and tell consumers when the energy on the grid will be the "cleanest."

## Team

Oshadi (github) - Front End

Mel (github) - blurb and role

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

## Supplemental Information
Turbines used for harnessing wind energy come in various "sizes", based on the output rating. To caluclate the MW output of a turbine, a power curve is used based on a function of the area of the rudders and the velocity. As velocity increasesm the power output of a turbine increases by a factor of 3. However, the turbines are unable to send all of the energy generated to the grid, as there is a max efficiency range of 45-55%. If the wind speed is too high, the turbine will shut off (this speed is called the cut-off speed). There is also a minimum wind speed to generate power.
