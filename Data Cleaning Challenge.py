"""
Data Cleaning Challenge

    The dataset is a .csv file containing so many
        tables within, ALL having the same 'column names'
        (and the same overall structure).

    This type of dataset can occur when we have so many
        teams collecting data under the same variables.

        At the end, each team submits their table.

        Then someone copies all tables from all excel
        spreadsheets and pastes them vertically, in the
        same excel spreadsheet, then saves the data as a
        .csv file

        (or someone just uses python to concatenate
        all of the tables into one .csv file?)

    The CHALLENGE:

    Your job is to clean the file, such that you get rid
        of ALL the repeated COLUMN HEADERS, then unify
        all of the data into a SINGLE TABLE with ONLY
        ONE row of column names: The first row of the data.


"""
import pandas as pd

"""
1. Load the dataset
"""
path = "file path/data_cleaning_challenge.csv"
data_import = pd.read_csv(path)


"""
2. See data details
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


# data_details(data_import)


"""
3. Let us drop 'Unnamed: 9' and 'Unnamed: 10' columns, since
    they have no data.
    
    Please note that since we are storing the result of the 
        operation under a different DataFrame name, we DO NOT
        have to use the 'inplace=True' attribute/parameter.
        
    PLEASE note that it is important to create a new variable
        a new variable evry time you want to make a change in 
        the dataframe.
        This is because you may want to ROLLBACK to an earlier 
        state of the dataframe if you later discover that you 
        made a mistake earlier on.
        
        
"""
drop_extra = data_import.drop(columns=["Unnamed: 9",
                                       "Unnamed: 10"])
# data_details(drop_extra)


"""
4. Add an extra column AT THE END of the columns

    We intend to use this extra column to give the same 
        number to all rows in a given table, within
        the dataset. 
        
        For example, all the rows of data in the first 
            table of the dataset would have a '1' at the
            end, all rows of data in the second table of
            the dataset would have a '2' at the end, etc.
        
"""
# Firstly, we have to remove all NaN values for the 'Row Type'
# column, since they are not iterable.
# https://pandas.pydata.org/docs/reference/api/pandas.notna.html

drop_NaNs = drop_extra[drop_extra['Row Type'].notna()]
# data_details(drop_NaNs)


# Next, we create an empty list
# (which we would finally use as our column to be inserted)
column_values = []

# next, we create a 'counter' variable
counter = 0

# create our 'for' loop
for i in drop_NaNs['Row Type']:

    # the ABOVE 'for loop' statement is going to iterate
    # over all the values in the 'Row Type' Column.

    # We then write an 'if' statement, targeting every
    # time we encounter 'first name'.
    # We do this because 'first name' belongs to every
    # row in the 'Row Type' column which contains column
    # names for each table in the dataset.

    if 'first name' in i:
        counter += 1

    column_values.append(counter)


# print(column_values)


# Finally, we add the 'column_values' table to our dataset
# Unrelated note: Changing cursor size in pycharm:
# https://stackoverflow.com/questions/34988774/how-to-change-pycharm-5-0-1-cursor

iter_cols = drop_NaNs
iter_cols[
    'Iterations'] = column_values   # create new col and add data

# data_details(iter_cols)


"""
5. Remove all extra column names from the dataset

    So we would remove all the rows in the dataset which are
        repeats of the first row of the dataset: 
        
        These rows are repeats of the column names.
"""
# You will now create a dataframe which contains all rows
# which do not have 'Row Type', hence eliminating all
# repeats of column names.
# (except the first row, which you used for the elimination process).
# Wow!
drop_extra_Column_Name_rows = iter_cols[
    iter_cols['Row Type'] != 'Row Type']

# data_details(drop_extra_Column_Name_rows)


"""
6. Remove {Retain} all repeats of the 'first name:' rows 

        This 'first name:' type of row appears in all tables 
            throughout the dataset. 
            So they all need to go  {BE KEPT}.
"""
name_dataframe = drop_extra_Column_Name_rows[
    drop_extra_Column_Name_rows[
        'Row Type'].str.contains('first name')
]

# data_details(name_dataframe)


"""
7. When we look at the data details for the 'name_dataframe'
    DataFrame, we notice that the columns:
    
    'Speed1', 'Speed2', 'Electricity',
       'Effort', 'Weight', 'Torque'
       
       are all empty.
       
       So we drop them.
       
"""

name_dataframe.drop(columns=['Speed1', 'Speed2',
                             'Electricity', 'Effort',
                             'Weight', 'Torque'],
                    inplace=True)

# data_details(name_dataframe)


"""
8. We now rename the columns
"""
name_dataframe.rename(columns={"Row Type": "First Name",
                               "Iter Number": "Last Name",
                               "Power1": "Date"},
                      inplace=True)

# data_details(name_dataframe)


"""
9. When we look at the data details for the 'name_dataframe'
    DataFrame once again, we notice that when we look at the 
    rows, we see:
    'first name: ', 'last name:', 'date: ' before each row 
    value.
    
    We do not want this. 
    
    The COLUMN NAMES already describe what the values in the 
        rows are.
        
    Let's remove them:
    
"""

# we strip the first 12 characters (including empty space)
# from every value in the 'First Name' column.
# Note that these first 12 characters are 'first name: '

name_dataframe['First Name'] = name_dataframe[
    'First Name'].str[12:]

# we do same for the 'Last name' column:

name_dataframe['Last Name'] = name_dataframe[
    'Last Name'].str[11:]

# we do the same for the 'Date: ' column:

name_dataframe['Date'] = name_dataframe[
    'Date'].str[6:]


# data_details(name_dataframe)


"""
10. We now create a DataFrame which does not contain the names:
        a 'no name' dataframe.
        
        To do this, we would use a previous dataframe.
        
        This is why as you progress, it is better to store 
            changes in new dataframe names, so that you
            can easily roll back to a previous state of the 
            dataframe
            
        *** Please note that in the code below, we have used the 
                INVERSE OPERATOR in pandas 
                (notice the minus (-) sign in the snippet below).
                
                This operator returns the EXACT OPPOSITE rows
                which were returned using the snippet in
                ~~~ lines 182-185
                
        Read more on inverse operators:
        
            (look for a link)
            
        NOTE: 
                An easy way to split data using two conditions is 
                to WRITE ONE CONDITION, THEN INVERSE IT TO CREATE
                THE OTHER CONDITION
         
"""
no_name_dataframe = drop_extra_Column_Name_rows[
    -drop_extra_Column_Name_rows[
        'Row Type'].str.contains(
        'first name')]

# data_details(no_name_dataframe)


"""
11. We now merge the data
        
        Read more on pd.merge:
        
        https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html
        
"""
cleaned_data = pd.merge(
    left=name_dataframe,
    right=no_name_dataframe,
    how='inner',
    on='Iterations'
)


# data_details(cleaned_data)


"""
You can now save the data into a .csv file or into a MySQL
            database.
"""
