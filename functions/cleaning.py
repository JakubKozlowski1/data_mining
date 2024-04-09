def cleaning():
    """
    Function that deletes ID columns, checks for missing data points and handles them.
    It's also create new features: browser and os.
    
     Input:
        df (pd.DataFrame): Raw data

     Output:
        df (pd.DataFrame): DataFrames ready for further processing.
    """
    # Imports
    import pandas as pd
    from functions.os_selection import os_selection
    import os
    
    path = os.getcwd() + '/data/fraud_challenge_150k.csv'
    df = pd.read_csv(path)
    
    
    df = df.drop(columns=['applicant_name','phone_number','applicant_name',
                        'billing_address', 'merchant_id', 'cvv',
                        'email_domain', 'EVENT_TIMESTAMP','ip_address',
                        'billing_city','billing_postal','billing_state',
                        'card_bin', 'locale'])
    
    df['EVENT_LABEL'] = [0 if x == 'legit' else 1 for x in df['EVENT_LABEL']]
    
    
    # Changing missing values to default value in more columns that it is possible
    df['user_agent'] = df['user_agent'].fillna("Unknown")
    df['currency'] = df['currency'].fillna("UNK")
    df['signature_image'] = df['signature_image'].fillna("UN")
    df['transaction_type'] = df['transaction_type'].fillna("UN")
    df['transaction_env'] = df['transaction_env'].fillna("UN")
    df['tranaction_initiate'] = df['tranaction_initiate'].fillna("UN")
    
    # Removing the rest of missing values
    df = df.dropna()
    
    # Creating new columns indicating browser and system that the transaction was made from
    df['browser']=df['user_agent'].str.split('/').str[0]
    df['os']=df['user_agent'].str.split('/').str[1].str.split('(').str[1]
    df['os'] = df['os'].astype(str)
    
    df['os_test'] = df.apply(os_selection, axis=1)
    df = df.drop(columns=['os','user_agent'])
    df.rename(columns={'os_test':'os'}, inplace=True)
    
    # Transition into categorical variables
    df['acc_age'] = pd.cut(x=df['account_age_days'], 
                       bins = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9200],
                       labels=['1', '2', '3', '4', '5', '6', '7', '8', '9']).astype('object')
    df['d_last_logon'] = pd.cut(x=df['days_since_last_logon'],
                            bins=[0, 20, 40, 60, 80, 100],
                            labels=['1', '2', '3', '4', '5'],
                            include_lowest=True).astype('object')
    df = df.drop(columns=['account_age_days', 'days_since_last_logon'])
   
    df = df[df['historic_velocity'] <= 9000]
   
    return df

