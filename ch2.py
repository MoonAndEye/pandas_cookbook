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

path = '311-service-requests.csv'

complaints = pd.read_csv(path)

#print (complaints['Complaint Type'])
print (complaints['Complaint Type'][:5])
