from env import get_db_url
import pandas as pd
import numpy as np
import os

def get_comet_data():
    if os.path.exists('sbdb_query_results.csv'):
        return pd.read_csv('sbdb_query_results.csv')
    #df = pd.read_csv('http://localhost:8888/edit/commet_class')
    df.to_csv('sbdb_query_results.csv', index=False)
    return df