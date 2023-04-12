# Applied DataScience Capstone Project
This repository contains the code and data for the Applied Data Science Capstone Project.<br>
This project was done as the final course for the IBM Data Science Professional Certificate on Coursera.

[April 2023]

## Executive Summary 
In this capstone project, we will predict if the Falcon 9 first stage will land successfully or not. We collect the data using SpaceXdata API and Webscraping from Wikipedia. After data collection, we wrangle the data: we rename columns, replace missing values of some columns, classify some columns and perform basic EDA. After the initial cleaning, we perform EDA using SQL, and then data is analysed using vizualization techniques using various plots and data is further prepared for modelling. Then, visual analytics is done using Folium library to get some physical and environment observations. A dashboard is also prepared to display some results. The final stage was to model the preprocessed and cleaned data, and we choose various classification models with hyperparameter tuning.<br>
We found that as flight number increased, the success rate also increased. We found that sites are located close to highways, coasts and highways. And after modelling, we found that Decision Tree Classifier was the best model and it gave the highest accuracy on test data.

## Introduction 
###   Project background and context:
Space X advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage. Therefore, if we can determine if the first stage will land, we can determine the cost of a launch. This information can be used if an alternate company wants to bid against space X for a rocket launch. This goal of the project is to train a machine learning model to predict if the first stage will land successfully or not, and hence determine the approximate cost of the whole mission
### Questions to which answers are to be found:
* What factors determine if the rocket will land successfully?
* The interaction amongst various features that determine the success rate of a successful landing?
* What operating conditions needs to be in place to ensure a successful landing
program?

## Methodology
### Data collection methodology: 
* One dataset was extracted by using SpaceXData API 
* Other dataset was webscraped using BeautifulSoup from wikipedia
### Data wrangling 
* Performed basic EDA 
*  Determined training labels
### Exploratory Data Analysis (EDA) using Visualization and SQL 
* Vizualized and analysed data using scatterplots
* Used SQL queries to further analyse data
### Interactive visual analytics using Folium and Plotly Dash
* Built a dashboard to view piechart and scatter plots according to each site
### Predictive Analysis using classification models 
*  Trained classification models and determined the best model, 
*  plotted the confusion matrix for each model.

## Conclusion
The conclusions drawn from the project are:
* The best launch site is KSC LC-39A 
* Launches with payloads over 8000kg have high success rate
* VLEO orbit is overall a good choice for launch as it has high success rate for high number of launches
* Failure rate of new launches are low.
* With heavy payloads the successful landing or positive landing rate are more for PO, LEO and ISS orbits.
* Launch sites are located close to the equator, and in close proximity to the coast, railway lines and highways.
* Decision Tree Classifier is the best model for the problem and can be used to predict
the success or failure of upcoming launches.


`Ayush Priyam`
