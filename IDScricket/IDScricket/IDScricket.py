import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Batsman_Data.csv")   # reading all the rows and columns
#Since a player did not bat in a particular match I'm using df.replace()

df=df.replace("DNB",-1)
df=df.replace("-",0)
#TO replace v India and so on to India 


a = ["India","Australia","England","Bangladesh","West Indies","Afghanistan","Pakistan","South Africa","Ireland","Zimbabwe","New Zealand","U.A.E","Netherlands","Sri Lanka","Scotland","Kenya"]
a1 = ["v India","v Australia","v England","v Bangladesh","v West Indies","v Afghanistan","v Pakistan","v South Africa","v Ireland","v Zimbabwe","v New Zealand","v U.A.E.","v Netherlands","v Sri Lanka","v Scotland","v Kenya"]

for i in range(0,16,1):
    df=df.replace(a1[i],a[i])
#print(df)

df1=pd.read_csv("Bowler_data.csv")
   #dropping first column 
#Replacing average to 0 when the bowler doesn't take any wickets in that match
df1=df1.replace("-",0)


        
a2=list(set(df1['Opposition']))
a3= ["India","Australia","England","Bangladesh","West Indies","Afghanistan","Pakistan","South Africa","New Zealand","Sri Lanka"]
a4=[]
for i in a2:
    a4.append(i[2:])
a5=list(set(a4)-set(a3))
a6=[]
for j in a5:
    a6.append("v "+j)




for i in range(0,len(a6),1):
        
        df1=df1.replace(a6[i],np.nan)
    
df1=df1.dropna()
#df1=df1.drop(df.columns[0],axis=1)
for i in df1:
    df1.loc[df1['Opposition']=='v India', 'Opposition']='India'
    df1.loc[df1['Opposition']=='v Australia','Opposition']='Australia'
    df1.loc[df1['Opposition']=='v Sri Lanka','Opposition']='Sri Lanka'
    df1.loc[df1['Opposition']=='v New Zealand','Opposition']='New Zealand'
    df1.loc[df1['Opposition']=='v South Africa','Opposition']='South Africa'
    df1.loc[df1['Opposition']=='v Afghanistan','Opposition']='Afghanistan'
    df1.loc[df1['Opposition']=='v Pakistan','Opposition']='Pakistan'
    df1.loc[df1['Opposition']=='v West Indies','Opposition']='West Indies'
    df1.loc[df1['Opposition']=='v England','Opposition']='England'
    df1.loc[df1['Opposition']=='v Bangladesh','Opposition']='Bangladesh'

df2=pd.read_csv("Ground_Averages.csv")
df2=df2.drop(['Span','NR'],axis=1)
#print(df2)

df3=pd.read_csv("ODI_Match_Totals.csv")
df3=df3.drop(['Country_ID','Start Date','Match_ID'],axis=1)
df3=df3.drop(df3.columns[0],axis=1)
op=list(set(df3['Opposition']))
op1=["India","Australia","England","Bangladesh","West Indies","Afghanistan","Pakistan","South Africa","New Zealand","Sri Lanka"]
op2=[]
for i in op:
    op2.append(i[2:])
op3=list(set(a4)-set(a3))
op4=[]
for j in op3:
    op4.append("v "+j)
for i in range(0,len(op4),1):
        
        df3=df3.replace(op4[i],np.nan)
k=0
"""for i in df3:
    for j in op4:
        if(i[6]==j):
            df3=df3.drop(df.rows[k])
    k=k+1"""

for i in df3:
    df3.loc[df3['Opposition']=='v India', 'Opposition']='India'
    df3.loc[df3['Opposition']=='v Australia','Opposition']='Australia'
    df3.loc[df3['Opposition']=='v Sri Lanka','Opposition']='Sri Lanka'
    df3.loc[df3['Opposition']=='v New Zealand','Opposition']='New Zealand'
    df3.loc[df3['Opposition']=='v South Africa','Opposition']='South Africa'
    df3.loc[df3['Opposition']=='v Afghanistan','Opposition']='Afghanistan'
    df3.loc[df3['Opposition']=='v Pakistan','Opposition']='Pakistan'
    df3.loc[df3['Opposition']=='v West Indies','Opposition']='West Indies'
    df3.loc[df3['Opposition']=='v England','Opposition']='England'
    df3.loc[df3['Opposition']=='v Bangladesh','Opposition']='Bangladesh'
df3=df3.replace("Newzealad","New Zealand")

#####################
p=list(set(df1['Wkts']))
for i in range(0,len(p),1):
    df1=df1.replace(p[i],int(p[i]))
    
#print(df1.groupby(['Bowler','Opposition']).Wkts.mean())


    
print(df.groupby('Batsman').transform(lambda x: (x - x.mean()) / x.std()))











