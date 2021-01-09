#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:48:37 2021

@author: camillezaug

A simple kmeans example
"""


import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix


# Generate data
data,labels = make_blobs(n_samples=240, centers=3, cluster_std=2.75)

# Plot data
plt.scatter(data[:,0],data[:,1], c = labels, marker = 'o', edgecolor = "k")
plt.show()

# Scale features so that means and stdevs are 0 and 1, respectively
scaler = StandardScaler()
scaledData = scaler.fit_transform(data)

# Now perform kmeans to group the data by clusters
kmeans = KMeans(init = "random",        # Randomly choose first guess of centers
                n_clusters = 3,         # Assume 3 clusters to find
                n_init = 10,            # Perform 10 times (since it's random)
                max_iter = 300)         # update centers max 300 times
                
kmeans.fit(scaledData)

# Get confusion matrix
CM = confusion_matrix(labels, kmeans.labels_)


