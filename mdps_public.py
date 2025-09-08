# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 12:58:27 2025

@author: rohit
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('trained_model.sav','rb'))

heart_disease_model = pickle.load(open('heart_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
st.title("Multiple Disease Prediction System")
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.subheader('Diabetes Prediction')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.subheader('Heart Disease Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            # Convert all inputs to correct numeric types
            user_input = [
                int(age), int(sex), int(cp), int(trestbps), int(chol),
                int(fbs), int(restecg), int(thalach), int(exang),
                float(oldpeak), int(slope), int(ca), int(thal)
            ]
            
            heart_prediction = heart_disease_model.predict([user_input])                          
        
            if (heart_prediction[0] == 1):
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        
        except ValueError:
            heart_diagnosis = "⚠ Please enter valid numeric values for all fields."
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.subheader("Parkinson's Disease Prediction")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

import streamlit as st

def set_bg_from_url(url, opacity=0.975):
    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
            <p style="font-size:1.1rem; color:white;">
                Made by Rohit Kumar
                &nbsp;
                <a href="https://www.linkedin.com/in/rohit-kumar-58b26727b" style="color:white;">
                    <!-- linkedin svg -->
                </a>
                &nbsp;
                <a href="https://github.com/Rohit102030/Multiple-Diseases-prediction" style="color:white;">
                    <!-- github svg -->
                </a>
            </p>
        </div>
    </footer>
    """
    st.markdown(footer, unsafe_allow_html=True)

    # Dark overlay + readable inputs/labels
    st.markdown(
        f"""
        <style>
            /* Page background with a dark overlay for contrast */
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.76), rgba(0,0,0,0.76)), url('{url}') no-repeat center center fixed;
                background-size: cover;
                color: #ffffff !important;
            }}

            /* Headings, labels and general text */
            h1, h2, h3, h4, h5, h6, label, .stText, .stMarkdown, .block-container, .element-container, .main {{
                color: #ffffff !important;
            }}

            /* Make input boxes dark translucent with white text */
            input[type="text"], input[type="number"], input[type="search"], textarea, select, .stTextInput input, .stNumberInput input, .stTextArea textarea {{
                background: rgba(0,0,0,0.55) !important;
                border: 1px solid rgba(255,255,255,0.12) !important;
                color: #ffffff !important;
                box-shadow: none !important;
            }}

            /* Placeholder text: ensure high contrast and visibility */
            input::placeholder, textarea::placeholder {{
                color: rgba(255,255,255,0.7) !important;
                opacity: 1 !important;
            }}
            /* For some browsers */
            ::-webkit-input-placeholder {{ color: rgba(255,255,255,0.7) !important; }}
            ::-moz-placeholder {{ color: rgba(255,255,255,0.7) !important; }}

            /* Sidebar slightly lighter but still dark */
            [data-testid="stSidebar"] {{
                background-color: rgba(255,255,255,0.03) !important;
                color: #ffffff !important;
            }}

            /* Buttons */
            button, .stButton>button {{
                background-color: rgba(255,255,255,0.06) !important;
                color: #ffffff !important;
                border: 1px solid rgba(255,255,255,0.12) !important;
            }}

            /* Remove intrusive shadows on widgets */
            .stTextInput, .stNumberInput, .stTextArea {{
                box-shadow: none !important;
            }}

            /* Ensure Streamlit markdown/code blocks inherit readable color */
            .stMarkdown, .stText, .css-1v3fvcr {{ color: #fff !important; }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Example usage
set_bg_from_url("https://images.everydayhealth.com/homepage/health-topics-2.jpg?w=768", opacity=0.975)










