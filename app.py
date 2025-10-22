import streamlit as st
import pickle
import pandas as pd
import requests
import time
import os

TMDB_API_KEY = os.environ.get("TMDB_API_KEY")


def fetch_poster(movie_id, retries=2, delay=1):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    for attempt in range(retries + 1):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            poster_path = data.get("poster_path")
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500/{poster_path}"
            else:
                print(f"[{attempt}] No poster found for movie ID {movie_id}")
                return "https://via.placeholder.com/500x750.png?text=No+Poster"
        except requests.exceptions.RequestException as e:
            print(f"[{attempt}] Error fetching poster for movie ID {movie_id}: {e}")
            time.sleep(delay)  # Wait before retrying
    return "https://via.placeholder.com/500x750.png?text=No+Poster"


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    recommended_mkvs=[]
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_mkvs.append(movies.iloc[i[0]].title)    
        #fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_mkvs, recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity  = pickle.load(open('similarity.pkl','rb'))
 
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values,
)

st.write("You selected:", selected_movie_name)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])