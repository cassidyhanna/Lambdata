import pandas as pd
import numpy as np

from pandas import DataFrame

def null_count(df):
    null_values = df.isnull().sum
    return null_values

if __name__ == "__main__":
    df = pd.DataFrame(np.random.rand(10,6))
    # Make a few areas have NaN values
    df.iloc[1:3,1] = np.nan
    df.iloc[5,3] = np.nan
    df.iloc[7:9,5] = np.nan
