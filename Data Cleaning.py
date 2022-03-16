"""
Data Cleaning in Python

    Below are some common issues with data:
        1. Reading the file
        2. Inconsistent column names (some upper case,
                                        some lower case).
        3. Missing values
        4. Different data types in the same column
        5. Duplicate rows
        etc
"""

import pandas as pd
import numpy as np


"""
1. Loading or reading the file

    An error experienced during the loading of a 
        file could be due to:
                    a. Encoding error
                    b. Inconsistent rows
"""

"""
1a. Encoding error
when we run the two lines of code below, we get an encoding error.
"""

path = "file path/unclean_data.csv"
# pd.read_csv(path)

"""
1a. Solution 1`

    We solve the problem by specifying an encoding
"""

df1 = pd.read_csv(path, encoding="latin1")
# print(df1.head())     # It worked

"""
1a. Solution 2

    If you doubleclick on the file (unclean_data.csv) 
        in order to  open it (in Pycharm), you discover 
        that it cannot open. 
    The file even has a question mark on it, as seen 
        when viewed in the PyCharm text editor.
        
    ----------------------------------------
    
    Try using these encodings, if 'latin1' encoding in 
        Solution 1 above does not work:
        
            1.  utf-8
            2. ISO-8859-1
            3. latin1 (I just listed it again. No qualms)
"""


"""
2. Inconsistent Column Names

    To deal with this issue, we have two options:
        1. We change the cases 
        2. We rename the columns
        
    Let us begin with the first solution:
        
        We change the cases to UPPER
"""
path2 = "file path/unclean_data1.csv"
df2 = pd.read_csv(path2)


"""
From the code below, we can see that the column names 
have both upper and lowercase characters
"""
# print(df2.columns)


"""
We change the cases to upper

        Please note that we can then save this 
        dataframe into a new '.csv' file after.
"""
df2.columns = df2.columns.str.upper()
# print(df2.columns)


"""
The second solution is to:
                            rename the columns.
    
    Suppose we want to rename the "DURATION" column
            to "TIME".
            
    Note this info from stackoverflow:
        ---------------   
        Use the df.rename() function and refer the 
        columns to be renamed. 
        Not all the columns have to be renamed:

        df = df.rename(columns={'oldName1': 'newName1', 
        'oldName2': 'newName2'})
        
        # Or rename the existing DataFrame 
        (rather than creating a copy): 
        
        df.rename(columns={'oldName1': 'newName1', 
        'oldName2': 'newName2'}, inplace=True)
        --------------- 
        
        https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas
        
        ---------------
        
        Please note that we can then save this 
        dataframe into a new '.csv' file after.
        
"""
# print(df2.columns)
df2.rename(columns={'DURATION': 'TIME'}, inplace=True)
# print(df2.columns)


"""
3. MISSING DATA

    We can handle missing data in different ways:
    
        1. add a default value for missing data,
            or use mean to fill it.
        2. Delete the row or column with missing data
        3. Interpolate the rows
        4. Replace
        
        
    3.1 We start by learning how to detect missing data.
    
        For this, we use the 'isnull()' function.
        
            This would give use the opportunity to 
                'see' weather or not there is missing 
                data in any position of our dataframe.
        
        'False' means there is NO missing data.
        
        'True' means there IS missing data.
"""
# print(df2.isnull())


"""
3.2 Knowing which columns contain missing data.
        
        Using the 'df2.isnull()' snippet gives you the
            whole dataframe. This is a problem because 
            with huge data, visual inspection ia a 
            nightmare.

        Inorder to know which column contains missing data,
            we use the following snippet:
                        print(df2.isnull().any())
        Remember:
            'False' means there is NO missing data.
            
            'True' means there IS missing data.
"""
# print(df2.isnull().any())


"""
3.3 Knowing if at all there are missing values in the dataset:

            print(df2.isnull().any().any())
                
        Remember:
            'False' means there is NO missing data.
            
            'True' means there IS missing data.
"""
# print(df2.isnull().any().any())


"""
3.4 Determining the total 'number of missing data' per
        column, in the dataframe.
"""
# print(df2.isnull().sum())


"""
3.5 Determining the total number of missing values in the
        entire dataframe.
"""
# print(df2.isnull().sum().sum())


"""
3.6 Add a 'default value' for the missing data
        Here, we would use zero.
        
        PLEASE PLEASE PLEASE: Note that, as we are 
            using a default value of zero, THIS 'MAY' 
            MAKE THINGS TO BE, SUCH THAT WE WOULD NO LONGER 
            BE ABLE TO DISTINGUISH BETWEEN 'ACTUAL ZEROS' AND
            'FILLED IN ZEROS'. 
            
        This is the case for any values which we choose to 
            use for 'filling' spaces with missing values.
            
        So this is a very risky option. VERY RISKY!!
"""
# df2.fillna(0, inplace=True)


"""
3.7 Fill missing values with the mean. (BETTER!!!!)

    ***     Please, this should be done after you
                have stripped away OUTLIERS.        ***
                
    Or else, you can fill with the MEDIAN or
                the MODE.
                
    You can use the MEDIAN when the data is CATEGORICAL!!
    
    You can use the MODE if the data is categorical ORDINAL!!
    
"""


"""3.7.1 Show the column values for the 'TIME' column"""
# print(df2['TIME'])

"""3.7.2 Calculate the mean of these column values"""
mean_time = df2['TIME'].mean()

"""
3.7.3 Fill the space with missing values in the TIME
        column with the 'mean_time' value
"""
# df2.TIME.fillna(mean_time, inplace=True)
# print(df2['TIME'])


"""
3.8 Delete the row or column with missing data

    This method drops any row which contains 
        as little as 1 missing value.
        
    Therefore, using this method could potentially 
        reduce your dataset to an unusably small scale.  
"""


def drop_rows_with_nan_values():
    """
    Please note that it is only when you call this function,
    that the  << df2.dropna(inplace=True) >> command
    would be permanent in the dataframe.

    This means that if you "comment out" this 'function CALL',
    the  << df2.dropna(inplace=True) >> command effect would be
    reversed
    """
    print(df2.shape)
    df2.dropna(inplace=True)
    print(df2.shape)


# drop_rows_with_nan_values()


"""
3.9 Dropping rows (with conditions).

        This is very important because if you use 'dropna',
            a row with a single missing value would 
            be dropped as well as a row with 30 missing 
            values. 
            And you know that these two rows are NOT equally
            damaged by missing values.
            
        So we need to create a function which would drop a row 
            which has missing values only if that row 'fulfills
            some predefined conditions'.
            
            
            
        For this, we use the 'thresh' attribute:
            df2.dropna(thresh=2, inplace=True)
            
        In the above snippet, we are dropping any
            row which has less than 2 values in it
        
        Please read all about the dropna() function
            in pandas from: 
            
            https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.DataFrame.dropna.html
            
        Note that you can also drop columns.
             df2.dropna(axis=1, inplace=True)
             
        Assignment:
            Learn how to drop duplicates
            
"""
