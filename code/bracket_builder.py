import pandas as pd
import random
import os
from matplotlib import pyplot

INPUT_DIR = 'artifacts'
OUTPUT_DIR = 'artifacts'

df = pd.read_csv(os.path.join(INPUT_DIR, "all_2022_matchups.csv"))
dict1 = {'team': ['PHX-2022', 'MEM-2022', 'GSW-2022', 'DAL-2022', 'UTA-2022', 'DEN-2022', 'MIN-2022', 'NOP-2022',
                  'MIA-2022', 'BOS-2022', 'MIL-2022', 'PHI-2022', 'TOR-2022', 'CHI-2022', 'BKN-2022', 'ATL-2022'],
         'conference': ['western', 'western', 'western', 'western', 'western', 'western', 'western', 'western',
                        'eastern', 'eastern', 'eastern', 'eastern', 'eastern', 'eastern', 'eastern', 'eastern'],
         'seed': [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]}
df1 = pd.DataFrame(dict1)

matchup_dict = {}
winner_dict = {}
conference_dict = {1: "western", 2: "eastern"}


def pick_winner(matchup):
    """This function picks the series winner of one matchup. The projected winning team is returned."""
    
    if df1[(df1['team'] == matchup[0])].iloc[0, 1] == df1[(df1['team'] == matchup[1])].iloc[0, 1]:
        if df1[(df1['team'] == matchup[0])].iloc[0, 2] > df1[(df1['team'] == matchup[1])].iloc[0, 2]:
            home_team = matchup[0]
            away_team = matchup[1]
        else:
            home_team = matchup[1]
            away_team = matchup[0]
    else:
        home_team = matchup[0]
        away_team = matchup[1]
        
    prob1 = df[(df['Home_TeamID'] == home_team) & (df['Away_TeamID'] == away_team)].iloc[0, 2]
    prob2 = df[(df['Home_TeamID'] == away_team) & (df['Away_TeamID'] == home_team)].iloc[0, 2]
    home_wins = 0
    for i in range(4):
        if prob1 > random.uniform(0, 1):
            home_wins += 1
    for i in range(3):
        if prob2 < random.uniform(0, 1):
            home_wins += 1

    if home_wins >= 4:
        return_value = home_team
    else:
        return_value = away_team

    return return_value


def build_round(game_lower, game_upper):
    """This function builds up matchups for a given round based on the upper and lower bounds of game numbers for a
    given round are used as arguments. There is no return value."""

    for i in range(game_lower, game_upper):
        matchup_dict[i] = [winner_dict[(2 * i) - 17], winner_dict[(2 * i) - 16]]


def pick_round(game_lower, game_upper):
    """This function picks one round of games by looping over matchup_dict. The upper and lower bounds of game numbers
    for a given round are used as arguments. The winner_dict dictionary is updated to reflect the projected winners of
    the round. There is no return value."""

    for i in range(game_lower, game_upper):
        winner_dict[i] = pick_winner(matchup_dict[i])


def build_bracket():
    """This function builds up the bracket. There is no argument or return value. The dataframe must be properly scoped so that the function can
    access it."""

    list1 = [1, 4, 3, 2]
    for i in list1:
        for n in range(1, 3):
            matchup_dict[list1.index(i) + 1 + ((n - 1) * 4)] = \
                [df1[(df1["conference"] == conference_dict[n]) & (df1['seed'] == i)].team.values[0],
                 df1[(df1["conference"] == conference_dict[n]) & (df1['seed'] == (9 - i))].team.values[0]]


def pick_bracket():
    """This function fills out entire bracket with successive calls to build_round and pick_round. It must be called
    after build_bracket. There is no argument or return value."""

    pick_round(1, 9)
    build_round(9, 13)
    pick_round(9, 13)
    build_round(13, 15)
    pick_round(13, 15)
    build_round(15, 16)
    pick_round(15, 16)

def pick_champion():
    """This function takes the information from build_bracket and returns
    the ultimate winnner of the tournament after pick_bracket is called. """
    build_bracket()
    pick_bracket()

    return(winner_dict[15])

def random_sim(num_simulations):
    """This function simulates the outcome of pick_champion for a desired
    number of times. It returns a list of champions names in the form NME-YEAR"""
    sim_champion = []
    for i in range(num_simulations):
        sim_champion.append(pick_champion())
    
    return(sim_champion)


if __name__ == '__main__':
    sim_result = pd.DataFrame(random_sim(1000)).value_counts()
    
    team_names = list(list(zip(*sim_result.index.values))[0])
    
    team_names = [s.replace("-2022", "") for s in team_names]
    
    pyplot.bar(team_names, sim_result.values / 10)
    pyplot.title('Pre-playoffs Probability of Winning 2022 Championship')
    pyplot.xlabel('Team')
    pyplot.ylabel('Win Percentage')
    pyplot.savefig(os.path.join("artifacts", "2022_bar_plot_1000.png"))
#    build_bracket()
#    pick_bracket()
#    with open(os.path.join(OUTPUT_DIR, "winners.csv"), 'w') as file:
#        for key in winner_dict.keys():
#            file.write("%s, %s\n" % (key, winner_dict[key]))

#    with open(os.path.join(OUTPUT_DIR, "matchups.csv"), 'w') as file:
#        for key in matchup_dict.keys():
#            file.write("%s, %s\n" % (key, matchup_dict[key]))
