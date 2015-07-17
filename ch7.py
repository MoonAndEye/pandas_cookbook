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

pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

path = 'data/311-service-requests.csv'

requests = pd.read_csv(path)