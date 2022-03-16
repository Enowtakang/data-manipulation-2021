"""
Tidying data

    For good information about tidying data and what tidy
        data really means, you need to read the article
        called
                    Tidy Data

        written by Hadley Wickham.

        The first three (03) sections are language agnostic,
        so you can read them.

        Notes:
            step 7 summarizes step 6 very very well!
            you must note point 8
"""

import pandas as pd


"""
1. Define our data details function
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


"""
2. Load our first dataset
"""

path = "C:/Users/HP/PycharmProjects/MachineLearningEnow/Py_Data_DC_2018/pydatadc_2018-tidy-master/data/pew.csv"
pew = pd.read_csv(path)

# data_details(pew)


"""
3. Melt Data
    
    When we look at the dataframe, we see that 'Religion'
        is unique and is located in one column.
        
        Income levels on the other hand are spread over 
            many columns, one for each income level.
            
        What we want at the end is just 3 columns, instead 
            of 11 columns: Religion, Income Level, Number.
            
            In this way, we can easily know 'the total number' 
            of people who share the same religion and are in
            the same income Level.
            
            So, for a given religion, we now have an income level 
            and a count.
            
            Read the paper on Tidy Data for more info:
            file:///C:/Users/HP/AppData/Local/Temp/tidy-data-1.pdf 
            
        Diagnostic:
        
            Long Data - This is data with many rows and much fewer
                columns.
            Wide Data - This is data with many columns and much 
                fewer rows.
                
            Many at times, we may have to melt Wide Data into Long
                Data, if some of the columns in the Wide Data are 
                RELATED, as it is in the 'pew' dataframe with 
                which we are working.
                
            So, before you melt data, you need to ask yourself:
            
                Are the columns in the dataset related?
                
                If yes (e.g. from a certain column number,
                each column afterward is a date, a salary, 
                etc), YOU NEED TO MELT THE DATA.              
"""
pew_long = pd.melt(pew, id_vars='religion')

# data_details(pew_long)


"""
4. We rename the 'variable' and 'value' columns in our 
        pew_long_data DataFrame.
        
        Please note that this could really be done in step 3 
            above. 
            See:
"""
pew_long_data = pd.melt(pew,
                        id_vars='religion',
                        var_name='income level',
                        value_name='count')

# data_details(pew_long_data)   # Done


"""
5. Another example which demonstrates the use of the 
    melting function when there is more than one column
    (variable) to be kept (in the 'id_vars=' parameter.
    
        We are using song billboard data for the year AD 2000.
        
        
        Please also note that the long form is the 
        preferred form for modelling and data storage 
        in databases.
        
"""
path_2 = "C:/Users/HP/PycharmProjects/MachineLearningEnow/Py_Data_DC_2018/pydatadc_2018-tidy-master/data/billboard.csv"
billboard = pd.read_csv(path_2)
# data_details(billboard)


"""
5.1 We melt the data
"""
billboard_melt = pd.melt(billboard,
                         id_vars=['year',
                                  'artist',
                                  'track',
                                  'time',
                                  'date.entered'
                                  ],
                         var_name='week',
                         value_name='rating'
                         )

# data_details(billboard_melt)


"""
6. What if we had a column which was storing more than one
    variable at a time?
    
    1. See the example column names below:
    
        m014 - males aged 0-14 years old
        f1020 -  females aged 10 - 20 years old
        
    2. See these other 4 examples:
    
        - cases_liberia
        - deaths_ liberia
        - cases_ghana
        - deaths_ghana
        
        Here, we may like to separate the data into 4 columns:
            - cases
            - deaths
            - countries
            - counts
            
            This is interestingly DIFFICULT, since column 
            names store demonstrate that they store multiple
            variables (cases, deaths, countries, counts) 
            at once.
            
        
        HOW DO WE GO ABOUT THIS?
"""


"""
6.1 We start by loading the dataset
"""

path_3 = "C:/Users/HP/PycharmProjects/MachineLearningEnow/Py_Data_DC_2018/pydatadc_2018-tidy-master/data/country_timeseries.csv"
ebola = pd.read_csv(path_3)
# data_details(ebola)


"""
6.2 We begin tidying by melting the dataset columns which all
        begin with either 'cases_' or 'deaths_', ignoring the
        countries that follow, at his phase of tidying.
"""
ebola_long = pd.melt(ebola,
                     id_vars=[
                         'Date',
                         'Day']
                     )

# data_details(ebola_long)


"""
6.3 We see at this point that the new 'variables'
    column has 3 bits of information:
    
        - cases,
        - deaths,
        - countries
        
    We could split the 'variable' column data into two, 
        separating out the countries, since every data 
        point in the column is of the form: xxxx_country.
"""

# 6.3.1 split the 'variables' column data into two,
# separating out the countries form the cases
# and deaths

variable_split = ebola_long['variable'].str.split('_')
# print(variable_split)


# 6.3.2 To isolate just the cases and deaths, we type:

c_d = variable_split.str[0]
# print(c_d)


# 6.3.3 To isolate the countries, we type:

countries_ebola = variable_split.str[1]
# print(countries_ebola)


"""
6.4 Add the status column (cases & deaths) and the 
        country column to the data.
"""

ebola_long['status'] = variable_split.str[0]
ebola_long['country'] = variable_split.str[1]

# data_details(ebola_long)


"""
7. There is a way to split the data and assign the parts 
    to newly created columns in the same dataframe:
"""

ebola_long[['status', 'country']] = ebola_long[
    'variable'].str.split('_', expand=True)

# data_details(ebola_long)


"""
8. Note that when your code is too long, you can break the 
    lines of code at the dot notations AFTER wrapping the code
    lines in extra curved brackets.
"""

ebola_long[['status', 'country']] = (ebola_long['variable']
                                     .str
                                     .split('_', expand=True))

# data_details(ebola_long)


"""
9. What happens when variables are stored in 
        both rows and columns?
        
        We have the weather dataset for this.
        Let us load it:
"""
path_4 = "C:/Users/HP/PycharmProjects/MachineLearningEnow/Py_Data_DC_2018/pydatadc_2018-tidy-master/data/weather.csv"
weather = pd.read_csv(path_4)
# data_details(weather)


"""
9.1 When we look at datasets in which two or more 
    rows are VERY SIMILAR, except for one or two data
    points, this is an indication that:
    VARIABLES ARE STORED IN BOTH ROWS AND COLUMNS,
    as seen in rows 2 & 3 of the weather dataset above:
    
    The 'element' column has tmax (row2) and tmin (row3)
        values at row 2 and 3, for EXAMPLE.
    
    But we really want the tmax and tmin values to be
        separate columns. 
        This is like the opposite of melting.
        We want to pivot back those tmax and tmin values, 
        to form columns of their own.
        
        So, we want a column called 'tmax' and a column
            called 'tmin'. 
             
            We do NOT want a column called 'element' which 
            has values called tmax and tmin.
            
            So how do we fix this?
        
        
        9.1:
            In this 9.1, we start by first melting the days
                columns.
                
"""
weather_melt = pd.melt(
    weather,
    id_vars=['id', 'year', 'month', 'element'],
    var_name='day',
    value_name='temp'
)

# data_details(weather_melt)


"""
9.2 At this point, if you want to build a model which 
    would end up predicting temperature, there is no way 
    to determine if the temperature is 'min' or 'max', since
    these specifications are hidden as VALUES in the 'element'
    column.
    
    We really want the tmax and tmin values to be separate 
    columns.
    
    So here, we would use the pivot table. See the link to 
        the documentation below:
        
        https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html
        
        Remember to read the above documentation very well.
        
        Please not that there is also a 'pivot' function to 
            pandas as well as the 'pivot_table' function.
            The pivot idea CANNOT handle duplicate values.
            
    Please note:
    
        The .melt() function can be used either as pd.melt(), 
        or as name_of_dataframe.melt().
            
"""
weather_tidy = weather_melt.pivot_table(

    # we begin by specifying the columns which we
    # do not want to touch, using the 'index' parameter.
    index=['id', 'year', 'month', 'day'],

    # next, we specify the columns on which we want to
    # do this pivot, using the columns parameter.
    # How does this work?
    # for every UNIQUE element in the column, a new column
    # would be created.
    columns='element',

    # In our case, we have just created two new columns. So,
    # Which data would be used to populate the columns?
    # We have to specify it.
    # The 'temp' column values would be used in our case.
    values='temp'

    # Please note:
    #       There is a parameter called 'drop_na'. By default,
    #       it is set to True. So in your results, all missing
    #       data points would be deleted.
    #       THEREFORE:
    #                   Treat missing value problems BEFORE
    #                   using the pivot_table() function.
)


# data_details(weather_tidy)


"""
9.3 Using the 'reset_index()' function in pandas.

    After using the pivot_table() function, we saw that
        there was some <<hierarchy>> of columns. 
        It was so irregular.
        Run this code and you will see: 
        
            data_details(weather_tidy)
            
        It is NOT GOOD for future analysis. 
        
        We can use the 'reset_index()' function to level all
            columns, so that the dataframe is good for FURTHER
            ANALYSIS.
            
            Note: 
                Sometimes, you have to run 'reset_index()' 
                twice before achieving your regular FLAT
                dataframe.
"""
weather_tidy = weather_tidy.reset_index()

# data_details(weather_tidy)    # Now, this is good!!


"""
10. What do we do when multiple types of observational units 
    are stored in the same table?
    
    Sometimes, the SAME DATA could be stored MULTIPLE times
    in the SAME TABLE.
    
    This takes a lot of memory!!
    
    Let us look at our billboard_melt dataframe above. 
    We would isolate all rows in which the track is the
    song 'Loser'.
    
    We would see that 'Loser' would be stored 76 times in the
    DATAFRAME. 
                Note that:
                            This is good for modelling, but 
                            maybe NOT for storage purposes as 
                            a lot of internal memory is 
                            avoidably consumed.
     
"""
# data_details(billboard_melt)

x_1 = billboard_melt.loc[billboard_melt['track'] == 'Loser']

# data_details(x_1)


"""
10 a. Implementing the principle.

        We have to drop duplicates, then merge stuff. 
        Let us see:
"""

"""
10 b. Create a 'songs' dataframe from the billboard dataframe.
"""
billboard_songs = billboard_melt[['year',
                                  'artist',
                                  'track',
                                  'time']]

"""
10 c. We see that the 'songs' dataframe has 24,000+ rows,
        duplicate data included.
"""

# data_details(billboard_songs)

"""
10 d. Let us drop duplicates
"""

billboard_songs = billboard_songs.drop_duplicates()
# data_details(billboard_songs)   # The data now has 317 rows. Wow!!

"""
10 e. Now you have a 'songs' dataset.

        You may later on create a 'ratings' dataset.
        
        The question now is, how do you join both datasets?
        
        Answer: We start by generating a key. 
        
            We create a new column called 'id', then give every
                song an 'id'.
"""
num_rows_in_billboard_songs = len(billboard_songs)
billboard_songs['id'] = range(num_rows_in_billboard_songs)
# data_details(billboard_songs)

"""
10 f. Save 'billboard_songs' dataset to csv
        
        index=False : 
                        This specification ensures that there
                        is no index in the final .csv file.
                        Set it to true if you need an index.
                        
        Comment out the code after running it, since the file
            would already have been created.
"""
# billboard_songs.to_csv('billboard_songs.csv', index=False)


"""
10 g. We now create our rank data.
        
        The idea is this: for every 'song id', what is the 
            week it corresponds to, and the rank for that week?
"""

billboard_ratings = billboard_melt.merge(
    billboard_songs,
    on=['year', 'artist', 'track', 'time']

    # Read the pandas.merge documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html
    # 'Tutorials point' explanation (Good): https://realpython.com/pandas-merge-join-and-concat/
)

"""
All we really did was to add that extra 'id' column from
the 'songs' dataframe.
"""
# data_details(billboard_ratings)

"""
10 h. We now filter the columns which we care about
"""
billboard_ratings = billboard_ratings[['id',
                                       'date.entered',
                                       'week',
                                       'rating']]

# data_details(billboard_ratings)

"""
10 i. Note that we can sample rows from a DataFrame
"""
a = billboard_ratings.sample(30)
# print(a)

"""
10 j. Save 'billboard_ratings' dataframe to .csv

    index=False : 
                        This specification ensures that there
                        is no index in the final .csv file.
                        Set it to true if you need an index.

    Comment out the code after running it, since the file
            would already have been created.
"""
# billboard_ratings.to_csv('billboard_ratings.csv', index=False)


"""
Read how to select data from a dataframe:

            https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
            https://towardsdatascience.com/23-efficient-ways-of-subsetting-a-pandas-dataframe-6264b8000a77
   
   
            
10 Efficient Ways for Inspecting a Pandas DataFrame Object:
        
        https://medium.com/codex/10-efficient-ways-for-inspecting-a-pandas-dataframe-object-3f66563e2f2
       
       
       
9 Efficient Ways for Describing and Summarizing a Pandas DataFrame:

        https://medium.com/codex/9-efficient-ways-for-describing-and-summarizing-a-pandas-dataframe-316234f46e6 



PANDAS API Reference:

        https://pandas.pydata.org/docs/reference/index.html#api
        
        

Pandas User Guide:

        https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#missing-data



Also check:

        Pandas:     group_by
        Pandas:     apply
        
        Python:    assert
"""





















































































































































































































































































































































