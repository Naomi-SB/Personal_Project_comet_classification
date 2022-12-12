import pandas as pd
def pre_processing(df):
    df=df.drop(columns=['DT','A1', 'A2', 'A3', 'n_obs_used', 'per_y','condition_code', 'ad'], inplace = True)
    return df

def date_to_dt_index(df, dt_feature):
    '''This function takes in a df with a date column
    and converts date to a datetime object
    then sets that as the index'''
    df[dt_feature] = pd.to_datetime(df[dt_feature])
    df = df.set_index(dt_feature).sort_index()