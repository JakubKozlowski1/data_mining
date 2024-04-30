def missclassification_rate(y_test, y_pred):
    """
    Calculation of missclassifictation rate.
    """
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)
    fn = cm[1][0]
    fp = cm[0][1]
    rate = (fn+fp) / sum(sum(cm))
    return rate