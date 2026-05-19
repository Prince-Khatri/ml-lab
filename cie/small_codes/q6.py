# Create a dataset and Perform the necessary pre-processing steps. Train the model using Naive Bayes Classifier. 
# Give new test data and predict the classification output.Analyze and write the

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak'],
    'play': ['No', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)
le = LabelEncoder()
for col in df.columns:
    df[col] = le.fit_transform(df[col])
X = df.drop(columns=['play']).values
y= df['play'].values.astype(int)



X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)