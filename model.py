import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import sklearn.preprocessing as pre
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, plot_confusion_matrix, ConfusionMatrixDisplay

import prepare as p



##################################################################
################          SCALED DATA        #####################


def Scaled_Data(train_X, validate_X, test_X):
    scaler = pre.StandardScaler()

    scaler.fit(train_X)

    train_scaled = scaler.transform(train_X)
    validate_scaled = scaler.transform(validate_X)
    test_scaled = scaler.transform(test_X)
   
    # here i put the arrays into dataframes
    train_scaled = pd.DataFrame(train_scaled)
    validate_scaled = pd.DataFrame(validate_scaled)
    test_scaled = pd.DataFrame(test_scaled)
    
    #here I give the new data frames columns names
    train_scaled = pd.DataFrame(data = train_scaled.values, columns = train_X.columns)
    validate_scaled = pd.DataFrame(data = validate_scaled.values, columns = validate_X.columns)
    test_scaled = pd.DataFrame(data = test_scaled.values, columns = test_X.columns)

    return train_scaled, validate_scaled, test_scaled

##################################################################
################         DECISION TREE       #####################

def decision_tree(train_X, validate_X, train_y, validate_y):
    clf = DecisionTreeClassifier(max_depth = 5, random_state = 1989)
    clf = clf.fit(train_X, train_y)
    
    in_sample_accuracy = clf.score(train_X, train_y)
    out_of_sample_accuracy = clf.score(validate_X, validate_y)
    
    # print result
    return in_sample_accuracy, out_of_sample_accuracy
    
##################################################################
################         RANDOM FOREST       #####################    
    
def random_forest(train_X, validate_X, train_y, validate_y):
    rf = RandomForestClassifier(max_depth = 3, random_state = 1989)
    rf = rf.fit(train_X, train_y)
    
    in_sample_accuracy = rf.score(train_X, train_y)
    out_of_sample_accuracy = rf.score(validate_X, validate_y)
    
    # print result
    return in_sample_accuracy, out_of_sample_accuracy

##################################################################
################     LOGISTIC REGRESSION    #####################    
    
    
def log_reg(train_X, validate_X, train_y, validate_y):
    '''get logistic regression accuracy on train and validate data'''

    # create model object and fit it to the training data
    logit = LogisticRegression(solver='liblinear')
    logit.fit(train_X, train_y)

    in_sample_accuracy = logit.score(train_X, train_y)
    out_of_sample_accuracy = logit.score(validate_X, validate_y)
    
    # print result
    return in_sample_accuracy, out_of_sample_accuracy
    
##################################################################
################             KNN             #####################  
def KNN(train_X, validate_X, train_y, validate_y):
    knn = KNeighborsClassifier(n_neighbors=5, weights='uniform')
    knn = knn.fit(train_X, train_y)
    
    in_sample_accuracy = knn.score(train_X, train_y)
    out_of_sample_accuracy = knn.score(validate_X, validate_y)
    
    # print result
    return in_sample_accuracy, out_of_sample_accuracy
    
##################################################################
################      CONCISE DATA FRAME    #####################    

def make_metric_df(in_sample_accuracy, out_of_sample_accuracy, metric_df, model_name):
    '''
    Takes in in_sample_accuracy, out_of_sample_accuracy, acc_diff, and a df
    returns a df of accuracy score for the model on train and validate
    and difference between the two
    '''
    if metric_df.size ==0:
        metric_df = pd.DataFrame(data=[
            {
                'Model': model_name,
                'Train Accuracy': in_sample_accuracy,
                'Validate Accuracy': out_of_sample_accuracy
            }])
        return metric_df
    else:
        return metric_df.append(
            {
                'Model': model_name,
                'Train Accuracy': in_sample_accuracy,
                'Validate Accuracy': out_of_sample_accuracy
            }, ignore_index=True)

def model_results(train_X, validate_X, train_y, validate_y):
    
    metric_df = pd.DataFrame()
    
    #KNN
    in_sample_accuracy, out_of_sample_accuracy = KNN(train_X, validate_X, train_y, validate_y)
    metric_df = make_metric_df(in_sample_accuracy, out_of_sample_accuracy, metric_df, 'KNN')
    
    #Log Reg
    in_sample_accuracy, out_of_sample_accuracy = log_reg(train_X, validate_X, train_y, validate_y)
    metric_df = make_metric_df(in_sample_accuracy, out_of_sample_accuracy, metric_df, 'Logistic Regression')
    
    # Decision Tree
    in_sample_accuracy, out_of_sample_accuracy = decision_tree(train_X, validate_X, train_y, validate_y)
    metric_df = make_metric_df(in_sample_accuracy, out_of_sample_accuracy, metric_df, 'Decision Tree')
    
    # Random Forest
    in_sample_accuracy, out_of_sample_accuracy = random_forest(train_X, validate_X, train_y, validate_y)
    metric_df = make_metric_df(in_sample_accuracy, out_of_sample_accuracy, metric_df, 'Random Forest')
    
    return metric_df
    
    
##################################################################
################         MODEL FOR TEST      ##################### 
     
def test_model(test_scaled, test_y):
    rf = RandomForestClassifier(max_depth = 3, random_state = 1989)
    rf = rf.fit(test_scaled, test_y)

    # print result
    print(f"Accuracy of Random Forest on train is {rf.score(test_scaled, test_y)}")
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    