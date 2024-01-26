import numpy
import sklearn.metrics

y_true = [
    "positive",
    "negative",
    "negative",
    "positive",
    "positive",
    "positive",
    "negative",
]
y_pred = [
    "positive",
    "negative",
    "positive",
    "positive",
    "negative",
    "positive",
    "positive",
]

r = sklearn.metrics.confusion_matriimport numpy
import sklearn.metrics

y_true = [
    "positive",
    "negative",
    "negative",
    "positive",
    "positive",
    "positive",
    "negative",
]
y_pred = [
    "positive",
    "negative",
    "positive",
    "positive",
    "negative",
    "positive",
    "positive",
]

r = sklearn.metrics.confusion_matrix(y_true, y_pred)

r = numpy.flip(r)

acc = (r[0][0] + r[-1][-1]) / numpy.sum(r)
print(acc)
