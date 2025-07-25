# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 09:00:04 2025

@author: P.Indra
"""
import base64
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#set page configuration
st.set_page_config(page_title="Health Assistance",
                   layout='wide',
                   page_icon="🧑‍⚕️")
#back ground image
def back_ground(image_file):
    with open(image_file,'rb') as image:
       encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp{{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            }}
        </style>
        """,
        unsafe_allow_html=True
        )
back_ground("C:/Users/P.Indra/Downloads/machine learning/image.png")
    
    
    

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

#loading the saved models
diabetes_model=pickle.load(open('C:/Users/P.Indra/Downloads/machine learning/savedmodels/trained_model_sav','rb'))

heart_disease_model=pickle.load(open('C:/Users/P.Indra/Downloads/machine learning/savedmodels/Heart_Disease_Model.sav','rb'))

parkinsons_model=pickle.load(open('C:/Users/P.Indra/Downloads/machine learning/savedmodels/parkinsons_model.sav','rb'))

#sidebar for navigator

with st.sidebar:
    
    selected = option_menu('Multiple Disease prediction systen Using ML',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons = ['activity','heart','person'],
                             default_index=0)
    
    

#diabetes prediction page
if(selected =='Diabetes Prediction'):
    #page title
    st.title('Diabetes prediciton using ML')
    
    #getting the input data from the user
   
    
    
    Pregnancies=st.text_input('Number of pregnancies')
    Glucose=st.text_input('Glucose Level')
    BloodPressure=st.text_input('Blood Pressure Value')
    SkinThickness=st.text_input('SkinThickness Value')
    Insulin=st.text_input('Insulin Level')
    BMI=st.text_input('BMI of a person')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    Age=st.text_input('Age of the person')
    
    
    # code for predection
    dignosis =''
    
    #creating a button for prediction
    
    if st.button('Check Diabetes Test results'):
        
     
        
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])
       
        
        if(diab_prediction[0]==1):
            dignosis='the person is Diabetic'
        else:
            dignosis='the person is not Diabetic'
    st.success(dignosis)
     


if(selected =='Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction using ML')
    
    #getting the inputs from user
    #colums for input file
    
    col1,col2,col3 = st.columns(3)
    with col1:
        age=st.text_input('Enter your Age')
    with col2:
        sex=st.text_input('Enter your Gender')
    with col3:
        cp=st.text_input('Enter your CP')
    with col1:
        trestbps=st.text_input('Enter trestbps')
    with col2:
        chol=st.text_input('Enter chol')
    with col3:
        fbs=st.text_input('Enter fbs')
    with col1:
    
        restecg=st.text_input('Enter restecg')
    with col2:
        thalach=st.text_input('Enter thalach')
    with col3:
        exang=st.text_input('Enter exang')
    with col1:
        oldpeak=st.text_input('Enter oldpeak')
    with col2:
        slope=st.text_input('Enter slope')
    with col3:
        ca=st.text_input('Enter ca')
    with col1:
        thal=st.text_input('Enter thal')
    
    test=''
    
    if st.button('check Heart Disease '):
        
        user_input = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = diabetes_model.predict([user_input])
       
      
        if (heart_prediction[0]==1):
            test='the person heart is not health'
        else:
            test='the person is healthy'
    st.success(test)
    
    
    

if(selected =='Parkinsons Prediction'):
    #page title
    st.title('Parkinsons Disease Prediction using ML')
    
    
    #getting the inputs from user
    col1,col2,col3 = st.columns(3)
    with col1:
        MD1= st.text_input('Enter MDVP:Fo(Hz)')
    with col2:
        MD2=st.text_input('Enter MDVP:Fhi(Hz)')
    with col3:
        MD3=st.text_input('Enter  MDVP:Flo(Hz)')
    with col1:
        MD4=st.text_input('Enter MDVP:Jitter ')
    with col2:
        MD5=st.text_input('Enter MDVP:Jitter')
    with col3:
        MD6=st.text_input('Enter MDVP:RA')
    with col1:
        MD7=st.text_input('Enter MDVP:PPQ')
    with col2:
        MD8=st.text_input('Enter Jitter:DDP')
    with col3:
        MD9=st.text_input('Enter MDVP:Shimmer')
    with col1:
        MD10=st.text_input('Enter MDVP:Shimmer(dB)')
    with col2:
        ShimmerAPQ3=st.text_input('Enter Shimmer:APQ3')
    with col3:
        ShimmerAPQ5=st.text_input('Enter Shimmer:APQ5')
    with col1:
        MDVPAPQ=st.text_input('Enter MDVP:APQ')
    with col2:
        MD12=st.text_input('Enter Shimmer:DDA')
    with col3:
        NHR=st.text_input('Enter NHR')
    with col1:
        HNR=st.text_input('Enter HNR')
    with col2:
        RPDE=st.text_input('Enter RPDE')
    with col3:
        DFA=st.text_input('Enter DFA')
    with col1:
        spread1=st.text_input('Enter spread1')
    with col2:
        spread2=st.text_input('Enter spread2')
    with col3:
        D2=st.text_input('Enter D2')
    with col1:
        PPE=st.text_input('Enter PPE')
    
    
    
    parkinsons=''
    
    if st.button('check parkinson Diesease'):
        
        
        user_input = [MD1,MD2,MD3,MD4,MD5,MD6,MD7,MD8,MD9,MD10,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,MD12,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = diabetes_model.predict([user_input])
       
        if (parkinsons_prediction[0]==0):
            parkinsons='the result is negative , your healthy'
        else:
            parkinsosn='result is positive'
        
    st.success(parkinsons)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    