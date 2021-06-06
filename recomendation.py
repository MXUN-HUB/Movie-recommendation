import pandas as pd
from math import sqrt
import numpy as np
import substring


movies_df = pd.read_csv('./dataset/movies_df.csv')
ratings_df = pd.read_csv('./dataset/ratings.csv')  
moviesWithGenres_df = pd.read_csv('./dataset/moviesWithGenres.csv')


def predict(userInput, q):
    inputMovies = pd.DataFrame(userInput)
    inputId = movies_df[movies_df['title'].isin(inputMovies['title'].tolist())]

    inputMovies = pd.merge(inputId, inputMovies)
    inputMovies = inputMovies.drop('genres', 1).drop('year', 1)

    userMovies = moviesWithGenres_df[moviesWithGenres_df['movieId'].isin(inputMovies['movieId'].tolist())]
    userMovies = userMovies.reset_index(drop=True)

    userGenreTable = userMovies.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)

    userProfile = userGenreTable.transpose().dot(inputMovies['rating'])

    genreTable = moviesWithGenres_df.set_index(moviesWithGenres_df['movieId'])
    genreTable = genreTable.drop('movieId', 1).drop('title', 1).drop('genres', 1).drop('year', 1)

    recommendationTable_df = ((genreTable*userProfile).sum(axis=1))/(userProfile.sum())
    recommendationTable_df = recommendationTable_df.sort_values(ascending=False)

    x = movies_df.loc[movies_df['movieId'].isin(recommendationTable_df.head(int(q)).keys())]
    x = x['title']

    a = []
    for i in x:
        a.append(i)
    return a



def searchds(k):
    x = movies_df
    title = x['title']
    for j in title:
        if k == j:
            return "Found"
    return "Not found"