import pandas as pd
import numpy as np
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


df = pd.read_csv('../data/titanic.csv')

df = pd.get_dummies(df, columns=['sex', 'pclass'], drop_first=True)

selected_features = ['fare', 'pclass_2', 'pclass_3', 'sex_male']

X = df[selected_features]

y = df['survived']


model = LogisticRegression()

model.fit(X, y)


pickle.dump(model, open('models/model.pkl', 'wb'))

