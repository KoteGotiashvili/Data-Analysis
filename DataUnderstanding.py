import seaborn as sns
from matplotlib.pylab import plt
import numpy as np
import pandas as pd

def load_data(csv_source):
    # display more columns
    pd.set_option('display.max_columns', 20)
    # read dataset
    df = pd.read_csv(csv_source)

    return df

def understand_basics(df):
    # understand the dataset

    # get shape row/column
    print(df.shape)

    # get columns
    print(df.columns)

    # find datatypes
    print(df.dtypes)

    # describe data
    print(df.describe())

    # get columns info
    print(df.info())

# get basic info about data
# understand_basics(load_data('./data/coaster_db.csv'))

