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

        """
        df = DataUnderstanding.load_data('./data/coaster_db.csv')
        # columns that make sense to keep at this moment
        columns_to_keep = ['year_introduced','coaster_name', 'Manufacturer', 'speed_mph', 'height_ft', 'Inversions_clean', 'Gforce_clean', 'opening_date_clean']
        # filter columns
        df = df.filter(items=columns_to_keep)
        # date set as object but it is datetime, so change it
        df['opening_date_clean'] = pd.to_datetime(df['opening_date_clean'])

        # Rename columns
        df = df.rename(columns={'coaster_name': 'Coaster_Name',
                                'year_introduced': 'Year_Introduced',
                                'opening_date_clean': 'Opening_Date',
                                'speed_mph': 'Speed_mph',
                                'height_ft': 'Height_ft',
                                'Inversions_clean': 'Inversions',
                                'Gforce_clean': 'Gforce'})


