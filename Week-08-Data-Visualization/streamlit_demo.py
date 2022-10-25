import streamlit as st
import pandas as pd
import numpy as np

st.header('Hello Everyone!')


df = pd.read_csv('multi_page_app/data/us-states-national-average.csv')

checked = st.checkbox('Show raw data')

if checked == True:
    st.subheader('First 5 rows of data.')
    st.dataframe(df[:5])

clicked = st.button('Click Me')

if clicked:
	st.write('Woah it worked!')

st.code("""
	for i in range(100):  
    print(i)
		""")

# st.button('Click me')
# st.checkbox('I agree')
# st.radio('Pick one', ['cats', 'dogs'])
# st.selectbox('Pick one', ['cats', 'dogs'])
# st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
# st.slider('Pick a number', 0, 100)
# st.select_slider('Pick a size', ['S', 'M', 'L'])
# st.text_input('First name')
# st.number_input('Pick a number', 0, 10)

# st.text_area('Text to translate')

# st.date_input('Your birthday')

# st.time_input('Meeting time')

# st.file_uploader('Upload a CSV')

# st.camera_input("Take a picture")

# st.color_picker('Pick a color')