import pandas as pd
import numpy as numpy

def acquire_df():
    df = pd.read_csv('nyc-rolling-sales.csv')
    return df

def prep_df():
    df = acquire_df()
    df.drop(df.columns[0], axis=1, inplace=True)
    return df