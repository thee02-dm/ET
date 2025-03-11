import streamlit as st
import pandas 
st.title('Machine Learning App')

st.info ('This App is built on Machine Learning Model')

df = pd.read_csv ('https://raw.githubusercontent.com/thee02-dm/yt-ml/refs/heads/master/.streamlit/penguins_cleaned.csv')
df
