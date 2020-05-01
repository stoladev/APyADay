# What is linear regression?
# -When you have data that directly correlates with other data, you can
#  predict certain values using a portion of that data.


import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import pickle
import matplotlib.pyplot as pyplot
from matplotlib import style


data = pd.read_csv('student-mat.csv', sep=';')
data = data[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]

predict = 'G3'

X = np.array(data.drop([predict], 1))
Y = np.array(data[predict])

skl_ms = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)
x_train, x_test, y_train, y_test = skl_ms

"""
best = 0
for _ in range(100):
    skl_ms = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)
    x_train, x_test, y_train, y_test = skl_ms

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    accuracy = linear.score(x_test, y_test)
    print(accuracy)

    if accuracy > best:
        best = accuracy
        with open('studentmodel.pickle', 'wb') as f:
            pickle.dump(linear, f)
"""

pickle_in = open('studentmodel.pickle', 'rb')
linear = pickle.load(pickle_in)

print("Coefficient: \n", linear.coef_)
print("Intercept: \n", linear.intercept_)

predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

p = 'studytime'
style.use('ggplot')
pyplot.scatter(data[p], data['G3'])
pyplot.xlabel(p)
pyplot.ylabel('Final Grade')
pyplot.show()
