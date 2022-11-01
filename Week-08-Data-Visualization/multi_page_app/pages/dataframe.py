import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json


df = pd.read_csv('data/us-states-national-average.csv') 
summary_stats = df.groupby('state')['cases_avg_per_100k'].agg(['mean', 'median', 'min', 'max', 'std'])
st.dataframe(summary_stats.style.highlight_max(axis=0, color='red'))