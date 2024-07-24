import seaborn as sns
from matplotlib.pylab import plt
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 2)
# read dataset
df = pd.read_csv("./data/coaster_db.csv")

#understand the dataset

#get shape row/column
print(df.shape)

# get columns
print(df.columns)

# find datatypes
print(df.dtypes)

# describe data
print(df.describe())

# get columns info
print(df.info())
