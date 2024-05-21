def true_pos_ratio(y_test, y_pred):
    """
    Calculation of true positive rate.
    """
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)
    tp = cm[1][1]
    rate = tp / sum(sum(cm))
    return rate