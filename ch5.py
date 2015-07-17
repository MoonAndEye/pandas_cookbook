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

#以下的範例不成功，因為對方改了下載地址
path = 'data/weather_2012.csv'

url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"

#url = url_template.format(month = 3, year = 2013)
"""
weather_mar2012 = pd.read_csv (url, skiprows = 15, index_col = 'Date/Time', parse_dates = True, encoding = 'latin1', header = True )

weather_mar2012 = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, encoding='latin1', header=True)
#print (weather__2012_final['Temp (C)'].plot(figsize = (15, 6)))
#print (weather_mar2012[u"Temp (\xc2\xb0C)"].plot(figsize=(15, 5)))

print (url)
"""

def download_weather_month(year, month):
    if month == 1:
        year += 1
    url = url_template.format(year=year, month=month)
    weather_data = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, header=True)
    weather_data = weather_data.dropna(axis=1)
    weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]
    weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time', 'Data Quality'], axis=1)
    return weather_data
    
weather_jan2012 = download_weather_month(2012, 1)[:5]

print (weather_jan2012)
