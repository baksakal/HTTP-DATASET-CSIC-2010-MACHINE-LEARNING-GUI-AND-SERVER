from prep import *
import csv
import re
import pandas as pd
import numpy as np
from sklearn import metrics 
from sklearn.model_selection import train_test_split

df = pd.read_csv("output.csv")
df.head()

df_0 = df[df.threat==0]
df_1 = df[df.threat==1]

from sklearn.utils import resample

df_1_up = resample(df_1,replace=True,n_samples=36000,random_state=123)
df = pd.concat([df_0,df_1_up])

x = df.drop("threat",axis = 1)
y = df.threat

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=4)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, log_loss
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier

model = RandomForestClassifier()

model.fit(x_train,y_train)

predictions = model.predict(x_test)

from sklearn.metrics import accuracy_score
print("Accuracy : %.2f"%(accuracy_score(y_test, predictions)*100))

from sklearn.metrics import confusion_matrix
print("Confusion Matrix:\n",  confusion_matrix(y_test, predictions))

from sklearn.metrics import recall_score
print("Recall : %.2f"%(recall_score(y_test, predictions)*100))

from sklearn.metrics import precision_score
print("Precision : %.2f"%(precision_score(y_test, predictions)*100))

from sklearn.metrics import f1_score
print("F1 Score : %.2f"%(f1_score(y_test, predictions)*100))

from sklearn.metrics import roc_auc_score
print("ROC : %.2f"%(roc_auc_score(y_test,predictions)*100))
