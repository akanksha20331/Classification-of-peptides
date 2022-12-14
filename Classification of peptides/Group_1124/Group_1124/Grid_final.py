# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bV3AR2p-ifl07f2g6J7dsIV55K6FyNCJ
"""


import sklearn


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.metrics import roc_curve
from sklearn.metrics import auc


import os
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score,f1_score

tr = pd.read_csv("final_amino_acid_result.csv")
te = pd.read_csv("test_amino_acid_result (1).csv")

trr = pd.read_csv("train (2).csv")

Y= trr[['Label']]

te

# removing first coloumn from a pandas dataframe
tr = tr.iloc[: , 1:]

# removing first coloumn from test data
te= te.iloc[:,1:]

Y= trr[['Label']]

sc=StandardScaler()
c2=pd.DataFrame(sc.fit_transform(tr))
c2.columns=tr.columns
c2.head()

sc=StandardScaler()
c3=pd.DataFrame(sc.fit_transform(te))
c3.columns=te.columns
c3.head()



from sklearn import svm
from sklearn.model_selection import GridSearchCV

rfc = RandomForestClassifier()
params = [{'max_depth': list(range(5, 15)), 'max_features': list(range(0,14))}]
clf= GridSearchCV(rfc,params)
clf.fit(tr, Y.values.ravel())

print(clf.best_params_)

print(clf.best_score_)

Y_pred= clf.predict(te)

with np.printoptions(threshold=np.inf):
   print(Y_pred)

print("Enter Sample File address")
sample = pd.read_csv(r"{}".format(input()))

sample[sample.columns[1]] = Y_pred

sample.columns = ['ID', 'Lable']

sample.to_csv("resultSVMFILTER.csv", index=False)

