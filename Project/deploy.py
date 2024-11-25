# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 15:37:31 2024

@author: Lenovo
"""

import pickle
import streamlit as st

# Open model in read binary mode
load = open('svm.pkl', 'rb')
model = pickle.load(load)

# Define predict function 
def predict(age, sex, albumin, alkaline_phosphatase, alanine_aminotransferase, aspartate_aminotransferase,
            bilirubin, cholinesterase, cholesterol, creatinina, gamma_glutamyl, protein):
    # Pass arguments in 2D array format
    prediction = model.predict([[age, sex, albumin, alkaline_phosphatase, alanine_aminotransferase,
                                 aspartate_aminotransferase, bilirubin, cholinesterase, cholesterol,
                                 creatinina, gamma_glutamyl, protein]])
    return prediction

def main():
    st.title('Free Disease Checkup')

    # Accept input values from user through browser
    age = st.number_input('Age: ', min_value=0, step=1)
    sex = st.radio('Sex:', [0, 1], format_func=lambda x: 'Male' if x == 0 else 'Female')  # Use radio for better input
    albumin = st.number_input('Albumin: ',min_value=0.0, step=0.01)
    alkaline_phosphatase = st.number_input('Alkaline Phosphatase: ',min_value=0.0, step=0.01)
    alanine_aminotransferase = st.number_input('Alanine Aminotransferase: ',min_value=0.0, step=0.01)
    aspartate_aminotransferase = st.number_input('Aspartate Aminotransferase: ',min_value=0.0, step=0.01)
    bilirubin = st.number_input('Bilirubin: ',min_value=0.0, step=0.01)
    cholinesterase = st.number_input('Cholinesterase: ',min_value=0.0, step=0.01)
    cholesterol = st.number_input('Cholesterol: ',min_value=0.0, step=0.01)
    creatinina = st.number_input('Creatinina: ',min_value=0.0, step=0.01)
    gamma_glutamyl = st.number_input('Gamma Glutamyl : ',min_value=0.0, step=0.01)
    protein = st.number_input('Protein: ',min_value=0.0, step=0.01)

    if st.button('Predict'):
        # Make prediction and debug result
        result = predict(age, sex, albumin, alkaline_phosphatase, alanine_aminotransferase, aspartate_aminotransferase,
                         bilirubin, cholinesterase, cholesterol, creatinina, gamma_glutamyl, protein)
        st.write("Prediction result:", result)  # Display result in Streamlit app for debugging

        # Display prediction category based on result
        if result == 0:
            st.success("Cirrhosis")
        elif result == 1:
            st.success("Fibrosis")
        elif result == 2:
            st.success("Hepatitis")
        elif result == 3:
            st.success("No_disease")
        elif result == 4:
            st.success("Suspect_disease")
        else:
            st.error("Prediction result not found")

# Run main function
if __name__ == '__main__':
    main()