# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:12:40 2015

"""

import pandas as pd
import matplotlib.pyplot as plt
import os, sys


pd.set_option('display.mpl_style', 'default')
pd.set_option('display.width' , 5000)
pd.set_option('display.max_columns', 60)


plt.rcParams['figure.figsize'] = (15,5)

path = 'C:/2_python/pandas_cookbook/bikes.csv'


fixed_df = pd.read_csv(path, sep=';', encoding='latin1', parse_dates = 1, dayfirst = True, index_col = 0)

fixed_df.plot(figsize = (15,10))
