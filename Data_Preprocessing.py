#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import numpy as np

df=pd.read_csv("Data.csv")
print('Original Data : \n',df)

x = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values = np.nan , strategy = 'mean')
imp.fit(x[:,1:3])
x[:,1:3]=imp.transform(x[:,1:3])
print('transform Data : \n',x)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
T = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')
P = np.array(T.fit_transform(x))
print('For Non-Numerical-Country- data For X Part :\n',P)

from sklearn.preprocessing import LabelEncoder
L = LabelEncoder()
y = L.fit_transform(y)
print('For Y Part : \n',y)


# In[ ]:




