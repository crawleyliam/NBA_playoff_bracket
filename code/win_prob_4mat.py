import os
import pandas as pd

###  cd ~/NBA_playoff_bracket

output = "artifacts"
outpath = os.path.join(output, "reformatted_probs.csv")

nbapath = os.path.join("artifacts", "all_2022_matchups.csv")
df = pd.read_csv(nbapath)
df = df.drop("Home_TeamID", 1)
df = df.drop("Away_TeamID", 1)


"ATL"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(1, [1])

dfone = pd.DataFrame(list1)

# print (dfone)


"BKN"

df2 = df[15:30]

list2 = df2.values.tolist()

list2.insert(7, [1])

dftwo = pd.DataFrame(list2)

# print (dftwo)


"BOS"

df3 = df[30:45]

list3 = df3.values.tolist()

list3.insert(6, [1])

dfthree = pd.DataFrame(list3)

# print (dfthree)


"CHI"

df4 = df[45:60]

list4 = df4.values.tolist()

list4.insert(5, [1])

dffour = pd.DataFrame(list4)

# print (dffour)


"DAL"

df5 = df[60:75]

list5 = df5.values.tolist()

list5.insert(10, [1])

dffive = pd.DataFrame(list5)

# print (dffive)


"DEN"

df6 = df[75:90]

list6 = df6.values.tolist()

list6.insert(13, [1])

dfsix = pd.DataFrame(list6)

#print (dfsix)


"GSW"

df7 = df[90:105]

list7 = df7.values.tolist()

list7.insert(12, [1])

dfseven = pd.DataFrame(list7)

# print (dfseven)


"MEM"

df8 = df[105:120]

list8 = df8.values.tolist()

list8.insert(14, [1])

dfeight = pd.DataFrame(list8)

# print (dfeight)


"MIA"

df9 = df[120:135]

list9 = df9.values.tolist()

list9.insert(0, [1])

dfnine = pd.DataFrame(list9)

# print (dfnine)


"MIL"

df10 = df[135:150]

list10 = df10.values.tolist()

list10.insert(4, [1])

dften = pd.DataFrame(list10)

# print (dften)


"MIN"

df11 = df[150:165]

list11 = df11.values.tolist()

list11.insert(15, [1])

dfeleven = pd.DataFrame(list11)

# print (dfeleven)


"NOP"

df12 = df[165:180]

list12 = df12.values.tolist()

list12.insert(9, [1])

dftwelve = pd.DataFrame(list12)

# print (dftwelve)


"PHI"

df13 = df[180:195]

list13 = df13.values.tolist()

list13.insert(2, [1])

dfthirteen = pd.DataFrame(list13)

# print (dfthirteen)


"PHX"

df14 = df[195:210]

list14 = df14.values.tolist()

list14.insert(8, [1])

dffourteen = pd.DataFrame(list14)

# print (dffourteen)


"TOR"

df15 = df[210:225]

list15 = df15.values.tolist()

list15.insert(3, [1])

dffifteen = pd.DataFrame(list15)

# print (dffifteen)


"UTA"

df16 = df[225:240]

list16 = df16.values.tolist()

list16.insert(11, [1])

dfsixteen = pd.DataFrame(list16)

# print (dfsixteen)

merged_teams = pd.concat([dfnine, dfone, dfthirteen, dffifteen, dften, dffour, dfthree, dftwo, dffourteen, dftwelve, dffive, dfsixteen, dfseven, dfsix, dfeight, dfeleven],
 axis=1, join="outer")

# print(merged_teams)

merged_teams.to_csv(outpath)
