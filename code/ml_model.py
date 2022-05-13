import os
import pandas as pd
import sklearn as sk
import numpy as np
from sklearn.linear_model import LogisticRegressionCV
from database import engine

query = """
select
    team_season, srs, ortg, drtg, true_shooting_percentage, average_age, margin_of_victory
from
    stats
where
    season in ('2011','2012','2013','2014','2015','2016','2017','2018','2019','2021','2022');
    """

team_stats = pd.read_sql_query(query, engine)

team_abbreviations = pd.read_csv(os.path.join("data", "clean", "team_abbreviations.csv"))

game_results = pd.read_csv(os.path.join("data", "clean", "game_results.csv"))
game_results = game_results.assign(home_win=lambda x: x.home_score > x.away_score)
game_results = game_results.loc[(game_results['year'] > 2010) & (game_results['year'] != 2020)] 

team_abbreviations = team_abbreviations.set_index(["Team"])
game_results = game_results.set_index(["home_team"])
game_results = game_results.assign(home_abbreviation = team_abbreviations["Abbreviation"])

game_results = game_results.reset_index()
game_results = game_results.set_index(["away_team"])
game_results = game_results.assign(away_abbreviation = team_abbreviations["Abbreviation"])
game_results = game_results.reset_index()

game_results['home_teamID'] = game_results['home_abbreviation'] + "-" + game_results["year"].astype(str)
game_results['away_teamID'] = game_results['away_abbreviation'] + "-" + game_results["year"].astype(str)

game_results = game_results.set_index(["home_teamID"])
team_stats = team_stats.set_index(["team_season"])
game_results = game_results.assign(
    home_srs = team_stats["srs"],
    home_ortg = team_stats["ortg"],
    home_drtg = team_stats["drtg"],
    home_true_shooting_percentage = team_stats["true_shooting_percentage"],
    home_average_age = team_stats["average_age"],
    home_margin_of_victory = team_stats["margin_of_victory"]
)

game_results = game_results.reset_index()
game_results = game_results.set_index(["away_teamID"])
game_results = game_results.assign(
    away_srs = team_stats["srs"],
    away_ortg = team_stats["ortg"],
    away_drtg = team_stats["drtg"],
    away_true_shooting_percentage = team_stats["true_shooting_percentage"],
    away_average_age = team_stats["average_age"],
    away_margin_of_victory = team_stats["margin_of_victory"]
)
game_results = game_results.reset_index()

game_results = game_results.assign(avg_age_diff=lambda x: x.home_average_age - x.away_average_age)

game_results = game_results.drop(["away_team", "home_team", "year", "round", "game", "home_score", "away_score", "home_abbreviation", "away_abbreviation", "home_average_age", "away_average_age"], axis = 1)

playoff_teams = ["ATL-2022", "BOS-2022", "CHI-2022", "DAL-2022", 
                 "DEN-2022", "GSW-2022", "MEM-2022", "MIA-2022",
                 "MIL-2022", "MIN-2022", "BKN-2022", "NOP-2022",
                 "PHI-2022", "PHX-2022", "TOR-2022", "UTA-2022"]

all_matchups = pd.DataFrame()
for team in playoff_teams:
    all_matchups = all_matchups.append(pd.DataFrame({'Home_TeamID': np.repeat(team, 15), 'Away_TeamID': list(filter((team).__ne__, playoff_teams))}))

all_matchups = all_matchups.set_index(["Home_TeamID"])
all_matchups = all_matchups.assign(
    home_srs = team_stats["srs"],
    home_ortg = team_stats["ortg"],
    home_drtg = team_stats["drtg"],
    home_true_shooting_percentage = team_stats["true_shooting_percentage"],
    home_average_age = team_stats["average_age"],
    home_margin_of_victory = team_stats["margin_of_victory"]
)

all_matchups = all_matchups.reset_index()
all_matchups = all_matchups.set_index(["Away_TeamID"])
all_matchups = all_matchups.assign(
    away_srs = team_stats["srs"],
    away_ortg = team_stats["ortg"],
    away_drtg = team_stats["drtg"],
    away_true_shooting_percentage = team_stats["true_shooting_percentage"],
    away_average_age = team_stats["average_age"],
    away_margin_of_victory = team_stats["margin_of_victory"]
)
all_matchups = all_matchups.reset_index()

all_matchups = all_matchups.assign(avg_age_diff=lambda x: x.home_average_age - x.away_average_age)

all_matchups = all_matchups.drop(["home_average_age", "away_average_age"], axis = 1)

clf = LogisticRegressionCV(cv = 10, solver = "liblinear", max_iter = 1000, penalty = 'l1', scoring = "roc_auc").fit(game_results.iloc[:, 3:14], game_results["home_win"])

all_2022_matchups = all_matchups.iloc[:, 0:2].reindex(columns = ["Home_TeamID", "Away_TeamID"])
all_2022_matchups["Home_win_prob"] = clf.predict_proba(all_matchups.iloc[:, 2:13])[:,1]

all_2022_matchups.to_csv(os.path.join("artifacts", "all_2022_matchups.csv"), index = False)