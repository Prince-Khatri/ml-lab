# Using any dataset, calculate TP, TN, FP ,FN and different metrics (Accuracy, Precision, Recall(Sensitivity), 
# F1-Score, MCC, Specificity, Negative Predictive Value) by defining your own functions. Compare your values 
# with scikit-learn's library functions. Get the result of Confusion Matrix using sklearn. Using sklearn, 
# plot the ROC & AUC Curves for your test data and random probabilities. 
# Using sklearn, calculate the AUC of your test data and of random probabilities. Interpret the results. 
# Write the inference/analysis of each output.

from sklearn.metrics import *
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = load_breast_cancer()
X=data.data
y=data.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LogisticRegression()

model.fit(X_train,y_train)

y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:,1]

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()
print(cm)
print(cm.ravel)
def custom(tp,fp,fn,tn):
    acc = (tp+tn)/(tp+fp+fn+tn)
    pre = tp/(tp+fp)
    rec = tp/(tp+fn)
    spe = tn/(tn+fp)
    f1 = 2*pre*rec/(pre+rec)
    npv = tn/(tn+fn)
    mcc = ((tp*tn)-(fp*fn))/np.sqrt((tp+fp)*(tn+fp)*(tp+fn)*(tn+fn))
    return acc, pre, rec, spe, f1, npv, mcc

def built_in(y_true,y_pred):
    acc = accuracy_score(y_true,y_pred)
    pre = precision_score(y_true,y_pred)
    rec = recall_score(y_true,y_pred)
    spe = tn/(tn+fp)
    f1 = f1_score(y_true,y_pred)
    npv = tn/(tn+fn)
    mcc = matthews_corrcoef(y_true,y_pred)

    return acc, pre, rec, spe, f1, npv, mcc

col =[ "acc", "pre", "rec", "spe", "f1", "npv", "mcc"]

metrics = pd.DataFrame([ custom(tp,fp,fn,tn),built_in(y_test,y_pred)], columns=col)

print(metrics.head())
rand = np.random.rand(len(y_test))
fpr,tpr,_ = roc_curve(y_test, y_proba)
plt.plot(fpr,tpr)
fpr,tpr,_ = roc_curve(y_test, rand)
plt.plot(fpr,tpr)
plt.plot([0,1],[0,1])

roc_m = roc_auc_score(y_test, y_proba)
roc_r = roc_auc_score(y_test, rand)
print(roc_m, roc_r)