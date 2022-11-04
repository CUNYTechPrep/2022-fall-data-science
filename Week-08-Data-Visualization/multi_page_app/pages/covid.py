import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from urllib.request import urlopen
import json


#https://github.com/nytimes/covid-19-data/tree/master/rolling-averages
st.set_page_config(layout="wide")

col0 = st.columns([1])[0]

# -- Create three columns
col1, col2, col3 = st.columns([1,1,4])


def load_data(fp):
    return pd.read_csv(fp)

def load_geos(fp):
    with open(fp) as response:
        counties = json.load(response)
    return counties


# loading the data

df = load_data('data/us-states-national-average.csv') 
df_counties = load_data('data/us-counties-recent.csv')


with col0:
    st.header('Welcome to my covid dashborad.')

with col1:
    st.write('Average number of cases per 100k compared to the national average.')


with col3:
    # create a list of all the state names
    state_list = sorted(df['state'].unique())
    
    # create a mulit select button
    selected_states = st.multiselect(
        'Select which states to compare.',
        state_list,
        default=['National Average']
        )



    # for debugging
    print(type(selected_states), selected_states)


    # extract just the selected states
    state_df = df[df['state'].isin(selected_states)].copy()

    # create line chart with just selected states
    fig = px.line(state_df, 
        x='date', 
        y='cases_avg_per_100k', 
        line_group='state', 
        color='state',
        title="Average # of cases per 100k people.",
        labels={ "cases_avg_per_100k": "Cases per 100k"} 
        )

    # changest the background color
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        })

    # changing the grid axes
    fig.update_xaxes(showgrid=False, gridwidth=1, gridcolor='Gray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='Gray')

    
    # create summary stats from selected_states dataframe
    summary_stats = state_df.groupby('state')['cases_avg_per_100k'].agg(['mean', 'median', 'min', 'max', 'std'])
    
    summary_stats.index = summary_stats.index.rename('Avg Cases Per 100k')
    st.write('Avg Cases Per 100k', summary_stats)
    st.plotly_chart(fig, use_container_width=True)


with col1:
    for state in selected_states:
        if state != 'National Average':
            avg = df[df['state'] == state]['cases_avg_per_100k'].mean()
            avg = round(avg, 2)
            national_average = df[df['state'] == 'National Average']['cases_avg_per_100k'].mean()
            national_average = round(national_average, 2)
            delta = avg-national_average
            delta = round(delta, 2)
            st.metric(label=state, value=avg, delta=delta, help='Average Cases Per 100k and the little number in green or red below is how it compares to the national average')
        else:
            national_average = df[df['state'] == 'National Average']['cases_avg_per_100k'].mean()
            national_average = round(national_average, 2)
            st.metric(label=state, value=national_average) #, delta=0.0, delta_color='off')
