def preprocessor(X_train):
    """
    Initial preprocessing of data before model training.
    Standard scaler and one hot encoder.
    """

    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.compose import ColumnTransformer
    num_labels = X_train.select_dtypes('number').columns
    cat_labels = X_train.select_dtypes('object').columns

    num_preprocess = StandardScaler()
    cat_preprocess = OneHotEncoder(drop='first', handle_unknown='ignore')
    preprocessor = ColumnTransformer([('cat', cat_preprocess, cat_labels),
                                  ('num', num_preprocess, num_labels)])
    return preprocessor