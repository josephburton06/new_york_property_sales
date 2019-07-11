import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

def create_enc(df, columns):
    '''
    The following will create encoded columns based on a list of columns as an argument. The original column
    will stay intact.  Ex: create_enc(df, ['sport', 'nationality'])
    '''
    for col in columns:
        df[col+'_enc'] = df[col]
        encoder = LabelEncoder()
        encoder.fit(df[col])
        df[col+'_enc'] = encoder.transform(df[col])
    return df

def remove_outlier_column(df, groupby_column, outlier_column):
    '''
    This function will remove outliers by grouping on unique values in a column identified (groupby_column).
    The outlier_column is used to identify the column to be evalated for outliers.
    If you use, for example, good_df and run it through once, you keep using the same good_df so each time
    that this function runs, it will already have the previously removed outliers still removed.
    Using a second df will capture observations that were removed.
    Ex: df_good, df_rem = remove_outlier_column(df, 'sex', 'height')
    '''
    uniques = list(sorted(df[groupby_column].unique()))
    
    removed_df = pd.DataFrame()
    final_df = pd.DataFrame()
    
    for unique in uniques:
        df_grouped_1 = df[df[groupby_column] == unique]
        df_grouped_2 = df[df[groupby_column] == unique]
        
        q1 = df[outlier_column].quantile(0.25)
        q3 = df[outlier_column].quantile(0.75)
    
        iqr = q3-q1
        fence_low = q1-1.5*iqr
        fence_high = q3+1.5*iqr
        
        df_rem = df_grouped_1.loc[(df_grouped_1[outlier_column] < fence_low) | (df_grouped_1[outlier_column] > fence_high)]
        removed_df = removed_df.append(df_rem)
        
        df_out = df_grouped_2.loc[(df_grouped_2[outlier_column] > fence_low) & (df_grouped_2[outlier_column] < fence_high)]
        final_df = final_df.append(df_out)
        
    return final_df, removed_df