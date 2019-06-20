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

    '''
    Below, we lowercase all column headers and replace spaces and hyphens with underscores.
    '''
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    df.columns = df.columns.str.replace('-', '_')

    '''
    There are hyphens in sale_price.  They will be dropped.  These are most likely properties that
    are gifted.  First, whitespace is dropped, then rows with just hyphens are dropped.
    '''
    df.sale_price = df.sale_price.str.replace(' ', '')
    df = df[df.sale_price != '-']

    return df