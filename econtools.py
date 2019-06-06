import pandas as pd
import numpy as np

def raw_to_df(raw_data_split, column_names):
    """Converts raw data into a pandas dataframe
        • 'raw_data_split' is a list of raw data that has been split on whitespace
        • 'column_names' is a list of column names that you wish to be in the dataframe"""
    
    df = pd.DataFrame()
    for i in range(len(column_names)):
        df[column_names[i]] = [float(raw_data_split[j]) for j in range(i,len(raw_data_split), len(column_names))]
    for name in df.columns:
        if name == 'year':
            df[name] = df[name].astype('int')
    return df