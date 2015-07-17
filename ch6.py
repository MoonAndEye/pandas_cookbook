# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 18:12:53 2015

@author: Moon
"""
import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.mpl_style', 'default')
plt.rcParams['figure.figsize'] = (8, 3)
plt.rcParams['font.family'] = 'sans-serif'

#以下的範例不成功，因為對方改了下載地址
path = 'data/weather_2012.csv'

weather_2012 = pd.read_csv(path, parse_dates = True, index_col = 'Date/Time')

weather_description = weather_2012['Weather']
is_snowing = weather_description.str.contains('Snow')
is_snowing = is_snowing.astype(float).resample('M', how=np.mean)
print (is_snowing)

#a = weather_2012['Temp (C)'].resample('M', how=np.median).plot(kind='bar')
b = is_snowing.plot(kind = 'bar')
#print (a)

