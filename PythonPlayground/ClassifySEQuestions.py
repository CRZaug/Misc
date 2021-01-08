#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:43:26 2021

@author: camillezaug
"""

import numpy as np
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer,CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

N = 20219


output = pd.DataFrame()

filename = 'SECategorizationData.txt'
  
  
# creating dictionary 
with open(filename) as fh: 
  
    k = 0
    
    for line in fh: 
        if k ==0:
            number = int(line)
        else:
        
            d = json.loads(line)
            
            output = output.append(d, ignore_index=True)
            

        k+=1
        

X = output.question

y = output.topic


X_train, X_test, y_train, y_test = train_test_split(X.T, y, test_size=0.33)


nbClassifier = MultinomialNB(alpha = 1.0, class_prior=None, fit_prior = True)


# Perform tf-idf vectorization

model = Pipeline([('vect', CountVectorizer()),
					 ('tfidf', TfidfTransformer()),
					 ('clf', MultinomialNB())
					 ])

# Fit the model
model.fit(X_train,y_train)

# Generate a confusion matrix
pred = model.predict(X_test)


cm = confusion_matrix(np.array(y_test), pred)