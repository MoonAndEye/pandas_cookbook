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

path = 'C:/2_python/pandas_cookbook/311-service-requests.csv'

complaints = pd.read_csv(path)

#complaints_counts = complaints['Complaint Type'].value_counts()

#noise_complaints = complaints[complaints['Complaint Type'] == "Noise - Street/Sidewalk"]

is_noise = complaints['Complaint Type'] == 'Noise - Street/Sidewalk'
in_brooklyn = complaints['Borough'] == 'BROOKLYN'
noise_complaints = complaints[is_noise]
noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()

"""
a = pd.Series([1,2,3]).values
b = np.array([1,2,3])
b = b[b != 2]
"""

#print (complaints['Complaint Type'])
#print (a)
#print (b)
a = noise_complaint_counts / complaint_counts.astype(float)
print (a.plot(kind = 'bar'))
