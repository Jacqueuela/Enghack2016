from urllib2 import Request, urlopen
import json

Movies = {}
#weighted_movies = []
checked = []
call_count = 0

class Movie:
    def __init__(self, raw_movie):
        self.title = raw_movie['title']
        self.overview = raw_movie['overview']
        self.date = raw_movie['release_date']
        self.genre = raw_movie['genre_ids']
        self.rating = raw_movie['vote_average']
        self.popularity = raw_movie['popularity']
        self.count = raw_movie['vote_count']
        self.weight = 0
    @property
    def score(self):
        return 0.7 * self.weight / call_count + 0.2 * self.rating / 10 + 0.1 * self.popularity / 100


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
    for i in range(5):
        add_movies(generate_movies(genre, i+1))
    checked.append(genre)

def weigh(movie, genre_first, genre_second):
    if genre_first in movie.genre:
        movie.weight += 1.
    elif genre_second in movie.genre:
        movie.weight += 0.5

def list_from_dict(dict):
    arr = []
    for key, movie in dict.iteritems():
        arr.append(movie)
    return arr

def new_entry(genre_first, genre_second):
    if genre_first not in checked:
        update_movies(str(genre_first))
    if genre_second not in checked:
        update_movies(str(genre_second))
    for key, movie in Movies.iteritems():
        weigh(movie, genre_first, genre_second)
    global call_count
    call_count += 1

def read_input(arr):
    for dikt in arr:
        new_entry(dikt['genres'][0], dikt['genres'][1])

def final():
    arr_movies = list_from_dict(Movies)
    sorted_movies = sorted(arr_movies, key=lambda movie: movie.score, reverse=True)
    for movie in sorted_movies[0:30]:
        print(movie.title)
        print(movie.score)

new_entry(27, 28)
new_entry(18, 27)
final()
