# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:12:40 2015

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


pd.set_option('display.mpl_style', 'default')
pd.set_option('display.width' , 5000)
pd.set_option('display.max_columns', 60)


plt.rcParams['figure.figsize'] = (15,5)

path = 'C:/2_python/pandas_cookbook/bikes.csv'

bikes = pd.read_csv(path, sep=';', encoding='latin1', parse_dates = 0, dayfirst = True, index_col = 0)

#print (bikes['Berri 1'].plot())

berri_bikes = bikes[['Berri 1']].copy()

berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday

#print (berri_bikes[:5])

#print (berri_bikes.index.weekday)

weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts.index = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat', 'Sun']

print (weekday_counts)
print (weekday_counts.plot(kind = 'bar'))
