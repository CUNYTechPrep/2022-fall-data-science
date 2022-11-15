import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Hello, Im Zack. It's nice to meet you",
    page_icon="👋",
)

st.write("# Welcome to my portfolio 👋")

col1, col2 = st.columns([1,1])

with col1:
    st.image('https://media-exp1.licdn.com/dms/image/C5603AQFHVJRtVAazbw/profile-displayphoto-shrink_800_800/0/1594756980450?e=2147483647&v=beta&t=IiEk7RhiY2zon4WFPFoK4OFTR6Vc31HFPR3lJ076J_8')


with col2:
    st.image('https://i1.sndcdn.com/avatars-000034142709-fv26gu-t500x500.jpg')


important_links = '''
[github.com/zd123](https://github.com/zd123),
[Company Github](https://github.com/CUNYTechPrep/2022-fall-data-science) _as a main contributor_.,
[IG](https://www.instagram.com/zd1233/),
[Surfline](https://www.surfline.com/)
'''

st.markdown(important_links)