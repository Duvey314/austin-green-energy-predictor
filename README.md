# Austin Energy Predictor

* [Overview](#overview)
* [Team](#team)
* [Datasets](#datasets)

## Overview
The problem statement is, "To determine the cleanest time to use energy as a consumer in Austin based on peak power generation", The idea is to combine weather data, power generation peak outputs, renewable energy contribution to the peak power generation and tell consumers when the energy on the grid will be the "cleanest."

As the world is moving towards greener energy resources, it is important to understand that energy of all forms is not tuned to be generated at demand.  Energy companies estimate the energy needs and trade energy based on a general demand requirements.  The energy source provided by Austin Energy, an energy provider in Texas is predominantly from fossil fuels.  However, there is a rise in renewable resources in their portfolio which are derived from wind and solar.

Energy is generated when the sources (which are wind and daylight) are in reasonable amounts.  As such, it is important to predict the time of day when the energy produced from wind and solar sources peak during the day.  This is because it enables the consumer to use or automate their energy consumption during this time.  For example, operating the pool pump on a schedule, charging of electric vehicles, and use of consumer electronics around peak output times.




Oshadi (https://github.com/oshadiw) - Circle, Front End & Market/Techology Research on Wind Power Plant in Texas
 
Mel (https://github.com/msindrasena) - Analysis and Support- pull weather data from API and formatted/presented into a DF

Rahul (https://github.com/madarahr)- Square, Performed ETL Process on weather data, ETL on Hackberry Wind Farm
 & merged dataframe and applied machine learning algorithm 
 
Collin (github) - X, relationship graphs and presentation organizer

Shayna (github) -Triange- pulled weather data from API and formatted/presented into a DF

Duvey (github.com/Duvey314/) - Square, Database administrator, Market/Tech Research with Austin Energy 

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

