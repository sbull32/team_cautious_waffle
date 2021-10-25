# team_cautious_waffle
Final Project

## Machine Learning Model
We will be using a multiple linear regression model in order to predict a players fantasy points for a given week. The data we will be using to train our model will be derived from last years statistics and the variables used will be based on the position a player plays. For example, if the player we are predicting fantasy points (target variable) for is a quarterback, we will be using different variables (features) than if the player was a different position such as running back. 

Listed below is the initial set of variables we will be using for each position we are predicting their stats for

QB: completions, passing attempts, passing yards, passing touchdowns, quarterback rating, interceptions, times sacked, fumbles lost
RB: rush attempts, rushing yards, rushing touchdowns, receptions, receiving yards, receiving touchdowns, fumbles lost
WR: targets, receptions, receiving yards, receiving touchdowns, longest reception, fumbles lost
TE: targets, receptions, receiving yards, receiving touchdowns, longest reception, fumbles lost
 
We chose a multiple linear regression model due to the abundance of statistics available to use for training our model and the fact that we are attempting to predict a continuous variable (stats/fantasy points). 

Once the player is chosen we will train the model using that players stats (features listed above) from 2020 to predict stats in 2021. We cam then test our model for each week in 2021 and then compare it to the actual results to test its accuracy.
