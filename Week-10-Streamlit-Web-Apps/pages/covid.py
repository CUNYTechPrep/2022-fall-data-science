import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json
import datetime


st.set_page_config(layout="wide")


st.header("Covid Dashboard")


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


# -- Create two columns
col1, col2 = st.columns([1,4])

with col1:
    st.write('Average number of cases per 100k compared to the national average.')


with col2:
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


    # create summary stats from selected_states dataframe
    summary_stats = state_df.groupby('state')['cases_avg_per_100k'].agg(['mean', 'median', 'min', 'max', 'std'])

    # This should work but doesn't     
    summary_stats.index = summary_stats.index.rename('Avg Cases Per 100k')

    # display the summary stats table
    st.write('Avg Cases Per 100k', summary_stats)


    # create line chart with just selected states
    fig = px.line(state_df, 
        x='date', 
        y='cases_avg_per_100k', 
        line_group='state', 
        color='state',
        title="Average # of cases per 100k people.",
        labels={ "cases_avg_per_100k": "Cases per 100k"} 
        )

    # changes the background color
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        })

    # changing the grid axes
    fig.update_xaxes(showgrid=False, gridwidth=1, gridcolor='Gray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='Gray')

    # display graph
    st.plotly_chart(fig, use_container_width=True)



    # create line chart of just last 90 days.
    today = datetime.datetime.now()
    d = datetime.timedelta(days = 50)
    last_90 = today - d

    df_last_ninety_days =  state_df[state_df['datetime'] > last_90]
    fig = px.line(df_last_ninety_days, 
        x='date', 
        y='cases_avg_per_100k', 
        line_group='state', 
        color='state',
        title="Last 90 Days:  Average # of cases per 100k people.",
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

    # display the chart.
    st.plotly_chart(fig, use_container_width=True)


# inside column 1
with col1:

    # for each state in selected states
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
