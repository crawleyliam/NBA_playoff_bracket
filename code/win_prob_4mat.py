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

df2 = df[16:31]

list2 = df2.values.tolist()

list2.insert(1, [1])

dftwo = pd.DataFrame(list2)

print (dftwo)

 

"BOS"

df3 = df[32:47]

list3 = df3.values.tolist()

list3.insert(2, [1])

dfthree = pd.DataFrame(list3)

print (dfthree)

 

"CHI"

df4 = df[48:63]

list4 = df4.values.tolist()

list4.insert(3, [1])

dffour = pd.DataFrame(list4)

print (dffour)

 

"DAL"

df5 = df[64:79]

list5 = df5.values.tolist()

list5.insert(4, [1])

dffive = pd.DataFrame(list5)

print (dffive)

 

"DEN"

df6 = df[80:95]

list6 = df6.values.tolist()

list6.insert(5, [1])

dfsix = pd.DataFrame(list6)

print (dfsix)

 

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


