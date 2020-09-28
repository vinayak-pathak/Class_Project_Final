# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:36:27 2020

@author: COLDD03
"""
##


import numpy as np
import pandas as pd
data = pd.read_pickle("C:\\Users\\COLDD03\\Desktop\\Project_Dataset\\WESAD\\S8\\S8.pkl")
#%%
eda = data["signal"]["chest"]["EDA"]
#%%
array2 = np.array([i for i in eda if ((i>11.48)&(i<11.50))])
#%%
arraylist = np.where(eda==array2[1])[0]
#%%

min(eda[0:700*60])
#%%

