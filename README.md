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


# Github will be Team_Cautious_Waffles version control.

This repository will be hosted on Github and will need to be able to read/write between team members.
*	standard HTTPS ports and can using HTTP authentication mechanisms, things like username/password authentication rather than having to set up SSH keys.

* URL based protocol will be used to clone, access, push over Git

### Advantages of using HTTP protocol for Git operations

HTTPS protocol provides the following advantages when used during git operations:

**Easy to Use**: HTTPS is easy to use. It was the main reason GitHub recommended it in the first place. To use HTTPS, the user has to copy the URL and run the git clone command to clone the repository. It is more comfortable and convenient to utilize for a user.

### Disadvantages of Using HTTP Protocol For Git Operations

HTTPS protocol has the following disadvantages when used during git operations:

- **Repetitive Authentication**: Whenever the user performs the network-based communication of any type such as pushing the changes to the repository or pulling the changes, every time they need to enter the credentials to authenticate their actions. 

## Machine Learning Model

We will be using a multiple linear regression model in order to predict a players fantasy points for a given week. The data we will be using to train our model will be derived from last years statistics and the variables used will be based on the position a player plays. For example, if the player we are predicting fantasy points (target variable) for is a quarterback, we will be using different variables (features) than if the player was a different position such as running back.

Listed below is the initial set of variables we will be using for each position we are predicting their stats for

- QB: completions, passing attempts, passing yards, passing touchdowns, quarterback rating, interceptions, times sacked, fumbles lost 
- RB: rush attempts, rushing yards, rushing touchdowns, receptions, receiving yards, receiving touchdowns, fumbles lost 
- WR: targets, receptions, receiving yards, receiving touchdowns, longest reception, fumbles lost 
- TE: targets, receptions, receiving yards, receiving touchdowns, longest reception, fumbles lost

We chose a multiple linear regression model due to the abundance of statistics available to use for training our model and the fact that we are attempting to predict a continuous variable (stats/fantasy points).

Once the player is chosen we will train the model using that players stats (features listed above) from 2020 to predict stats in 2021. We cam then test our model for each week in 2021 and then compare it to the actual results to test its accuracy.
