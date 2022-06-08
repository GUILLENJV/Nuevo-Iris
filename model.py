from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import pickle
import os


X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

clf = RandomForestClassifier()
print(clf.fit(X_train, y_train).score(X_test, y_test))

filepath = 'model.pkl'
#pickle.dump(clf, open(filepath, 'wb'))

loaded_model = pickle.load(open(filepath, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)
print(loaded_model.predict([[5.6, 2.7, 4.2, 1.3]]))