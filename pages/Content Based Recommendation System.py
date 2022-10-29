import streamlit as st
import pandas as pd
from pickle import load
import bz2

st.set_page_config(page_title="Movie Recommendation System", page_icon="🤔",layout="wide")
st.title("Content Based Recommendation System")
def decompress_pickle(file):
	data = bz2.BZ2File(file, 'rb')
	data = load(data)
	return data
similarity = decompress_pickle('pickle/similarity_content.pbz2') 
model = load(open('pickle/movies_content_dict.pkl','rb'))

movies = pd.DataFrame(model)
title_list=movies['title']
movies_names=[]
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
             recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.subheader('Top 5 Movies: ')
selected_movie_name = st.selectbox(
"Type or select a movie from the dropdown",
movies['title'].values
)
if st.button('Show Recommendation'):
    output= recommend(selected_movie_name)
    for i in output:
        st.text(i)
