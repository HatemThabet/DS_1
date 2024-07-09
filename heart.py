import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



dataset=pd.read_csv('heart.csv')
df=dataset.copy()
df.isnull().sum()
#sns.boxplot(df.Age)


df.isnull().sum()

#categorical


cols1=['Sex','ChestPainType','RestingECG','ExerciseAngina','ST_Slope']

df[cols1]=df[cols1].fillna(df.mode().iloc[0])

#numerical
cols2=['Age','RestingBP','Cholesterol','FastingBS','MaxHR','Oldpeak','HeartDisease']

df[cols2]=df[cols2].fillna(df.mean())

df.Age.hist()

sns.boxplot(df.Age)



#outliers*******************************

df[df.Age>60].shape

df.Age.hist()






