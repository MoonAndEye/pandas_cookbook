# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 01:46:06 2015

@author: Moon
"""
import sqlite3
import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path = 'data/weather_2012.sqlite'

con = sqlite3.connect(path)
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
print (df)