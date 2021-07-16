# -*- coding: utf-8 -*-
"""Untitled23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qT5XyOx1PL6BhUjLyrNIuiKr4fWbvTOQ
"""

import pandas as pd
import numpy as np
import pickle

df = pd.read_csv("train_loan.csv")

df['LoanAmount']=df['LoanAmount'].fillna(df['LoanAmount'].mean())
df['Loan_Amount_Term']=df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mean())
df['Credit_History']=df['Credit_History'].fillna(df['Credit_History'].mean())
#df1['LoanAmount']=df1['LoanAmount'].fillna(df1['LoanAmount'].mean())
#df1['Loan_Amount_Term']=df1['Loan_Amount_Term'].fillna(df1['Loan_Amount_Term'].mean())
#df1['Credit_History']=df1['Credit_History'].fillna(df1['Credit_History'].mean())

df['Gender']=df['Gender'].fillna(df['Gender'].mode()[0])
df['Married']=df['Married'].fillna(df['Married'].mode()[0])
df['Dependents']=df['Dependents'].fillna(df['Dependents'].mode()[0])
df['Self_Employed']=df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])
# df1['Gender']=df1['Gender'].fillna(df1['Gender'].mode()[0])
# df1['Married']=df1['Married'].fillna(df1['Married'].mode()[0])
# df1['Dependents']=df1['Dependents'].fillna(df1['Dependents'].mode()[0])
# df1['Self_Employed']=df1['Self_Employed'].fillna(df1['Self_Employed'].mode()[0])

X_train=df.iloc[:,:-1]
y_train=df.iloc[:,-1]
# X_test=df1.iloc[:,:-1]
# y_test=df1.iloc[:,-1]

X_train=X_train.drop(columns='Property_Area')

X_train=X_train.drop(columns='Loan_ID')
# X_test=X_test.drop(columns='Loan_ID')

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
clf.fit(X_train, y_train)

pickle.dump(clf,open('irl.pkl','wb'))

# y_pred=clf.predict(X_test)