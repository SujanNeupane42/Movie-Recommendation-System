# Importing Dependencies
import streamlit as st
import pickle
import pandas as pd
import requests
import base64

# For getting the background image
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    st.set_page_config(layout="wide")
    bin_str = get_base64(png_file) 
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: scroll; 
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('./images/image2.jpg')

'''
Created on friday oct 22, 2021 by Sujan Neupane
'''
if st.button('GitHub'):
    url = "https://github.com/SujanNeupane42/Movie-Recommendation-Systems"
    st.write("[GitHub](%s)" % url)

st.title("Movie Recommendation System")
    
# Loading Pickled Data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Converting the loaded pickled data into a pandas dataframe
movies = pd.DataFrame(movies_dict)

# Inputs from the user
option = st.selectbox('Enter Your Favourite Movie:', movies['title'].values)
option1 = option.lower()
n_recommendations = st.slider('How many Movies do you want to be recommended? ', min_value=1, max_value=10, value=3, step=1) 


# This function makes use of The Moviedb API to access poster url of a movie
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=2f84edafaf37015fe23889c2d33e65b0&language=en-US".format(movie_id)
    # Converting a string, that is fetched through the API, into json object
    response = requests.get(url).json()
    poster = response['poster_path']
    # Url for poster of a movie
    poster_url = "https://image.tmdb.org/t/p/w500/" + poster
    return poster_url


# This function makes use of The Moviedb API to access other details of a movie
def fetch_details(movie_id):
    details = []
    url = "https://api.themoviedb.org/3/movie/{}?api_key=2f84edafaf37015fe23889c2d33e65b0&language=en-US".format(movie_id)
    # Converting a string, that is fetched through the API, into json object
    response = requests.get(url).json()

    # Appending movie's overview
    overview = response['overview']
    details.append(overview)

    # Apending movie's genres 
    genres = response['genres']
    n = []
    for i in range(len(genres)):
        n.append(genres[i]['name'])
    details.append(n)

    # Appending movie's budget
    budget = str(round(int(response['budget'])/(1000000), 2))
    details.append(budget)

    # Appending movie's revenue
    revenue = str(round(int(response['revenue'])/(1000000), 2))
    details.append(revenue)

    # Appending movie's release date
    release_date = (response['release_date'])
    details.append(release_date)

    # Appending movie's link to homepage
    homepage = response['homepage']
    details.append(homepage)

    # Aopending movie's ratings
    ratings = response['vote_average']
    details.append(ratings)

    return details


# This function helps to load similar movies through the movies dataframe, and loaded pickled data that consists of similarity vector
def recommend(movie):
    
    # Getting the index of a movie from the dataframe
    index_of_the_movie = movies[movies['titlelower'] == movie].index[0]

    # Creating a list consisting of a tuples with index of a movie, and their similarity scores
    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    # Sorting the above list with respect to similarity scores such that most similar movies are sorted first
    sorted_similar_movies = sorted(similarity_score, key = lambda x : x[1], reverse = True) 

    recommended_movies = []
    posters = []
    movie_details = []

    for i in sorted_similar_movies[1:n_recommendations+1]:
        index = i[0]
        # Accessing the id of a movie
        movie_id = movies.iloc[index]['id']
        selected_movie = movies.title.iloc[index]

        # Calling and appending the returned values of the functions developed
        recommended_movies.append([selected_movie, i[1]])
        posters.append(fetch_poster(movie_id))
        movie_details.append(fetch_details(movie_id))
    
    return recommended_movies, posters, movie_details


st.write("Data is retrieved through The Movie Database API. So, it is subjected to certain amount of error in data displayed.")

# When Submit button is pressed, the following code executes
if st.button('Submit'):
    st.write("Please Know that there are limited movies in the dataset used.")
    st.write(" ")
    st.write("Selected Movie: ",option)
    recommendations, posters_urls, details_list = recommend(option1)
    
    for i in range(n_recommendations):
        st.write(str(i+1)+". ",recommendations[i][0],'(',str(round(recommendations[i][1]*100,2)),'%)')

        # Poster of the movie
        image = "<img height = 400 width = 400 src = "+posters_urls[i]+">"
        st.markdown(image, unsafe_allow_html = True)

        # For an empty new line
        st.write(" ")

        # overview of the movie
        st.write(details_list[i][0])

        # Ratings
        text = 'Ratings : '+str(details_list[i][6])+ "/10"
        st.write(text)

        # Release date
        text = "Release Date: "+details_list[i][4]
        st.write(text)

        # Revenue
        text = "Box Office:  "+(details_list[i][3]) +" Millon USD"
        st.write(text)

        # Budget
        text = "Budget:  "+(details_list[i][2]) +" Millon USD"
        st.write(text)

        # Genres of the movie
        text = "Genre : "
        for j in details_list[i][1]:
            text += j+"/"
        st.write(text[:-1])

        # Homepage Url
        homepage = details_list[i][5]
        if (homepage != ""):
            text = "Homepage: "+homepage
        else:
            text = "Homepage: "+"Unavailable"
        st.write(text)
        
        # Two empty lines after every recommendations
        st.write(" ")
        st.write(" ")



#   Thank you
#   From Sujan Neupane (neupanesujan420@gmail.com)
    