import streamlit as st

st.set_page_config(page_title="About", page_icon="❤️",layout="wide",)

st.header('About Movie Recommendation System')
about= '''
A movie recommendation system, or a movie recommender system, is an ML-based approach to filtering or predicting the users’ film preferences based on their past choices and behavior. It’s an advanced filtration mechanism that predicts the possible movie choices of the concerned user and their preferences towards a domain-specific item, aka movie.
'''
st.markdown(about,unsafe_allow_html=True)

st.header('Developers:')
d='''
Made with ❤️ by :\n
Dhruv Dixit \n
Dhreeti Kesharwani \n
Erram Prithvi Raj \n
Aakash Kovai \n
Kasukurti Shiva Kumar

'''
st.markdown(d,unsafe_allow_html=True)
