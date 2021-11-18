# Fantasy Football Predictor

## Overview
This project is tasked with utilizing a machine learning model (multiple linear regression) to predict the amount of fantasy points NFL players would accure. This model can then be used to build optimal rosters in fantasy football competitions.  There are a variety of sites to utilize to calculate fantasy points. This project utilizes the DraftKings site, which the rules can be found at  [NFL Classic Rules and Scoring](https://www.draftkings.com/help/rules/1/1). 

## Software
Python 3.7.10, pgAdmin 4

## ETL Process
- Data extraction from [Sportsipy](https://github.com/roclark/sportsipy), a python API that pulls stats from [Sports Reference](https://www.sports-reference.com).
- Data transformation:
  - Performed list comprehensions to iterate through box scores of every NFL game during the 2020 season.
  - Appended box scores and created dataframe with features to be used in the machine learning model.
  - Web scraped player position and team from www.sports-reference.com directly.
  - Appended player position to the dataframe in order to filter out defensive players.
  - Calculated fantasy points (target variable) accrued, for each player each week in the 2020 season, and appended to the dataframe.
- Data loading:
  - Imported box score dataframe and team dataframe into PostgresSQL database and performed a join between the two tables.
  - Created connection between the PostgreSQL database and machine learning model. 

## Machine Learning Model

We will be using a multiple linear regression model in order to predict a players fantasy points for a given week. The data we will be using to train our model will be derived from last years statistics and the variables used will be based on the position a player plays. For example, if the player we are predicting fantasy points (target variable) for is a quarterback, we will be using different variables (features) than if the player was a different position such as running back.

Listed below is the initial set of variables we will be using for each position we are predicting their stats for

- QB: completed passes, attempted passes, passing yards, passing touchdowns, quarterback rating, interceptions, longest pass, rush yards
- RB: rush attempts, rush yards, rush touchdowns, receptions, receiving yards, receiving touchdowns, fumbles lost, longest rush, targets
- WR: targets, receptions, receiving yards, receiving touchdowns, longest reception, fumbles lost, rush yards, longest rush, rush touchdowns
- TE: targets, receptions, receiving yards, receiving touchdowns, longest reception, fumbles lost, rush yards, longest rush, rush touchdowns

We chose a multiple linear regression model due to the abundance of statistics available to use for training our model and the fact that we are attempting to predict a continuous variable (stats/fantasy points).

We originally thought we would use the data from 2020 in order to predict stats in 2021 however after some time with the model we now think it is better to train last years data to see how well it predicted last years results. Therefore we decided to use our training and testing data from the same year. We decided to use a training set of 84% as that was the closest we could come to a 3 game sample of tests vs the rest of the season (14 games) to train the model.

So far we have used the linear regression model on the entire dataframe to see how well last years stats in the aforementioned categories affected their fantasy points as well as a random forest classifier for each of the different positional dataframes to determine which features carried the most weight based on the players position.

In addition to what we currently have trained, we plan on doing more in depth analysis on the models for each specific position to see what else we can uncover given the data we have. We also plan on using various methods to help visualize the data better.
