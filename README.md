# Austin Energy Predictor

![Austin Energy](https://austinenergy.com/wcm/connect/5f1c9e35-5964-489f-ac58-46cd0c865727/AELogo_RGB.jpg?MOD=AJPERES&CVID=mUt6-Xx)
---

# Table of Contents
* [Overview](#overview)
* [Datasets](#datasets)
* [Database](#database)
* [Methodology](#methodology)
* [Model](#model)
* [Dashboard](#dashboard)
* [Team](#team)
* [Acknowledgements](#acknowledgements)
* [Resources](#resources)

# Overview
--- 
This model is a culmination of a 5-week capstone project for the UT Austin Data Analytics & Visualization Bootcamp. Using our proficiencies in core Python, we retrieved weather data from online resources, organized it into easily-accessible data formats and interpreted the data relationships. 

The Austin Energy Predictor outputs forecasted renewable energy in Megawatt-Hours  (MWh) generated from a wind and solar energy farm in Texas. The model is used to predict renewable energy output based on time and weather factors, such as temperature, wind speed and cloud coverage.

Our purpose is to forecast power generation to get a better understanding of renewable energy as a mainstream power source for a healthier planet. We hope you enjoy learning about the project! Please feel free to contact us if you have any questions. You can find our github and linkedin pages at the bottom.(link to bottom of page)

To View our Project Dashboard, please visit this link: https://austin-green-energy-predictor.herokuapp.com/

To View our Project on Google Slides, please visit this link:
https://docs.google.com/presentation/d/1bD3JhPvRM_7ClN2xdoWEC1OZS5LJlWrjyJesHR8705s/edit#slide=id.ga1bdb9328c_0_10

To View a recorded, short demonstration (~5 min) of our Project, please visit this link:


To View a recorded, in depth overview (~15 min) of the Project, please visit this link: 
https://www.youtube.com/watch?v=Vx4V56U1gDI&t=1s

# Datasets
---
The machine learning model predicts renewable energy output based on weather conditions. Therefore, the model is fed two types of data - energy output data (MWh) and weather data. 

Energy Output Data:
Our team utilized energy output data provided by Austin energy for two of their renewable energy farms: Hackberry Wind Farm and Webberville Solar Farm. The data consists of hourly power generation for each of the renewable energy farms from 2017 through July of 2020. https://www.nj.gov/emp/energy/faq.html

The Hackberry Wind Farm is located west of Dallas, and Webberville Solar Farm is located just outside of Austin. The location of both renewable energy farms as well as Austin Energy’s additional energy farms can be observed below:

![Gen Map](https://github.com/Duvey314/austin-green-energy-predictor/blob/master/Resources/Images/Gen%20Map.png)

Both of these datasets (found under "Resources") are provided directly by Austin Energy and contain the hourly output of the wind/solar farm in Mwh. Take a look below for additional information on each of these farms:

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

## Historical Weather Data
Historical weather data for each farm has then been combined with the respective energy output to create two separate datasets - one for wind energy and one for solar. Using the Local Historical Weather Online API, multiple API calls were made to collect hourly weather parameters such as temperature, humidity percentage, and cloud coverage for each of the renewable energy farm locations. To ease the merging of the weather and energy output datasets, the data collected also extends the same time frame from January 2017 to July 2020.

## Forecasted Weather Data
After achieving an accurate machine learning model, forecasted weather data is used to make energy output predictions for Austin Energy’s wind and solar farm.

# Database 
---
The database used for this project is a MongoDB Atlas database hosted on an AWS server. The historical weather data and renewable energy outputs (Mwh) have been cleaned and merged on a DateTime timestamp before inserting the data into the database. The main database is the wind-solar-database, which houses two collections - a wind data collection and a solar data collection. These collections can be accessed using the PyMongo driver and a connection string along with a username and password given to each member of the team.

### Hackberry Wind MWH DataFrame
![](Resources/Images/HackberryWindMWH.png)

### Webberville Solar MWH DataFrame
![](Resources/Images/WebbervilleSolarMWH.png)

# Model
---
## Machine Learning Model Selection
The goal of the project is to predict the energy generation of renewable energy farms using weather forcast data. This means that we are looking for a model with a continuous output and therefore need some type of regression model. The two we have decided to use are a multiple linear regression and a neural network. Both models will be trained on the solar and wind data sperately.

## Multiple Linear Regression
The linear regression model is good at handling linear relationships between data but cannot handle other types of relationships without more data preprocessing. This resulted in a low accuracy for both models. The solar linear regression achieved an accuracy of ~60%. This closely resembled the shape of the data but could not predict the value of the power generated very well. The wind linear regression achieved an accuracy of ~30% and had many of the same pitfalls of the solar regression. The output of the regression gave an impression of the shape but did not get close to the correct values. 

## Neural Network
The neural network is able to handle more complex relationships between the data which resulted in a higher accuracy for both models. The shape of the two models are very similar. Both use a relu function output to ensure that the output is continuous and non negative. This is particularly important for the solar data because it has more values close to zero because it is not generating at night. Each model has three layers with 20-30 neurons per layer. The solar model has a mean absolute error of about 1.5 MWh or an accuracy of ~10%. It can predict very well the output during the day and is nearly perfect at predicting when the panels will start producing. The wind model has a mean absolute error of about 25 MWh or an accuracy of ~15%. This means that the data takes the shape of the output well but has difficulty predicting exact values.

# Future Recomendations 
Given that we only had 5 weeks to complete the project, there are definitely some things we would have loved to explore more. For future analysis, we would like to connect different weather data points to the historical data we already have. Ideally, we would like to also add more features to further develop the accuracy of the machine learning model. Lastly, we would like to develop a more advanced model for both solar and wind power generation. Our team would like to continue working with energy companies to predict energy output and give them an advantage in the energy marketplace. We also hope to empower consumers to make energy choices based on forecasted renewable energy output. 

## Tech Stack
Html, Flask, CSS, JavaScript, MongoDB, PyMongo, Matplotlib, Seaborn, Plotly, hvPlot, Scikit-Learn Library, TensorFlow Library, Pickle Module, Heroku

# Team
---
## Team Members
* [Oshadi Wimalarathne](https://www.linkedin.com/in/oshadiw/) - [GitHub](https://github.com/oshadiw)

* [Melina indrasena](https://www.linkedin.com/in/melina-indrasena/) - [GitHub](https://github.com/msindrasena)

* [Rahul Madarapu](https://www.linkedin.com/in/rahul-m-a2aa687/) - [GitHub](https://github.com/madarahr)
    
* [Collin Sculley](https://www.linkedin.com/in/collinsculley78745/) - [GitHub](https://github.com/collinsculley)
    
* [Shayna Sims](https://www.linkedin.com/in/shaynasims/) - [GitHub](https://github.com/shayna-UT)

* [David Rudow](https://www.linkedin.com/in/davidmrudow/) - [GitHub](https://github.com/Duvey314)
 



# Acknowledgements
---
* Kasun Chandrarathna (Xcel Employee):
    * Electrical Engineer at [Xcel Energy](https://www.xcelenergy.com/)
    * Provided information on how wind turbines are made and how power is generated and coverted to the grid.
* [Austin Energy](https://austinenergy.com/ae/about)
