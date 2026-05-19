# Design an experiment to investigate the impact of varying the number of trees in a Random Forest classifier 
# on its performance for a given dataset. Write Python code to implement the Random Forest algorithm with 
# different numbers of trees and evaluate its classification performance using appropriate evaluation

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import *
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("../dataset/diabetes1.csv")
data = data.dropna()
X,y = data.drop(columns=['Outcome']), data.Outcome

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=42)
acc=[]
for t in range(1,101,20):
    model = RandomForestClassifier(n_estimators=t, random_state=42)
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    acc.append(accuracy_score(y_test,y_pred))

plt.plot(range(1,101,20),acc)