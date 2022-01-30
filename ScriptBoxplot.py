# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:39:34 2022

@author: hugog
"""

import pandas as pd 
import seaborn as sns
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

df = pd.read_csv("C://Users//Public//Documents//ProjetTransverse//Data_Transverse//ENTETES_TICKET_V4.csv", sep = '|')


df['TIC_DATE'] = pd.to_datetime(df['TIC_DATE'])
df["TIC_TOTALTTC"]= df['TIC_TOTALTTC'].str.replace(',', '.').astype(float)
df['year'] = pd.DatetimeIndex(df['TIC_DATE']).year
df = df[df['TIC_TOTALTTC'].between(0, 500)]

figure(figsize=(10, 8), dpi=80)
fig = sns.boxplot(y='TIC_TOTALTTC', x='year', 
                 data=df, 
                 palette="colorblind",
                 hue='year')
plt.xlabel("Années")
plt.ylabel("CA total des clients")
plt.title("Boite a moustache du CA TOTAL des clients par annee d'achat") # You can comment this line out if you don't need title
plt.show(fig)