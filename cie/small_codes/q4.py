# Write a program to demonstrate the working of the decision tree based ID3 algorithm Use an appropriate data set for 
# building the decision tree and apply this knowledge to classify a new sample. Interpret the results.
#  Write the inference/analysis of each output

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import *
import pandas as pd
# ID3
data = {
    'Outlook':['Sunny','Sunny','Overcast','Rainy','Rainy'],
    'Humidity': ['High', 'High', 'High', 'Normal', 'Normal'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Strong'],
    'Play':['No','No','Yes','Yes','No']
}

df = pd.DataFrame(data)

X = df.drop(columns=['Play'])
y = df['Play']


model = DecisionTreeClassifier()

model.fit(X,y)

y_pred = model.predict(X)

print("Accuracy: ", accuracy_score(y, y_pred))

plot_tree(model)