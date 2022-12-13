import pandas as pd
from sklearn.model_selection import train_test_split


def pre_processing(df):
    df=df.drop(columns=['DT','A1', 'A2', 'A3', 'n_obs_used', 'per_y','condition_code', 'ad'])
    df['tp_cal']=df['tp_cal'].str.split(pat='.').str[0]
    df['tp_cal']=df['tp_cal'].str.split(pat='-').str[0]
    df=df.drop(index=[0,1])
    df['tp_cal'] = df['tp_cal'].astype('int')
    df = pd.get_dummies(df, columns = ['two_body'], drop_first=False)
    df = df.set_index('full_name')
    df.rename({'class': 'orbit'}, axis=1, inplace=True)
    return df

###################################################################################
                                    #SPLIT DATA#
###################################################################################

def split_data(df):
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=1989)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=1989)
    return train, validate, test

#############################################   SECONDARY SPLIT

def final_split(df, target):
    train_X, validate_X, test_X = split_data(df)
    
    #remember that for this project the target is orbit
    train_y = train_X[target]
    validate_y = validate_X[target]
    test_y = test_X[target]
    
    #code to remove 'target' as a column
    train_X.drop(columns = target, inplace = True)
    validate_X.drop(columns = target, inplace = True)
    test_X.drop(columns = target, inplace = True)
    
    return train_X, validate_X, test_X, train_y, validate_y, test_y    
    

