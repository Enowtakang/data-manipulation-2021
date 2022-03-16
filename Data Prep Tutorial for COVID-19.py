# """
# Data prep for Coronavirus dataset
# ---------------------------------
#
# Credits:
#     https://github.com/CSSEGISandData/COVID-19
# Task:
#     1. Update dataset
#     2. Automate the updating process
# Note:
#     1. For downloading wheels (GDAL and Fiona, etc):
#         https://www.lfd.uci.edu/~gohlke/pythonlibs/
#
#     2. For installing downloaded wheels (Example):
#
#     cd C:\path\to\the\folder\that\contains\the\WHL\files
#     pip3.7 install GDAL-3.0.4-cp37-cp37m-win_amd64.whl && setx GDAL_VERSION "3.0.4"
#     pip3.7 install Fiona-1.8.13-cp37-cp37m-win_amd64.whl
#     pip3.7 install geopandas-0.7.0-py3-none-any.whl
#
#     3. What I actually did:
#
#     Go to this site, read Step 5 in order to understand:
#     https://www.pointsnorthgis.ca/blog/geodjango-gdal-setup-windows-10/
#
#     Other needed links for all info:
#
#     https://geopandas.org/en/stable/getting_started/install.html
#     https://stackoverflow.com/questions/61416724/issues-installing-geopandas-on-windows/61418519#61418519
#     https://www.lfd.uci.edu/~gohlke/pythonlibs/
#     https://stackoverflow.com/questions/65627536/the-token-is-not-a-valid-statement-separator-in-this-version
#     https://www.lfd.uci.edu/~gohlke/pythonlibs/
#     https://stackoverflow.com/questions/34427788/how-to-successfully-install-pyproj-and-geopandas
#
#     Remember: What I actually did.
#
#     cd C:\Users\HP\PythonWheels
#     pip3.8 install GDAL-3.3.3-cp38-cp38-win_amd64.whl
#     pip3.8 install Fiona-1.8.20-cp38-cp38-win_amd64.whl
#     pip install geopandas
#
#     pip install descartes
# """

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

"""
1. Get Url to data

    We look up the dashboard/dataset in github. 
    We then click on 'raw' to view the raw dataset in a different 
        HTML web page.
    We copy the link.
    
    Note: 
    
        0. Link to the mother HTML page
            https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series
            
        1. The link to the page containing the 'raw' button:
            https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
        The link of the HTML page with the raw data:
            https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
        
        2. RESEARCH on dashboards: creation, uses, applications 
        
        3. Recovered cases 'raw' button and raw data pages urls 
            respectively:
            
            'raw' button link:
            https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv
            
            data page url link:
            https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv
            
        4. Death cases 'raw' button and raw data pages urls 
            respectively:
            
            'raw' button link:
            https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv
            
            data page url link:
            https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv
            
"""

confirmed_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

recovered_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"

death_cases_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"


"""
2. Load dataset
    Pandas permits the loading of a dataset from the web.
    
    Since the data is in .csv() format, we'll use 
        pandas.read_csv()
"""

df_confirmed = pd.read_csv(confirmed_cases_url)
df_recovered = pd.read_csv(recovered_cases_url)
df_death = pd.read_csv(death_cases_url)


"""
3. See data details
"""


def data_details(name_of_dataframe):
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


# data_details(df_confirmed)


"""
4. Reshape data (df = confirmed)
    
    In our data frame, the dates are column names.
        Bad Stuff.
        
    When we look at the github page, we see that the dates
    are all in a column.
        We have to fix this.
        
    We use Pandas melt. 
    YOU NEED TO READ MORE ON PANDAS 'MELT'. 
    Check picture at 06:26 of video 
"""

# 'id_vars=' stores the variables which you do
# not want to melt
confirmed_df = df_confirmed.melt(id_vars=[
    'Province/State',
    'Country/Region',
    'Lat',
    'Long'])

"""
4.1 see new data structure
"""
# data_details(confirmed_df)   # good job

"""
4.2 Rename the two new 'variable' and 'data' columns 
    to 'date' and 'confirmed' respectively.
    
    "inplace= True" makes the changes permanent
"""
confirmed_df.rename(
    columns={"variable": "Date", "value": "Confirmed"},
    inplace=True)

# data_details(confirmed_df)


"""
5. Now, automate stuff by creating a function to 
    fetch data and reshape it.
"""


def get_and_melt_data(data_url, case_type):
    df = pd.read_csv(data_url)

    # melt df above
    melted_df = df.melt(id_vars=[
        'Province/State',
        'Country/Region',
        'Lat',
        'Long'])

    # rename columns
    melted_df.rename(
        columns={"variable": "Date", "value": case_type},
        inplace=True)

    # return
    return melted_df


"""
6. Now fetch Death or Recovered datasets
"""
recovered_df = get_and_melt_data(recovered_cases_url,
                                 "Recovered")

death_df = get_and_melt_data(death_cases_url,
                             "Death")

# data_details(recovered_df)
# data_details(death_df)
# data_details(confirmed_df)

# print(recovered_df.shape)
# print(death_df.shape)
# print(confirmed_df.shape)

"""
7. Merging 

    When we look at the columns from each dataset, we see
        that 'all of the data' and 'all of the columns' are 
        similar, except the last columns: 
            Recovered, Death & Confirmed, respectively.
        
    So in order to merge all three datasets, we just need to
        take the last columns in two of the datasets and merge
        them with the entirety of the remaining dataset. 
        
    It is important to note that all of the datasets should 
        have the same SHAPE.
    
    "I just discovered that the Recovered dataset does not 
        have the same shape as the rest. 
        Let me try my luck and see."
"""
# we start by merging the 'Death' column in the death_df
# dataset to the entirety of the confirmed_df dataset.

new_df = confirmed_df.join(death_df['Death'])
# data_details(new_df)

# We now 'further' merge with the 'Recovered' column
# of the recovered_df.
final_df = confirmed_df.join(
    death_df['Death']).join(
    recovered_df['Recovered'])

# data_details(final_df)

"""
NOTE
        The above merging worked! 

        What is the lesson? 
            In order to merge two columns with the 
                '.join' method in pandas, the initial
                dataframes from which the columns emanate
                MUST NOT have the same SHAPE.
                
            But if they don't have the same shape, you must
                know HOW TO DEAL WITH THE 'MISSING' DATA
                that would 'emerge' as a result of the merging
                of the two columns.
                
                All the missing data would have a value of
                    'NaN'. What to do?
"""


"""
8. We now save our modified dataset to a .CSV file

    This is powerful.
    
    Note that we can save the dataset from the data frame 
        to so many other file formats,
            including SQL.
            This is VERY POWERFUL, because we can then 
                load the data in the SQL file into 
                a MySQL database for storage and querying.
                
                Nice and Sweet.
"""

# final_df.to_csv("Coronavirus_updated_dataset.csv")


# I have commented out the above code, since the '.csv'
# file has already been created.


"""
9. Now, let us do some Visualization + Analysis

        We start with Geospatial plotting with Geopandas
"""

# 9.1 define the GeoDataFrame
geo_df_01 = gpd.GeoDataFrame(
    final_df, geometry=gpd.points_from_xy(
        final_df['Long'], final_df['Lat']
    )
)

# 9.2 Plot the data in the 'geo_df_01' GeoDataFrame
geo_df_01.plot(figsize=(20, 10))
# plt.show()


# We see that the data points have been plotted, but
# they need to be placed on top of a map, if we are to
# make sense of the figure (or the plot).


# 9.3 Overlapping with world map

# 9.3.1 Get world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
ax = world.plot(figsize=(20, 10))
ax.axis('off')
# plt.show()


# 9.3.2 Overlap
fig, ax = plt.subplots(figsize=(20, 10))
geo_df_01.plot(cmap='Reds', ax=ax)
world.geometry.boundary.plot(color=None,
                             edgecolor='k',
                             linewidth=2,
                             ax=ax)
# plt.show()


"""
10. We automate the work of collecting data on a 
        day to day basis.

    How?
        We create a new directory (autodata) in our
            current working directory (JCharisTech_2)
    
            - Go to terminal
            - Type: cd JCharisTech_2
            - Type: mkdir autodata
            - Type: cd autodata
            - Type: cls
        
        Now, we go to 'autodata' and continue coding 
                    there.
"""

