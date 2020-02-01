import pandas as pd
import numpy as np

df=pd.Series(np.arange(1,51,0.5))

#  checking the dimension of dataframe
# print (df)
print('\n\ndimension of df :', df.ndim)

# checking the ros axes of dataframe

print('\n\naxes of df :',df.axes)

# checking the values of dataframe without labels

print('\n\n df values\n\n',df.values)


pf=pd.DataFrame({'a':pd.Series(np.arange(1,51)),'b':pd.Series(np.arange(51,101))})

# print(pf)

print('\n\nhead of pf dataframe : \n\n',pf.head(12))
print('\n\n',pf.values)

oe={'odd':np.arange(1,100,2),'even':np.arange(0,100,2)}

print(oe['odd'])
print(oe['even'])

oef=pd.DataFrame(oe)
print(oef)

# checking the sum of each column

print('sum of values \n\n\n',oef.sum())

# checking the standard deviation of dataframe

print('standard deviation of values : \n\n\n\n',oef.std())


# Iteration of itmes

df=pd.DataFrame(np.random.rand(5,4),columns=['col1','col2','col3','col4'])
print('\n\ncolumn wise iteration\n\n')
for key , value in df.iteritems():
    print(key, value)

print('\n\nrow wise iteration \n\n')

for key ,value in df.iterrows():
    print(key , value)

print('\n\n tuple iteration row wise\n\n')

for row in df.itertuples():
    print(row)

print('\n\n group by operation\n\n')

world_cup={'Team':['West Indies','West Indies','India','Austrelia','Pakistan','Srilanka','Austrelia','Austrelia',\
                   'Austrelia','India','Austrelia'],'Rank':[7,7,2,1,6,4,1,1,1,2,1],'Year':[1975,1979,1983,1987,1992,\
                                                                                           1996,1999,2003,2007,2011,2015]}
df=pd.DataFrame(world_cup)
print(df)
print('\n\n printing group by\n\n')
print(df.groupby('Team').groups)
print('\n\ngroup by  multiple field\n\n')
print(df.groupby(['Team','Rank']).groups)
grouped=df.groupby('Team')

for name , group in grouped:
    print(name , group)
    print('***************************************************************************************')



print('\n\nconcatenating the dataframs\n\n')
world_champions={'Team':['India','Australia','west Indies','Srilanka','Pkmkb']\
    ,'ICC_Rank':[2,3,7,4,8],'World_CHampion_Yaer':[2011,2015,1979,1996,1992],'Points':[874,787,753,855,673]}
chokers={'Team':['South Africa','NewZealand','Zimbabwe'],'ICC_Rank':[1,5,9],'Points':[895,764,656]}

df1=pd.DataFrame(world_champions)
df2=pd.DataFrame(chokers)
print(pd.concat([df1,df2]))


print('\n\nappending of dataframes\n\n')

print(df1.append(df2))

print(df2.append(df1))

print('\n\n x-axis concatenation \n\n',pd.concat([df1,df2],axis=0))

print('\n\n y-axis concatenation \n\n',pd.concat([df1,df2],axis=1))


print('\n\n merging and joining of dataframes\n\n')

Match_stats={'Team':['India','Australia','west Indies','Srilanka','Pkmkb'],\
             'World_cup_played':[11,10,11,8,9],'ODI_Played':[733,988,712,662,679]}

df3=pd.DataFrame(Match_stats)

print(pd.merge(df1,df3,on='Team'))
print('\n\nleft join\n\n')
print(pd.merge(df1,df2,on='Team',how='left'))
print('\n\nright join\n\n')
print(pd.merge(df1,df2,on='Team',how='right'))
print('\n\nouter join\n\n')
print(pd.merge(df1,df2,on='Team',how='outer'))
print('\n\ninner join\n\n')
print(pd.merge(df1,df3,on='Team',how='inner'))



