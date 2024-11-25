# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:22:49 2024

@author: Lenovo
"""

# streamlit_app.py
import streamlit as st
import pickle
import pandas as pd

# Load the saved model

model = pickle.load(open('svm.pkl', 'rb'))

# Define user input form
st.title("Liver Disease Prediction")
age = st.number_input('Age', min_value=0, max_value=100)
sex = st.selectbox('Sex', ('f', 'm'))
albumin = st.number_input('Albumin', min_value=34.0, max_value=54.0)
alkaline_phosphatase=st.number_input('alkaline_phosphatase',min_value=0.0,max_value=100.0,step=0.01)
alanine_aminotransferase=st.number_input('alanine_aminotransferase',min_value=0.0,max_value=100.0,step=0.01)
aspartate_aminotransferase=st.number_input('aspartate_aminotransferase',min_value=0.0,max_value=100.0,step=0.01)
bilirubin=st.number_input('bilirubin',min_value=0.0,max_value=100.0,step=0.01)
cholinesterase=st.number_input('cholinesterase',min_value=0.0,max_value=100.0,step=0.01)
cholesterol=st.number_input('cholesterol',min_value=0.0,max_value=100.0,step=0.01)
creatinina=st.number_input('creatinina',min_value=0.0,max_value=500.0,step=0.01)
gamma_glutamyl=st.number_input('gamma_glutamyl',min_value=0.0,max_value=100.0,step=0.01)
protein=st.number_input('protein',min_value=0.0,max_value=100.0,step=0.01)
# Add other features here

# Create a prediction button
if st.button("Predict"):
    # Process input data
    input_data = pd.DataFrame([[age, sex, albumin,alkaline_phosphatase,alanine_aminotransferase,aspartate_aminotransferase,bilirubin,
                                cholinesterase,cholesterol,creatinina,gamma_glutamyl,protein]], 
                              columns=['age', 'sex', 'albumin','alkaline_phosphatase','alanine_aminotransferase','aspartate_aminotransferase',
                                       'bilirubin','cholinesterase','cholesterol','creatinina','gamma_glutamyl_transferase','protein'])
    input_data['sex'] = 1 if sex == 'm' else 0  # Encode the sex variable

    # Debugging - Show input data
    st.write("Input Data:", input_data)

    # Make a prediction
    prediction = model.predict(input_data)
    st.write("Model Prediction:", prediction)  # Debugging - Show prediction output
    
    # Display the result based on prediction
    if prediction == 0:
        st.success("No disease")
    elif prediction == 1:
        st.success("Suspect Disease")
    elif prediction == 2:
        st.success("Hepatitis C")
    elif prediction == 3:
        st.success("Fibrosis")
    else:
        st.success("Cirrhosis")

    # Output the prediction
    #result = Predict(age, sex, albumin,alkaline_phosphatase,alanine_aminotransferase,aspartate_aminotransferase,bilirubin,
                                #cholinesterase,cholesterol,creatinina,gamma_glutamyl,protein)
   
   
    
         
