import streamlit as st
import pandas as pd
from pickle import load

st.set_page_config(page_title="Movie Recommendation System", page_icon="🤔",layout="wide")
st.title("Popularity Based Recommendation System")
model = load(open('pickle/movies_popularity.pkl','rb'))
movies = pd.DataFrame(model)
movies_names=[]
def recommend():
    movies_list=movies["title"]
    for i in movies_list:
        movies_names.append(i)
    return movies_names

st.subheader('Top 12 Movies: ')
output=recommend()
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.text("1."+output[0])
with col2:
    st.text("2."+output[1])
with col3:
    st.text("3."+output[2])
with col4:
    st.text("4."+output[3])
col5, col6, col7, col8 = st.columns(4)
with col5:
    st.text("5."+output[4])
with col6:
    st.text("6."+output[5])
with col7:
    st.text("7."+output[6])
with col8:
    st.text("8."+output[7])
col9, col10, col11, col12 = st.columns(4)
with col9:
    st.text("9."+output[8])
with col10:
    st.text("10."+output[9])
with col11:
    st.text("11."+output[10])
with col12:
    st.text("12."+output[11])
