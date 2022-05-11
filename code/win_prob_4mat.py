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

df7 = df[96:111]

list7 = df7.values.tolist()

list7.insert(6, [1])

dfseven = pd.DataFrame(list7)

print (dfseven)

 

"MEM"

df8 = df[112:127]

list8 = df8.values.tolist()

list8.insert(7, [1])

dfeight = pd.DataFrame(list8)

print (dfeight)

 

"MIA"

df9 = df[128:143]

list9 = df9.values.tolist()

list9.insert(8, [1])

dfnine = pd.DataFrame(list9)

print (dfnine)

 

"MIL"

df10 = df[144:159]

list10 = df10.values.tolist()

list10.insert(9, [1])

dften = pd.DataFrame(list10)

print (dften)

 

"MIN"

df11 = df[160:174]

list11 = df11.values.tolist()

list11.insert(10, [1])

dfeleven = pd.DataFrame(list11)

print (dfeleven)

 

"NOP"

df12 = df[175:191]

list12 = df12.values.tolist()

list12.insert(11, [1])

dftwelve = pd.DataFrame(list12)

print (dftwelve)

 

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


