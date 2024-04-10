def remove_outliers_iqr(df, columns):
    for i in columns:
        if i != 'EVENT_LABEL':
            q1 = df[i].quantile(0.25)
            q3 = df[i].quantile(0.75)
            iqr = q3-q1
            low = q1 - 1.5 * iqr
            high = q3 + 1.5 * iqr
        
        df = df[(df[i] >= low) & (df[i] <= high)]
    return df