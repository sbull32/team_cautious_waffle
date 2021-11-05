# team_cautious_waffle
Final Project

## Machine Learning Model
We will be using a multiple linear regression model in order to predict a players fantasy points for a given week. The data we will be using to train our model will be derived from last years statistics and the variables used will be based on the position a player plays. For example, if the player we are predicting fantasy points (target variable) for is a quarterback, we will be using different variables (features) than if the player was a different position such as running back. 

Listed below is the initial set of variables we will be using for each position we are predicting their stats for

- QB: completed passes, attempted passes, passing yards, passing touchdowns, quarterback rating, interceptions, times sacked, yards lost from sacks, fumbles lost, longest pass, rush yards, rush touchdowns, rush attempts
- RB: rush attempts, rush yards, rush touchdowns, receptions, receiving yards, receiving touchdowns, fumbles lost, longest rush, targets
- WR: targets, receptions, receiving yards, receiving touchdowns, longest reception, fumbles lost, rush yards, longest rush, rush touchdowns
- TE: targets, receptions, receiving yards, receiving touchdowns, longest reception, fumbles lost, rush yards, longest rush, rush touchdowns
 
We chose a multiple linear regression model due to the abundance of statistics available to use for training our model and the fact that we are attempting to predict a continuous variable (stats/fantasy points). 

We originally thought we would use the data from 2020 in order to predict stats in 2021 however after some time with the model we now think it is better to train last years data to see how well it predicted last years results. Therefore we decided to use our training and testing data from the same year. We decided to use a training set of 84% as that was the closest we could come to a 3 game sample of tests vs the rest of the season (14 games) to train the model. 

So far we have used the linear regression model on the entire dataframe to see how well last years stats in the aforementioned categories affected their fantasy points as well as a random forest classifier for each of the different positional dataframes to determine which features carried the most weight based on the players position. 

In addition to what we currently have trained, we plan on doing more in depth analysis on the models for each specific position to see what else we can uncover given the data we have. We also plan on using various methods to help visualize the data better. 
