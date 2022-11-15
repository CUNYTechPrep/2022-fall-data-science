import streamlit as st
import pandas as pd
import pycaret
from pycaret.classification import *




df = pd.read_csv('data/titanic.csv')
df = df.drop(columns=['passengerid', 'ticket', 'cabin', 'name', 'age', 'sibsp', 'parch', 'embarked'])
df = pd.get_dummies(df, columns=['sex', 'pclass'], drop_first=True)

df.head()

setup(data = df, target = 'survived', session_id=69, silent=True) 

with st.spinner('Running multiple machine learning models. Please wait....'):
	best_model = compare_models()

st.header('Completed running all models!')
st.write('See results below.')
st.balloons()
report = pull()

st.dataframe(
	report.style.highlight_max(axis=0, color='yellow'),
	use_container_width=True
	)
	


best_choice = str(best_model)

st.markdown("The best model is:\n\n"+
	best_choice
	)


