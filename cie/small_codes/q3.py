# Implement linear and logistic regression and test it using any dataset. 
# Give new test data and predict the output. Print the confusion matrix, accuracy, precision, recall, MSE, RMSE etc. 
# Compare and write the inference.

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import *
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


X = [
    [1,2,3,4],
    [5,2,4,4],
    [11,22,13,34],
    [51,32,43,42],
    
    [10,20,30,40]
]
y_r = [
    1,2,3,4,5
]
y_c = [
    1,0,1,0,1
]

lin_mod = LinearRegression()
log_mod = LogisticRegression()

lin_mod.fit(X,y_r)
log_mod.fit(X,y_c)

r_pred = lin_mod.predict(X)
c_pred = log_mod.predict(X)

print("Accuracy: ", accuracy_score(y_c,c_pred))
cm = confusion_matrix(y_c,c_pred)
print(cm)

mse = mean_squared_error(y_r, r_pred)
print(mse)