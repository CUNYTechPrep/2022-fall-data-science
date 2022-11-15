import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json


#https://github.com/nytimes/covid-19-data/tree/master/rolling-averages
st.set_page_config(layout="wide")

def strip_fips(input_string):
    try:
        return( input_string.split('-')[1] )
    except:
        return(00000)


@st.cache
def load_geos(fp):
    print('Running load_geos function...')
    with open(fp) as response:
        counties = json.load(response)
    return(counties)



@st.cache
def load_counties(fp):
    print('Running load_counties function...')
    df = pd.read_csv(fp)

    # extracting the fips code
    df['fips'] = df['geoid'].apply(strip_fips)

    # converting to date-time cause date_input needs to be a datetime object
    df['date'] = pd.to_datetime(df['date'])
    return(df)





county_fp = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/rolling-averages/us-counties-recent.csv'
df_counties = load_counties(county_fp)

geo_fp = 'data/geojson-counties-fips.json'
counties = load_geos(geo_fp)


# getting the valid dates
max_date = df_counties.date.max()
min_date = df_counties.date.min()


# setting the default value to the max date
# and limiting selection to only dates in dataframe
selected_date = st.date_input(
    "Select date to see daily covid rate", 
    min_value=min_date,
    max_value=max_date,
    value=max_date)


st.write("Displaying data for %s" % selected_date)

# selecting just the selected date
df_to_plot = df_counties[ df_counties['date'] == str(selected_date)].copy()


# Creating the choropleth map
fig = px.choropleth(df_to_plot, 
                    geojson=counties, 
                    locations='fips', 
                    color='cases_avg_per_100k',
                    color_continuous_scale="OrRd",
                    scope="usa",
                    range_color=(0, 50), 
                    hover_data=["county", "state", "cases_avg_per_100k"]
                   )


# changing the charts background color
fig.update_layout(geo=dict(bgcolor= 'rgba(0,0,0,0)'))
fig.update_traces(marker_line_width=0)


# pushing the chart to the page
st.plotly_chart(fig, use_container_width=True)


