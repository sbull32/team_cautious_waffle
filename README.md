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
  - Web scraped player position and team from [Sports Reference](https://www.sports-reference.com) directly.
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

## Web App Visualization of the Data
So originally the web app was going to be a way to display our results from the machine warning data in a user-friendly, and interactive method. Originally we were going to pull the machine learning model out through postgresSQL, and through using SQL alchemy we’re going to parse through that data and utilize it in a interactive menu that will display a table of all of our 600+ players that we pulled down from the Sportipy API. We were going to use a Python-based app that were referencing index that had general information about who was on the project what players you could select, what teams they were on, what positions they are, and as you felt up to this day that we were going to parse all of the additional statistics that applied specifically to those types of players or that specific player. Eventually when you settle down on one specific player I was hoping to pull the machine learning models predicted fantasy points into a gauge chart that would be able to visually show the user that this specific flare from this specific week would be a good choice based on prior data that we had, as well as show data from oral multiple linear regression‘s about how correlated the data from last week was to our model for that specific player. This would allow users to have a easy and simple selection method for our four different positions we were running through our model. 

However, due to some technical difficulties with connecting these SQL database to the python app, we had some issues that would not allow this original project idea to be complete before our deadline. So in the meantime, I created a web app with index file that referenced simple JavaScript-based data options showing data that we pulled from our API and predicted values. Since this was a mass poll of table data, I simplified it down to A smaller selection of players to make sure that the simple web app and we had to create didn’t get overwhelmed. The index simply utilizes three drop-down menus that allow you to par three play your names, positions, and their team in a little show their fantasy points for any of the selections you need. You can narrow it down to one of the players, you can show every member of that specific team that’s in the small table we have, or you can show it for specific positions across-the-board. It utilizes a similar drop-down function we’re going to utilize in our original web app design as well as the table format I was using in the rough draft of the web app. This allowed us to have a demo web app to show in tandem with the rest of our machine learning model, and can also show you what a rough table model would look like for a given week of data.

