import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json


@st.cache
def load_covid_data(fp):
    print('Running load_covid_data...')

    # read in the csv via the link
    df = pd.read_csv(fp)

    # Creating the National Average
    national_average = df.groupby('date')['cases_avg_per_100k'].mean()

    # turn that into a data frame
    national_average = pd.DataFrame(national_average).reset_index()

    # create a state column
    national_average['state'] = 'National Average'

    # add it to the main dataframe
    df = df.append(national_average)

    df['datetime'] = pd.to_datetime(df['date'])

    return(df)


# loading the data
fp = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/rolling-averages/us-states.csv'

df = load_covid_data(fp) 

summary_stats = df.groupby('state')['cases_avg_per_100k'].agg(['mean', 'median', 'min', 'max', 'std'])

st.dataframe(
	summary_stats.style.highlight_max(axis=0, color='red'),
	use_container_width=True)
