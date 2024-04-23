# Fraud Detection Project
# IN-PROGRESS
### Absract
This project was done to find the most robust model in detection of fraud transactions. The analyzed models were: logistic regression, random forest classifier, xgb, and lgbm. The best results yield random forest classifier.
![Results](img/pr_result.png)

### Goal
Detect, if the transaction is fraud or not. The main assumption is that the the most important is to get as low number of false negatives (fraud transactions classified as legit) as possible. The sub-goal is to describe most common traits of fraud transaction.

### Project structure
1. data - contains raw data and partitioned, preprocessed datasets.
2. functions - python scripts with functions imported to notebooks, functinos used to preprocessing and model evaluation
3. img - exported graphs
4. models - trained models
Notebooks contains EDA, model training, cross-validation and evaluation.

### Data
Data comes from [Kaggle](https://www.kaggle.com/datasets/ban7002/fraud-challenge-data). It's a dataset containing 26 variables and 150 000 fictional observations.
Variables:
1. **account_age_days**: The age of the account in days. 
2. **transaction_amt**: The amount of money involved in the transaction.
3. **transaction_adj_amt**: Manipulation fees, currency exchange etc.
4. **historic_velocity**: Scoring according to the frequency of transactions.
5. **ip_address**: The IP address associated with the transaction
6. **user_agent**: Information about the web browser or device used for the transaction.
7. **email_domain**: The domain part of the email address used for the account.
8. **phone_number**: The phone number associated with the account.
9. **billing_city**: The city associated with the billing address.
10. **billing_postal**: The postal code associated with the billing address.
11. **billing_state**: The state or region associated with the billing address.
12. **card_bin**: The Bank Identification Number (BIN) of the credit card used in the transaction.
13. **currency**: The currency used for the transaction.
14. **cvv**: Card Verification Value, a security feature typically found on the back of a credit card.
15. **signature_image**: A signature image associated with the transaction.
16. **transaction_type**: The type of transaction, e.g., purchase, refund, withdrawal.
17. **transaction_env**: The environment in which the transaction occurred, such as online or in-store.
18. **EVENT_TIMESTAMP**: The timestamp of the transaction.
19. **applicant_name**: The name of the account holder or applicant.
20. **billing_address**: The billing address associated with the account.
21. **merchant_id**: The identifier for the merchant where the transaction took place.
22. **locale**: Region settings associated with transaction.
23. **transaction_initiate**: Information about how the transaction was initiated, e.g., online, phone, in-person.
24. **days_since_last_logon**: Number of days since the last login or activity on the account.
25. **inital_amount**: The initial amount associated with the account.
26. **EVENT_LABEL**: The label or classification of the event, often used in supervised learning for fraud detection.

### Description
[exploration.ipynb, functions]
Cleaning of data consisted of outlier deletion based on IQR, and filling in missing values with new class value or deletion. The distributions of variables were explored. Extraction of features was done on date and user agent. VIF was calcualted to check for multicollinearity.

[log_reg.ipynb, random_forest.ipynb, xgboost.ipynb, lgbm.ipynb, functions]
Preprocessing step consisted of numerical variables scaling (StandardScaler()) and categorical variables encoding (OneHotEncoder()). Due to imbalance in target variable, dataset before fitting model were undersampled (RandomUnderSampler) or oversampled (SMOTE).  
Logistic regression, random forest classiffier, xgb and lgbm models were built on under- and oversampled data and cross-validated using GridSearchCV with hyperparameter tuning.*

[evaluation.ipynb, functions]
During the evaluation stage each model was evaluated separetely and compared at the end. The metrics are:
1. ROC
2. Precision-recall curve
3. KS statistic
4. Confussion matrix
5. Missclassification rate
6. Recall - main metric
7. Precision
8. F1 score
9. Accuraccy
10. Coefficients and feature importance in each model

### Conclusion



\* amount of folds and parameters options reduced due to hardware limitations.
### Requirments
Needed packages are listed in requirments.txt file. To visualize '.dot' files [GraphViz] (https://dreampuf.github.io/GraphvizOnline) can be used.
