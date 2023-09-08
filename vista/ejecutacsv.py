import pandas as pd 
import random 
import numpy as np
import matplotlib.pyplot as plt 
df=pd.read_csv("surveys.csv")
df2=pd.read_csv("species.csv")
print(df.columns)
print(df2.columns)
#df3 = pd.merge(left=df,right=df2, left_on='species_id', right_on='species_id')
df4 = pd.merge(left=df,right=df2, how='left', left_on='species_id', right_on='species_id')
print(df4)


data2 = df[df['sex']=='F'].count()
data3 = df[df['sex']=='M'].count()
#print(data3)
#df=pd.unique(df['species_id'])
#print(df['weight'].describe())
#print(df)
#print(data2.describe())
#species_counts = df.groupby('species_id')['record_id'].count()
#df=df.groupby('species_id')['record_id'].count()['DO']
#print(species_counts)
#print(df)
#df = df.groupby('species_id')['record_id'].count()
#print(species_counts)
#df.plt()
#print(species_counts)
#y=species_counts['species_id']
#print(y)
#fig, ax = plt.subplots()
#df.loc[0, ['species_id', 'plot_id', 'weight']]
#df.iloc[0:4, 1:4]
#df=pd.isnull(df).sum()
#print(df)
#ax.stem(x, y)

#plt.show()

#df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))

#df = df.cumsum()

#plt.figure();

#df.plot();
#df2 = pd.DataFrame(np.random.rand(10, 4), columns=["a", "b", "c", "d"])

#df2.plot.bar()