# NFL Fantasy Sports Predictor

## Overview
This project is tasked with utilizing a machine learning model to predict the amount of fantasy points NFL players would accure.  There are a variety of sites to utilize to calculate fantasy points.  This project utilizes the DraftKings site, which the rules can be found at [NFL Classic Rules and Scoring](https://www.draftkings.com/help/rules/1/1). 

## Software
Python 3.7.10, pgAdmin 4

## ETL Process
- Data extraction from [Sportsipy](https://github.com/roclark/sportsipy).
- Data transformation:
  - Segregate raw NFL data by week, by player, by position in columns that align with DraftKings scoring (features).
  - Convert raw NFL data into fantasy points.
- Data loading:
  - Store dataframes in a database (postgres).
  - Create dashboard to request and visualize data.    
