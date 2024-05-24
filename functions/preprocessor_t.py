def preprocessor_t(X_train):
    """
    Initial preprocessing of categorical data before model training.
    """

    from sklearn.preprocessing import OneHotEncoder
    from sklearn.compose import ColumnTransformer
    cat_labels = X_train.select_dtypes('object').columns


    cat_preprocess = OneHotEncoder(drop='first', handle_unknown='ignore')
    preprocessor = ColumnTransformer([('cat', cat_preprocess, cat_labels)])
    return preprocessor