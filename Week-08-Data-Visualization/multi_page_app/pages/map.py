import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json


#https://github.com/nytimes/covid-19-data/tree/master/rolling-averages
st.set_page_config(layout="wide")

def load_data(fp):
    return pd.read_csv(fp)


def load_geos(fp):
    with open(fp) as response:
        counties = json.load(response)
    return counties


# loading the data
df_counties = load_data('data/us-counties-recent.csv')
geo_fp = 'data/geojson-counties-fips.json'
counties = load_geos(geo_fp)


# converting to date-time cause date_input needs to be a datetime object
df_counties['date'] = pd.to_datetime(df_counties['date'])


# getting the max date
max_date = df_counties.date.max()


# setting the default value to the max date
selected_date = st.date_input(
    "Select date to see daily covid rate", 
    value=max_date)


st.write("Displaying data for %s" % selected_date)

# selecting just the selected date
df_counties = df_counties[ df_counties['date'] == str(selected_date)]


# Creating the choropleth map
fig = px.choropleth(df_counties, 
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


