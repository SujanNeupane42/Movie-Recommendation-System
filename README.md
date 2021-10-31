# Movie-Recommendation-System
![Python](https://img.shields.io/badge/Python-3.9.2-blueviolet)
![Scikit learn](https://img.shields.io/badge/sklearn-0.24.2-red)
![Numpy](https://img.shields.io/badge/Numpy-1.19.5-green)
![Pandas](https://img.shields.io/badge/Pandas-1.3.3-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.1.0-red)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.3.4-white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11.1-pink)

This is a simple Movie recommendation system. I have used following python libraries: numpy, matplotlib, seaborn, and sklearn. 


The dataset contains various features lke budget,	genres,	homepage,	id,	keywords,	original_language,	original_title,	overview,	popularity,	runtime	spoken_languages,	status, tagline,	title,	vote_average,	vote_count,	cast,	crew,	director

The dataset can also be found in `Kaggle`. However, I have added the csv files in the respository. The link to Kaggle dataset is https://www.kaggle.com/rounakbanik/the-movies-dataset.

I have performed the following steps in the jupyter notebook:
  1. Loading the data- I have used pandas library to load all the csv files.
  2. Selecting certain features: genres, keywords, cast, and director.
  3. Creating a series by combining the features
  4. Using CountVectorizer to learn vocabulary from the resultant series.
  5. Using Cosine Similarity
  6. Finally, by using similarity scores of a movie with all other movies, the movies with highest similarity are recommended to the user.


# Heroku
Then, I used streamlit to create a proper and appealing GUI ,which I deployed using Heroku Platform.

# The Movies Database API
In the streamlit/python file, I have used Spotify the moviesdb `API` to get thumbnail, url, title, and other details of the selected and recommended movies.

This is a simple content-based Movie Recommendation System that recommends Movies to the user based on genres, actors, directors etc.
