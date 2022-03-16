"""
PyData DC 2018: Cleaning data with pandas

"""

import pandas as pd

"""
1. Load Data
        
        By default, the .read_csv function in pandas reads all
            files, interpreting each coma (,) as a value
            separator.
        
        Since the data is NOT separated by comas, we added
            the < sep='\t' > snippet in the .read_csv 
            function in order to specify the type of 
            separation mark (tabs) 
"""

path = "C:/Users/HP/PycharmProjects/MachineLearningEnow/Py_Data_DC_2018/pydatadc_2018-tidy-master/data/gapminder.tsv"
df = pd.read_csv(path, sep='\t')


"""
2. Get data details
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
3. Parts of a DataFrame

            A dataframe has 3 parts:
                a.  Columns : Here, we can see all the column
                    names.
                b. Index: The numbers which come BEFORE each row.
                    Those numbers are unique identifiers of the 
                    rows.
                c. Body: The actual data in the dataframe.
                
            
            For those working with TIME-SERIES data, they
                may prefer to SET the DATE-and-TIME as the 
                INDEX, so that they can access data for any 
                date-time.
"""


"""
4. type() function

        Sometimes, you may be working with pandas, and you
            get a wierd error.
            The type() function could be used to let you know 
            if you are really working with the object type
            (e.g. dataframe) which you think you are working 
            with.
"""


def type_of_data_or_structure(item):
    print(type(item))


# type_of_data_or_structure(df)


"""
5. How to subset columns with pandas

        Remember that you can save the subset to 
        a new file type (.csv, .xlsx, .json, .html, etc.)

"""
# 5.1 To subset a single column, do this:

country_df = df['country']
# print(country_df)
# print(country_df.head())


# 5.2 To subset multiple columns, do this:

subset_col = df[['country', 'continent', 'year']]
# print(subset_col.head())


"""
6. How to subset rows in pandas

        There are three (03) ways to subset rows in pandas:
            - one of them is depricated.
            - the other one is not advised
            - so you should ONLY really work with 1 of them
"""

"""
6.1 Use '.loc'
        
        loc is used for LABEL BASED INDEXING

        loc  - this means location.
            So if you are looking for the row with index 2
            in the dataset (i.e, the row labelled 2), 
            you use loc.
            
        Note - this method is sometimes problematic
            because when you concatenate dataframes, 
            2 rows, each from a different previous dataframe 
            (before concatenation) may have the same index  
            label (index duplication). 
            This method may then return two indices instead of 
            one.           
"""
# print(df.loc[2])


"""
6.2 How to subset multiple rows with .loc method
    
        Remember that if after concatenation, 2 rows
            retain the index label 2, both rows may 
            be returned.
"""
# print(df.loc[[2, 0]])


"""
6.3 The '.iloc' method
    
    iloc is used for POSITIONAL BASED INDEXING

    iloc - this means index location

    In the '.loc' method, we saw that it returns the row(s)
        which are labeled with the index number being 
        researched.
        
    In the '.iloc' method, we actually get the row in the 
        'i'th index location, irrespective of the index 
        number with which it is labelled.
        
        For example, if "after concatenation" we see that in 
            the 10th index position there is a row with an 
            index label of 2, the .iloc[10] method would
            return this row, while we would have to get  
            this same row with the .loc[2] method.
    
"""
# print(df.iloc[2])


"""
6.4 The .ix method

    This is depricated.
    
    It would not work.
"""
# print(df.ix[2])


"""
7. How to subset both row and columns in pandas

        i.e., creating a subset of the original dataframe.
        
        Let us write code which collects 'all of the rows' 
        for 'two columns' - year and pop.
"""
subset_df = df.loc[:, ['year', 'pop']]
# print(subset_df.head())


"""
7.1 Filtering rows

        Please note:
            you can always save the results of your
            filter in a new file type. 
            (.csv, .xlsx, .json, .html, etc.)

        Imagine that we wanted to retain all the 
        ROWS which contained the year '1967' for:
        
"""

# 7.1.1 All the columns

subset_df_2 = df.loc[df['year'] == 1967, :]
# print(subset_df_2.head())


# 7.1.2 The YEAR and POP columns

subset_df_3 = df.loc[df['year'] == 1967, ['year', 'pop']]
# print(subset_df_3.head())


"""
7.2 Multiple conditions for row filtering.

    7.2.1 Imagine that we want all rows containing the
            year 1967 'AND' where the population was more than
            one million (for the YEAR and POP columns)
"""
subset_df_4 = df.loc[

    (df['year'] == 1967)
    &
    (df['pop'] > 1_000_000),

    ['year', 'pop']
]

# print(subset_df_4.head())


"""
7.2.2 Imagine that we want all rows containing the
            year 1967 'OR' the population was more than
            one million (for the YEAR and POP columns)
"""
subset_df_5 = df.loc[

    (df['year'] == 1967)
    |
    (df['pop'] > 1_000_000),

    ['year', 'pop']
]

# print(subset_df_5.head())


"""
NOW, WE ARE DONE WITH THE INTRO
        
        25:13
"""


"""
We now move to part 2: 

    Tidying the dataset
"""










































































