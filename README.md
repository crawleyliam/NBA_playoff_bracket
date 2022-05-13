# Report
## GOAL:
The goal of this analysis is to generate a model which predicts the winner of the 2022 NBA finals.
This analysis incorporates the probability that a given team will beat another given team in each game in every series, generating a final probability the team will win the finals.
Monte Carlo simulation will also be used to present the amount of times a team will win out of 1,000 simulations.

## Methodology:
This project uses publicly availible historical data from sportsreference.com.
The data is downloaded and turned into a database using SQL.
The database is cleaned trough SQL.
The historical data is then used to train a probit model to predict the probability a home team beats an away team based on a series of factors. 
These factors are determined by random forest modeling.
A probit model is used because we find that the score differentials between teams follow a normal distribution.
The 2022 NBA finals are then run through the model, each game is played in each series until a winner emerges from the bracket.
This scenario is then repeated 1000 times in a Monte Carlo simulation.
The results of this simulation reveal how likely any given team is to win the finals.
A simple visualisation of the methodology is presented in Excel and PowerPoint.

## Findings
(findings (or non-findings) must be clearly documented)
(Your findings must be supported by your analysis)

## Limitations
This project is limited by the strength of the probability model, which relied on machine learning techniques to gather the proper covariates of relevence. As mentioned also in the data/limitations section, our model lacks data on statistics such as coaching ability, team vs. team strategy, and player injuries. We believe the inclusion of these statistics into the probability model would improve the results of the analysis, however the Monte Carlo simulation tries to account for some of the non-white noise error. 
## Extensions

## Visualization
![ROC_curve](https://user-images.githubusercontent.com/97993980/168327854-5fea75bf-374e-4614-bbf3-5ebcaa6756e8.png)


# Data
## Source
The source of the data was sportsreference.com.

## Collection
Data was downloaded from sports reference and SQL was used to generate a database from the raw data.
Data was cleaned using SQL ensuring that team names were consistent, missing values were removed, and seasons with too few games were excluded.

## Details
The raw data includes several CSVs with various content.
First, game_data.csv includes historical game results; teams are labeled home and away.
Second, advanced_stats includes relevant team statistics which create the probit model.
Advanced stats include, OR & DR (offensive and defensive rating), EFG (effictive field goals), Pace, ORB & DRB (Rebound Rates), and SRS (Simple Rating System).
The data does not contain detailed information about individual players, injuries, or rule changes.

## Limitations
The data does not contain information about coaching ability, game strategy, or player injury. 
These factors could have played large roles in individual historical games leading abnormal ratings to muddle our training data; however the large amount of data helps compensate for these potential confounds.

## Data Extensions
The data used for this project could be extended in several ways.
Our analysis does not account for team strategy/game plan.
If our data were to include how each team was most likely to approach each game, and how each of those approaches performs against other approaches, the accuracy of the model may be improved.
Another possibility is to treat coach records against other coaches as another variable in the regression, allowing for strategies to be rolled into coaching style and helping to explain upset games. 
The most beneficial addition could be the inclusion of injury data which could help clarify past upset losses, such as the Raptors wins over the Warriors in 2019, and help explain upsets when predicting out.
