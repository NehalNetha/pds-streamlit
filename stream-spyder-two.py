#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:29:01 2023

@author: nehal
"""


import streamlit as st
import pickle
import sklearn

 # Import your machine learning code





#add_selectbox = st.sidebar.selectbox(
  #  "which model do you wanna use?",
#    ("Logistic Regression", "KNN", "Random Forest Classifier")
#)

#if add_selectbox == 'Logistic Regression':
   # st.subheader("Logistic Regression")
token = pickle.load(open("/Users/nehal/pds-final-streamlit/model-log-cv.pkl", "rb"))
model = pickle.load(open("/Users/nehal/pds-final-streamlit/model-log-clf.pkl", "rb"))

    
#elif add_selectbox == "Random Forest Classifier":
    #st.subheader("Random Forest Classifier")
  #  token = pickle.load(open("/Users/nehal/pds-final-streamlit/model-log-cv.pkl", "rb"))
   # model = pickle.load(open("/Users/nehal/pds-final-streamlit/model-rf-clf.pkl", "rb"))

#elif add_selectbox == "KNN":
    #st.subheader("KNN")

   # token = pickle.load(open("/Users/nehal/pds-final-streamlit/model-cv.pkl", "rb"))
  ##  model = pickle.load(open("/Users/nehal/pds-final-streamlit/model-clf.pkl", "rb"))

    



def predict_age(input):

    t = token.transform([input])
    predict = model.predict(t)
    return int(predict[0])

def main():
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Stock Markert Sentiment Analysis</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    inp = st.text_input("headlines")
    if st.button("Predict the sentiment of the headline"):
        output = predict_age(inp)
        if output == 0:
            st.success('The headlines is neutral')
        elif output == 1:
            st.success('The headlines is positive')
        else:
            st.success('The headlines is negative')
            
        

if __name__ == "__main__":
    main()
