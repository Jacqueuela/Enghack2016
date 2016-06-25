from urllib2 import Request, urlopen
import json

class Movie:
    def __init__(self, raw_movie):
        self.title = raw_movie['title']
        self.overview = raw_movie['overview']
        self.date = raw_movie['release_date']
        self.genre = raw_movie['genre_ids']
        self.popularity = raw_movie['popularity']
        self.rating = raw_movie['vote_average']

Movies = {}

# Acquire a list of movies based off of genre
def get_movies(genre):
    request = Request('http://api.themoviedb.org/3/genre/' + genre + '/movies?api_key=03bb4843dcfd206b47dc2872f71aa418')
    response_body = urlopen(request).read()
    return json.loads(response_body)

# Updates the total list of Movies
def update_movies(raw_movies):
    #keys = ['id', 'title', 'overview', 'release_date', 'genre_ids', 'popularity', 'vote_average']
    for movie_index in raw_movies['results']:
        Movies[movie_index['id']] = Movie(movie_index)


raw = get_movies('18')
update_movies(raw)
for movie in Movies:
    print(Movies[movie].title)
