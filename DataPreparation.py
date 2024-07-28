import seaborn as sns
from matplotlib.pylab import plt
import numpy as np
import pandas as pd
from DataUnderstanding import DataUnderstanding



# start preprocessing
class DataPreparation:
    """
    Class to handle data preprocessing tasks, such as NaN values.
    """

    def clean_colums(self):
        """
        Save only neccessary columns, remove others

        clean dataset, handle nan values, keep interesting things.

        This is not dynamic class, because I will work only on this dataset.
        this is reason why i dont pass directory to load data

        """
        df = DataUnderstanding.load_data('./data/coaster_db.csv')
        # columns that make sense to keep at this moment
        columns_to_keep = ['Location', 'year_introduced','coaster_name', 'Manufacturer', 'speed_mph', 'height_ft', 'Inversions_clean', 'Gforce_clean', 'opening_date_clean']
        # filter columns
        df = df.filter(items=columns_to_keep)
        # date set as object but it is datetime, so change it

        # Rename columns
        df = df.rename(columns={'coaster_name': 'Coaster_Name',
                                'year_introduced': 'Year_Introduced',
                                'opening_date_clean': 'Opening_Date',
                                'speed_mph': 'Speed_mph',
                                'height_ft': 'Height_ft',
                                'Inversions_clean': 'Inversions',
                                'Gforce_clean': 'Gforce'}) # modify original without copy
        df['Opening_Date'] = pd.to_datetime(df['Opening_Date'])
        # identify missing values
      #  print(df.isna().sum())

        # check if there is duplicate in coaster names

       # print(df.query('Coaster_Name == "Crystal Beach Cyclone"'))
        #The code identifies duplicates in df based on the columns
        # 'Coaster_Name', 'Location', and 'Opening_Date' and removes if there is duplicates
        df = df.loc[~df.duplicated(subset=['Coaster_Name', 'Location', 'Opening_Date'])] .reset_index(drop=True).copy()
        # print(df.head())
        # print(df.shape)

        return df



dp = DataPreparation()
dp.clean_colums()

