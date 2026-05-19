# Build a KNN model for predicting if a person will have diabetes or not with a high accuracy score. 
# erform some appropriate Pre-Processing steps on the given dataset for better results. Implement the 
# KNN algorithm on your own. Try other possible processes that can be done to dataset and tuning the model 
# to increase accuracy such as Increase K value, Normalization and Different Distance Metrics

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def dist_1(a,b):
    return np.sum(np.abs(a-b),axis=1)

def dist_2(a,b):
    return np.sqrt(np.sum((a-b)**2,axis=1))


def knn(X_train, y_train, X_test, k, dist_func):
    pred=[]
    for test in X_test:
        dist = dist_func(X_train,test)
        k_labels = y_train[np.argsort(dist)[:k]]
        p = np.bincount(k_labels).argmax()
        pred.append(p)
    return pred
ks=[1,3,5,10]
dist = [dist_1, dist_2]

df = pd.read_csv('../dataset/diabetes1.csv')
df = df.dropna()
sc = StandardScaler()

X = df.drop(columns=['Outcome']).values
y= df['Outcome'].values.astype(int)



X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

plot_data = []

for d in dist:
    print(d.__name__)
    acc = []
    for k in ks:
        pred = knn(X_train, y_train, X_test, k, d)
        acc.append(accuracy_score(y_test, pred))
    plot_data.append(acc)

plt.plot(ks,plot_data[0],color='r')
plt.plot(ks,plot_data[1])