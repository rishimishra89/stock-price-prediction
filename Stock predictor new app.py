# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:29:30 2024

@author: AMIT
"""
import streamlit as st
import pickle
import pandas as pd

# Load the model
loaded_model = pickle.load(open("C:/Users/AMIT/Desktop/All subs/Evoastra/trained_model.sav", "rb"))

def Stock_predictor(compound,score,price_volatility):
    
    input_data = pd.DataFrame([[compound, score, price_volatility]], columns=['compound', 'score', 'price_volatility'])
    predict = loaded_model.predict(input_data)[0] 
    
    if predict:
        return "Congrats for profit"
    else:
        return "Sorry you suffered a loss"
    
def main():
    
    st.title("Stock Predictor App")
    
    compound = st.text_input("Compound Value :")
    score = st.text_input("Score value :")
    price_volatility = st.text_input("price_volatility :")
    
    predict = ""
    
    if st.button("Stock Predictor"):
        predict = Stock_predictor(compound, score, price_volatility)
        
    st.success(predict)
    
    
if __name__ == '__main__':
    main()
