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
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

path = 'data/weather_2012.csv'


url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"

url = url_template.format(month = 3, year = 2013)
weather_mar2012 = pd.read_csv (url, skiprows = 15, index_col = 'Date/Time', parse_dates = True, encoding = 'latin1', header = True )

weather__2012_final = pd.read_csv (path, index_col = 'Date/Time')
#print (weather__2012_final['Temp (C)'].plot(figsize = (15, 6)))
print (weather__2012_final[u"Temp (\xc2\xb0C)"].plot(figsize=(15, 5)))

