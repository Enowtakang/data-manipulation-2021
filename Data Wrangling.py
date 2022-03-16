"""
Data Wrangling in Python

    Most of the time, the data which they provide for
        you to work with, is not usable in a machine
        learning project, if good results are awaited.

    In this tutorial, we would learn most of the data
        wrangling techniques.


    Here is the link to the course script:

        https://github.com/AkumaEX/Cognitive-Class/blob/master/DA0101EN%20Data%20Analysis%20with%20Python/DA0101EN-Review-Data-Wrangling.ipynb

"""

import pandas as pd
import matplotlib.pylab as plt
import numpy as np

"""
1. Load the data
"""
fileName = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(fileName)


"""
2. Data Details
"""


def data_details(name_of_dataframe):
    print('     Dataset Columns: ')
    print('')
    print(name_of_dataframe.columns)
    print('')

    print('     First Five Rows: ')
    print('')
    print(name_of_dataframe.head())
    print('')

    print('     Last Five Rows: ')
    print('')
    print(name_of_dataframe.tail())      # to see how many rows we have
    print('')

    print('     Total Information about the dataset: ')
    print('')
    print(name_of_dataframe.info())    # understand our data
    print('')

    print('     Description of the dataset: ')
    print('')
    print(name_of_dataframe.describe())
    print('')


# data_details(df)


"""
3. Provide column names. 

        We can see that the dataset has no column names.
        
        In many cases, we may receive datasets which do not
            even have column names. 
            
        We have to speak with the clients, then get the column 
            names.
            
"""
headers = ["symboling", "normalized-losses", "make",
           "fuel-type",
           "aspiration", "num-of-doors", "body-style",
           "drive-wheels",
           "engine-location", "wheel-base", "length",
           "width",
           "height", "curb-weight", "engine-type",
           "num-of-cylinders",
           "engine-size", "fuel-system", "bore",
           "stroke",
           "compression-ratio", "horsepower", "peak-rpm",
           "city-mpg",
           "highway-mpg", "price"]


"""
4. Now, we add the headers to the dataframe
"""

df_2 = pd.read_csv(fileName, names=headers)
# data_details(df_2)


"""
5. Replace '?'s with 'NaN's

        When we look at df_2, we see that some columns
            have issues with the data in them.
            
            For example, the 'normalized loses' column
            has  question marks(?) instead of integer values.
            
            It is good that we replace these question marks 
            with NaN, so that we can easily handle the 
            NaNs.
            
            
            The snippet below replaces all '?'s found ANYWHERE 
            in the dataset with 'NaN's.
            
            Please note that if we did not create df_3, we would 
            have added the 'inplace=True' snippet in order to 
            commit the changes to df_2.
            
            Also, we can use this method to replace so many 
            different digits/symbols in the same dataset.
"""

df_3 = df_2.replace('?', np.nan)
# data_details(df_3)


"""
6. We now see all the missing values in a different 
        dataframe.
        
        The snippet below tells us weather or not the value
            at that position is null, i.e., a 'NaN'.
"""
missing_values = df_3.isnull()
# data_details(missing_values)


"""
7. We now want to see the 'frequency' of each VALUE in each
        COLUMN.
"""


def column_value_frequency(dataframe):
    for column in dataframe.columns.values.tolist():
        print(column)
        print(dataframe[column].value_counts())
        print("")


# column_value_frequency(df_3)


"""
8. Check the number of non-null values in each COLUMN
"""


def check_missing_values(dataframe):
    global check_missing
    check_missing = dataframe.isnull()

    for column in check_missing.columns.values.tolist():
        print(column)
        print(check_missing[column].value_counts())


# check_missing_values(df_3)
