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
    Convert sale_price, land_square_feet, into numeric values.

    There are hyphens in sale_price.  They will be dropped.  These are most likely properties that
    are gifted.  First, whitespace is dropped, then rows with just hyphens are dropped.
    '''
    df.sale_price = df.sale_price.str.replace(' ', '')
    df = df[df.sale_price != '-']
    df.sale_price = pd.to_numeric(df.sale_price, downcast='integer')

    '''
    There are numerous observations with sale prices under $1,000.  Again, these may have been properties
    that were gifted or sold at a very low amount.  This do not seem accurate for real world predictions.  
    They will be dropped as well.
    '''

    df = df[df.sale_price > 1000]

    '''
    We still have many observations with a '-' in gross square feet.  Instead of dropping these all.  We'll
    separate them into another dataframe so they can be modeled without this feature.
    '''

    df.gross_square_feet = df.gross_square_feet.str.replace(' ', '')
    no_sqft_df = df[df.gross_square_feet == '-']

    '''
    Now, we will remove those observations witout gross square feet from the original dataframe
    '''

    df = df[df.gross_square_feet != '-']

    return df, no_sqft_df