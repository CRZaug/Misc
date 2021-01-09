#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:22:39 2021

@author: camillezaug

Calculate the MSE of a linear regression model using Leave One Out validation
"""


import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import LeaveOneOut



A = np.random.rand(100,1)
B= np.random.rand(100,1)

loo = LeaveOneOut()

loo.get_n_splits(A)

model= LinearRegression()

error = []

for train_index, test_index in loo.split(A):
    
    model.fit(A[train_index],B[train_index])
        
    prediction = np.matmul(model.coef_,[A[test_index]])

    error.append((prediction-B[test_index])**2)

MSE = 1/len(A) * sum(error)

print(MSE)