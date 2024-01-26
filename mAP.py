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


y_true1 = [
    "positive",
    "negative",
    "positive",
    "negative",
    "positive",
    "positive",
    "positive",
    "negative",
    "positive",
    "negative",
]

pred_scores1 = [0.7, 0.3, 0.5, 0.6, 0.55, 0.9, 0.75, 0.2, 0.8, 0.3]

y_true2 = [
    "negative",
    "positive",
    "positive",
    "negative",
    "negative",
    "positive",
    "positive",
    "positive",
    "negative",
    "positive",
]

pred_scores2 = [0.32, 0.9, 0.5, 0.1, 0.25, 0.9, 0.55, 0.3, 0.35, 0.85]

thresholds = numpy.arange(start=0.2, stop=0.9, step=0.05)

precisions1, recalls1 = precision_recall_curve(
    y_true=y_true1, pred_scores=pred_scores1, thresholds=thresholds
)


precisions2, recalls2 = precision_recall_curve(
    y_true=y_true2, pred_scores=pred_scores2, thresholds=thresholds
)

precisions1.append(1)
recalls1.append(0)

precisions2.append(1)
recalls2.append(0)

precisions1 = numpy.array(precisions1)
recalls1 = numpy.array(recalls1)

preciimport numpy
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


y_true1 = [
    "positive",
    "negative",
    "positive",
    "negative",
    "positive",
    "positive",
    "positive",
    "negative",
    "positive",
    "negative",
]

pred_scores1 = [0.7, 0.3, 0.5, 0.6, 0.55, 0.9, 0.75, 0.2, 0.8, 0.3]

y_true2 = [
    "negative",
    "positive",
    "positive",
    "negative",
    "negative",
    "positive",
    "positive",
    "positive",
    "negative",
    "positive",
]

pred_scores2 = [0.32, 0.9, 0.5, 0.1, 0.25, 0.9, 0.55, 0.3, 0.35, 0.85]

thresholds = numpy.arange(start=0.2, stop=0.9, step=0.05)

precisions1, recalls1 = precision_recall_curve(
    y_true=y_true1, pred_scores=pred_scores1, thresholds=thresholds
)


precisions2, recalls2 = precision_recall_curve(
    y_true=y_true2, pred_scores=pred_scores2, thresholds=thresholds
)

precisions1.append(1)
recalls1.append(0)

precisions2.append(1)
recalls2.append(0)

precisions1 = numpy.array(precisions1)
recalls1 = numpy.array(recalls1)

precisions2 = numpy.array(precisions2)
recalls2 = numpy.array(recalls2)

AP1 = numpy.sum((recalls1[:-1] - recalls1[1:]) * precisions1[:-1])
print(AP1)


AP2 = numpy.sum((recalls2[:-1] - recalls2[1:]) * precisions2[:-1])
print(AP2)

mAP = (AP1 + AP2) / 2
print(mAP)
