import os
import pandas as pd
from glob2 import glob

# read csv loop and create row replacement list
os.path.join("data", "team_vs_team")

names = glob("*.csv")
dfs = []

old_names = ["Charlotte Bobcats", "New Jersey Nets", "New Orleans/Oklahoma City Hornets", "New Orleans Hornets","Seattle SuperSonics"]
current_names = ["Charlotte Hornets", "Brooklyn Nets", "New Orleans Pelicans", "New Orleans Pelicans", "Oklahoma City Thunder"]

for file in glob("*.csv"):
    df = pd.read_csv(file)
    # rename header to current abbreviation
    if "CHA" in df.columns:
        df.rename(columns={"CHA" : "CHO"}, inplace=True)
    if "NJN" in df.columns:
        df.rename(columns={"NJN" : "BRK"}, inplace=True)
    if "NOK" in df.columns:
        df.rename(columns={"NOK" : "NLP"}, inplace=True)
    if "NOH" in df.columns:
        df.rename(columns={"NOH" : "NLP"}, inplace=True)
    if "SEA" in df.columns:
        df.rename(columns={"SEA" : "OKC"}, inplace=True)

    # rename team name to current name
    for old in old_names:
        df.loc[df["Team"] == old, "Team"] = current_names[old_names.index(old)]

    # replace vs record into %
    for col in df.columns:
        for i, c in enumerate(df[col]):
            try:
                if str(c).strip()[1] == "-" and str(c).strip()[0].isdigit():
                    record = str(c).strip().split("-")
                    record_l = int(record[0])
                    record_r = int(record[1])
                    percent = str(round(record_l/sum([record_l, record_r]), 4))
                    df[col][i] = percent
            except:
                continue
    dfs.append(df)

os.path.join("data", "clean", "team_vs_team")
for i in range(len(dfs)):
    new_df = dfs[i]
    filename = names[i]
    new_df.to_csv(str(filename), index=False)
