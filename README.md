# Daily Fantasy Sports Roster Optimizer

## Overview
This project is tasked with utilizing a machine learning model (initial thoughts would be a supervised linear regression model) to create daily fantasy roster(s) that would "win" on a consistent basis in daily fantasy sports competitions.  The target variable is the amount of fantasy points.  There are two types of games within daily fantasy sports:

- Cash games - around 50 percent of the participants win the same prize and don’t require a top score to win.
- Guaranteed prize pool (GPP) games - 20 percent or fewer of the lineups win money, with the top finishers getting a big percentage of the winnings while that percentage drops quickly as you go down the list of winners.

This model is aimed at constructing an optimal lineup to compete in cash games.  Furthermore, there are a variety of sports to compete in along with a variety of sites to utilize.  This project centers on fantasy football, using the DraftKings site, and utilizing the rules concerning classic roster construction.  The rules can be found at [NFL Classic Rules and Scoring](https://www.draftkings.com/help/rules/1/1). 

## Software
Python 3.7.10, pgAdmin 4

## Procedure(tentative)
- Data selection from [Sportsipy](https://github.com/roclark/sportsipy).
- Data processing:
  - Segregate raw NFL data by week, by player, by position in columns that align with DraftKings scoring (features).
  - Apply machine learing model to predict NFL data for each eligible NFL player.
  - Convert raw NFL data into fantasy points.
  - Utilizing DraftKings roster requirements, calculate an optimal lineup for a given week (the Excel Sovler tool can be used as an example).
- Data transformation:
  - Store dataframes in a database (postgres).
  - Create dashboard to request and visualize data.    
