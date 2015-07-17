# -*- coding: utf-8 -*-
"""
這個 chapter有問題
可能是資料來源卡住了，後面的方法換不出來


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

pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

path = 'data/311-service-requests.csv'
na_values = ['NO CLUE', 'N/A', '0']

requests = pd.read_csv(path, na_values = na_values, dtype = {'Incident Zip': str})
#requests = pd.read_csv(path, dtype = {'Incident Zip': str})
#print (requests[:10])
"""
rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
print (len(len(requests[rows_with_dashes])))

"""

print (requests[requests['Incident Zip'] == '00000'])