import os
import pandas as pd

###  cd ~/NBA_playoff_bracket

nbapath = os.path.join("artifacts", "all_2022_matchups.csv")
df = pd.read_csv(nbapath)
df = df.drop('Home_TeamID', 1)
df = df.drop('Away_TeamID', 1)

 
"ATL"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)



"BKN"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"BOS"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"CHI"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"DAL"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"DEN"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"GSW"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"MEM"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"MIA"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"MIL"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"MIN"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"NOP"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"PHI"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"PHX"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"TOR"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)

 

"UTA"

df1 = df[0:15]

list1 = df1.values.tolist()

list1.insert(0, [1])

dfone = pd.DataFrame(list1)

print (dfone)


