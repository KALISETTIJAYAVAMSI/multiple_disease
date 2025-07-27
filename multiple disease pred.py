# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 11:10:50 2025

@author: jayav
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models

diabetes_model=pickle.load(open('trained_model.sav','rb'))

heart_disease_model=pickle.load(open('heart_model.sav','rb'))

parkinsons_model=pickle.load(open('pakinson_model.sav','rb'))


#sidebar for navigation


with st.sidebar:
    
    selected=option_menu('multiple disease prediction', 
                        
                         ['diabetes prediction',
                          'heart disease prediction',
                          'parkinsons prediction'],
                         
                         icons=['activity','heart','person'],
                         default_index=0)
######################################################################################
#diabetes prediction page
if(selected == 'diabetes prediction'):
    #page title
    st.title('diabetes prediction using ml')
    
    #getting the input data from user
    #columns for input fields
    col1,col2,col3=st.columns(3)
    
    
    with col1:
        pregnancies =st.text_input('number of pregnancies')
    with col2:
        glucose =st.text_input('glucose level')
    with col3:
        bloodpressure =st.text_input('blood pressure value')
    with col1:
        skinthickness =st.text_input('skin thickness value')
    with col2:
        Insulin =st.text_input('insulin value ')
    with col3:
        BMI =st.text_input('BMI VALUE')
    with col1:
        diabetespedigreefunction =st.text_input(' diabetespedigreefunction value ')
    with col2:
        Age =st.text_input('Age')
        
        
    
    #code for prediction
    diab_diagnosis = ''
    
    # creating a button for prediction
    if st.button('diabetes test result'):
        diab_prediction=diabetes_model.predict([[pregnancies,glucose,bloodpressure,skinthickness,Insulin,BMI,diabetespedigreefunction,Age]])
        if(diab_prediction[0]==1):
            diab_diagnosis='the person is diabetic'
        else:
            diab_diagnosis='the person is not diabetic'
    st.success(diab_diagnosis)
        
        
        
        
        
        
#####################################################################################    
if(selected=='heart disease prediction'):
    #page title
    st.title('heart disease prediction using ml')
    
    #getting the input data from user
    #columns for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input('age')
    with col2:
        sex=st.text_input('sex')
    with col3:
        cp=st.text_input('cp')
    with col1:
        trestbps=st.text_input('trestbps')
    with col2:
        chol=st.text_input('chol')
    with col3:
        fbs=st.text_input('fbs')
    with col1:
        restecg=st.text_input('restecg')
    with col2:
        thalach=st.text_input('thalach')
    with col3:
        exang=st.text_input('exang')
    with col1:
        oldpeak=st.text_input('oldpeak')
    with col2:
        slope=st.text_input('slope')
    with col3:
        ca=st.text_input('ca')
    with col1:
        thal=st.text_input('thal')
        
    #code for prediction
    heart_diagnosis = ''
    
    # creating a button for prediction
    if st.button('heart test result'):
        heart_prediction=heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if(heart_prediction[0]==1):
            heart_diagnosis='the person having heart disease'
        else:
            heart_diagnosis='the person is not having heart disease'
    st.success(heart_diagnosis)
        
        
#########################################################################################
if(selected=='parkinsons prediction'):
    #page title
    st.title('parkinsons prediction using ml')
    
    #getting the input data from user
    #columns for input fields
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        Fo=st.text_input('MDVP:Fo(Hz)')
    with col2:
        Fhi=st.text_input('MDVP:Fhi(Hz)')
    with col3:
        Flo=st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter2=st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter1=st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP=st.text_input('MDVP:RAP')
    with col2:
        PPQ=st.text_input('MDVP:PPQ')
    with col3:
        Jitter=st.text_input('Jitter:DDP')
    with col4:
        Shimmer4=st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer3=st.text_input('MDVP:Shimmer(dB)')
    with col1:
        Shimmer2=st.text_input('Shimmer:APQ3')
    with col2:
        Shimmer1=st.text_input('Shimmer:APQ5')
    with col3:
        APQ=st.text_input('MDVP:APQ')
    with col4:
        Shimmer=st.text_input('Shimmer:DDA')
    with col5:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input('DFA')
    with col4:
        spread1=st.text_input('spread1')
    with col5:
        spread2=st.text_input('spread2')
    with col1:
        D2=st.text_input('D2')
    with col2:
        PPE=st.text_input('PPE')
    
    
    
    #code for prediction
    parkinsons_diagnosis = ''
    
    # creating a button for prediction
    if st.button('parkinsons test result'):
        parkinsons_prediction=parkinsons_model.predict([[Fo,Fhi,Flo,Jitter2,Jitter1,RAP,PPQ,Jitter,Shimmer4,Shimmer3,Shimmer2,Shimmer1,APQ,Shimmer,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        if(parkinsons_prediction[0]==1):
            parkinsons_diagnosis='the person having parkinsons'
        else:
            parkinsons_diagnosis='the person is not having parkinsons'
    st.success(parkinsons_diagnosis)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
##########################################################################################