# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 01:46:06 2015

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

path = 'data/popularity-contest'

popcon = pd.read_csv(path, sep = ' ', )[:-1]
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']

print (popcon [:5])