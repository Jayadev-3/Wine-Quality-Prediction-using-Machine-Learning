import streamlit as st
import pandas as pd
import pickle
from PIL import Image

img = Image.open("img.png")
st.image(img, width=700)

st.title('WINE QUALITY PREDICTION USING RANDOM FOREST CLASSIFIER')
st.write("ENTER THE DETAILS TO PREDICT THE QUALITY OF WINE")

randomforestclassifier = open('wine_model.pkl', 'rb')
classifier = pickle.load(randomforestclassifier)

fa= st.text_input('Fixed acidity : ')
va= st.text_input('Volatile acidity : ')
ca= st.text_input('Citric acid : ')
rs= st.text_input('Residual sugar : ')
c= st.text_input('Chlorides : ')
fsd= st.text_input('Free Sulfur dioxide : ')
tsd= st.text_input('Total Sulfur dioxide : ')
d= st.text_input('Density : ')
ph= st.text_input('pH value : ')
s= st.text_input('Sulphates : ')
a= st.text_input('Alcohol : ')

submit = st.button("Predict")

if submit:
    prediction = classifier.predict(
        [[fa,va,ca,rs,c,fsd,tsd,d,ph,s,a]])
    if prediction == 1:
        st.write("GOOD QUALITY WINE")
    else:
        st.write("BAD QUALITY WINE")