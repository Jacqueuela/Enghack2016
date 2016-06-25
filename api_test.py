from urllib2 import Request, urlopen
import json

Movies = {}

class Movie:
    def __init__(self, raw_movie):
        self.title = raw_movie['title']
        self.overview = raw_movie['overview']
        self.date = raw_movie['release_date']
        self.genre = raw_movie['genre_ids']
        self.popularity = raw_movie['popularity']
        self.rating = raw_movie['vote_average']

# Acquire a list of movies based off of genre
def generate_movies(genre, page):
    request = Request('http://api.themoviedb.org/3/genre/' + genre + '/movies?api_key=03bb4843dcfd206b47dc2872f71aa418&page=' + str(page))
    response_body = urlopen(request).read()
    return json.loads(response_body)

# Adds total list of Movies
def add_movies(raw_movies):
    #keys = ['id', 'title', 'overview', 'release_date', 'genre_ids', 'popularity', 'vote_average']
    for movie_index in raw_movies['results']:
        if movie_index['id'] not in Movies:
            Movies[movie_index['id']] = Movie(movie_index)

# Updates the total list of Movies
def update_movies(genre):
    for i in range(10):
        add_movies(generate_movies(genre, i+1))

update_movies('18')
for movie in Movies:
    print(Movies[movie].title)

print("="*60)

update_movies('12')
for movie in Movies:
    print(Movies[movie].title)
