# Build a K-Means Model for any dataset. Assume K value as 2,3,4 .
# Compare and interpret the results of different

from sklearn.cluster import KMeans
from sklearn.metrics import *
from sklearn.datasets import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X,y = make_blobs(n_samples=10)

for k in [2,3,4]:
    model = KMeans(n_clusters=k)
    model.fit(X)
    labels = model.labels_
    plt.subplot(1,3,k-1)
    plt.scatter(X[:,0],X[:,1],c=labels)
    center = model.cluster_centers_
    plt.scatter(center[:,0],center[:,1],s=100, color='r')