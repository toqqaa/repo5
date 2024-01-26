import numpy
import sklearn.metrics


def precision_recall_curve(y_true, pred_scores, thresholds):
    precisions = []
    recalls = []

    for threshold in thresholds:
        y_pred = [
            "positive" if score >= threshold else "negative" for score in pred_scores
        ]

        precision = sklearn.metrics.precision_score(
            y_true=y_true, y_pred=y_pred, pos_label="positive"
        )
        recall = sklearn.metrics.recall_score(
            y_true=y_true, y_pred=y_pred, pos_label="positive"
        )

        precisions.append(precision)
        recalls.append(recall)

    return precisions, recalls


y_true = [
    "positive",
    "negative",
    "negative",
    "positive",
    "positive",
    "positive",
    "negative",
    "positive",
    "negative",
    "positive",
    "positive",
    "positiveimport numpy
import sklearn.metrics


def precision_recall_curve(y_true, pred_scores, thresholds):
    precisions = []
    recalls = []

    for threshold in thresholds:
        y_pred = [
            "positive" if score >= threshold else "negative" for score in pred_scores
        ]

        precision = sklearn.metrics.precision_score(
            y_true=y_true, y_pred=y_pred, pos_label="positive"
        )
        recall = sklearn.metrics.recall_score(
            y_true=y_true, y_pred=y_pred, pos_label="positive"
        )

        precisions.append(precision)
        recalls.append(recall)

    return precisions, recalls


y_true = [
    "positive",
    "negative",
    "negative",
    "positive",
    "positive",
    "positive",
    "negative",
    "positive",
    "negative",
    "positive",
    "positive",
    "positive",
    "positive",
    "negative",
    "negative",
    "negative",
]
pred_scores = [
    0.7,
    0.3,
    0.5,
    0.6,
    0.55,
    0.9,
    0.4,
    0.2,
    0.4,
    0.3,
    0.7,
    0.5,
    0.8,
    0.2,
    0.3,
    0.35,
]
thresholds = numpy.arange(start=0.2, stop=0.7, step=0.05)

precisions, recalls = precision_recall_curve(
    y_true=y_true, pred_scores=pred_scores, thresholds=thresholds
)

precisions.append(1)
recalls.append(0)

precisions = numpy.array(precisions)
recalls = numpy.array(recalls)

AP = numpy.sum((recalls[:-1] - recalls[1:]) * precisions[:-1])
print(AP)
