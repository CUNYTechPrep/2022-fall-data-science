import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Create a page header
st.header("Welcome to my homepage! 👋")


# Create three columns 
col1, col2, col3 = st.columns([1,1,1])


# inside of the first column
with col1:

    # display a picture
    st.image('images/covid-icon.png')

    # display the link to that page.
    st.write('<a href="/covid"> Check out my Covid Dashboard</a>', unsafe_allow_html=True)
    
    # display another picture
    st.image('images/friends.png')

    # display another link to that page
    st.write('<a href="https://www.behance.net/datatime">View more pretty data visualizations.</a>', unsafe_allow_html=True)


# inside of column 2
with col2:
    # display a picture
    st.image('images/covid-map.png')

    # display a link 
    st.write('<a href="/map"> Check out my Interactive Map</a>', unsafe_allow_html=True)    
    

    # same
    st.image('images/github.png')
    # same
    st.write('<a href="https://github.com/zd123"> View more awesome code on my github.</a>', unsafe_allow_html=True)    



# inside of column 3
with col3:
    # st.write('<div style="background:red">asdf </div>', unsafe_allow_html=True)
    
    # display a picture
    st.image('https://www.rmg.co.uk/sites/default/files/styles/full_width_1440/public/Atlantic%20liner%20%27Titanic%27%20%28Br%2C%201912%29%20sinking%2C%20bow%20first%2C%201912%2C%20with%20eight%20full%20lifeboats%20nearby%20and%20an%20iceberg%20in%20the%20distance_banner.jpg?itok=fQV6kN3z')

    # display a link to that page
    st.write('<a href="/Titanic">Interact with my ML algorithm.</a>', unsafe_allow_html=True)    
    
    # same
    st.image('https://i1.sndcdn.com/avatars-000034142709-fv26gu-t500x500.jpg')
    #same
    st.markdown('<a href="/Bio">Learn more about me as a human :blush:</a>', unsafe_allow_html=True)






