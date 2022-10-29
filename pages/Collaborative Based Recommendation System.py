import streamlit as st
import pandas as pd
from pickle import load
import bz2

st.set_page_config(page_title="Movie Recommendation System", page_icon="🤔",layout="wide")
st.title("Collaborative Based Recommendation System")
def decompress_pickle(file):
	data = bz2.BZ2File(file, 'rb')
	data = load(data)
	return data
model = decompress_pickle('pickle/movies_collaborative_dict.pbz2')
model1=load(open('pickle/movies_content_dict.pkl','rb'))
similarity = load(open('pickle/similarity_collaborative.pkl','rb'))

movies = pd.DataFrame(model)
movies_names=pd.DataFrame(model1)
def recommend_movie(movie_name,user_rating):
    score = movies[movie_name]*(user_rating-2.5)
    score = score.sort_values(ascending = False).head(15)
    score=score.to_string()
    return score

st.subheader('Top 15 Movies: ')

movie_name=st.selectbox(
"Type or select a movie from the dropdown",
movies_names['title'].values
)
rating=st.slider("Rating", min_value=0, max_value=5)

if st.button('Show Recommendation'):
    output= recommend_movie(movie_name,rating)
    output=output[6:]
    st.text(output)
