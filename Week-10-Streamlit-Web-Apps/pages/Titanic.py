import streamlit as st
import pandas as pd
import pickle
import plotly.express as px



# Load the model you already created...
model = pickle.load(open('models/model.pkl', 'rb'))


# Begin user inputs

# Get fare
fare = st.slider('Select passenger fare', 0, 99)

# Get pclass
pclass = st.radio('Pick passenger pClass they were in', ['1', '2', '3'])


# Get Sex
sex_male = st.radio('Pick passenger sex', ['Male', 'Female'])




# Button to start prediction, Once make_prediction button is clicked...
make_prediction = st.button('Submit and make prediction.')


# Once make_prediction button is clicked... the code below will run. 
if make_prediction:
	if pclass == '1':
		# Remember pclass == 0 when pclass_2 and pclass_3 are both 0.
		pclass_2 = 0
		pclass_3 = 0

	if pclass == '2':
		pclass_2 = 1
		pclass_3 = 0

	if pclass == '3':
		pclass_2 = 0
		pclass_3 = 1

	if sex_male == 'Male':
		sex_male_int = 1
	else:
		sex_male_int = 0

	# put the variables into a list in the same order as the model expects them in.
	to_predict = [fare, pclass_2, pclass_3, sex_male_int]

	# make a prediction
	prediction = model.predict([to_predict])

	# get the predicted probability 
	prediction_proba = model.predict_proba([to_predict])

	# debugging help
	print(prediction_proba)

	# extract the predicted value. 
	value = prediction[0]

	# if it predicts zero, then make output 'Death' else 'Survived'
	# also get the predicted probability 
	if value == 0:
		pred_output = 'Death'
		pred_proba = prediction_proba[0][0].round(2) * 100
	else:
		pred_output = 'Survival'
		pred_proba = prediction_proba[0][1].round(2) * 100

	# Generate output text
	output_text = '## Predicted a ' + '%' + '**%s chance of %s** \n\n based on the input of %s' % (pred_proba, pred_output, str(to_predict))

	# Display the users input variables back to them.
	st.markdown(output_text)
	st.markdown('Fare='+str(fare))
	st.markdown('Sex='+sex_male)
	st.markdown('Pclass='+str(pclass))
	st.balloons()