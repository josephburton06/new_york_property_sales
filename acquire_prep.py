import pandas as pd
import numpy as numpy

def acquire_df():
    df = pd.read_csv('nyc-rolling-sales.csv')
    return df

def prep_df():
    '''
    There is a column similar to an index that starts at 4.  It's in the 0th position. It has no purpose
    and we'll drop it.
    '''
    df = acquire_df()
    df.drop(df.columns[0], axis=1, inplace=True)
    return df