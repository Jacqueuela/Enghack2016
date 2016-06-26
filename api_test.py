from urllib2 import Request, urlopen
import json

Movies = {}
weighted_movies = []

#genre_first = input("Please input first choice genre: ")
#genre_second = input("Please input second choice genre: ")

class Movie:
    def __init__(self, raw_movie):
        self.title = raw_movie['title']
        self.overview = raw_movie['overview']
        self.date = raw_movie['release_date']
        self.genre = raw_movie['genre_ids']
        self.popularity = raw_movie['popularity']
        self.rating = raw_movie['vote_average']
        self.count = raw_movie['vote_count']
        self.weight = 2 * self.rating * self.count / 1000 + self.popularity


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
    for i in range(20):
        add_movies(generate_movies(genre, i+1))

def weigh(movie):
    if genre_first in movie.genre:
        movie.weight += 10.
    elif genre_second in movie.genre:
        movie.weight += 5.

def make_list():
    for key, movie in Movies.iteritems():
        weighted_movies.append(movie)

def sort_by_weight():
    return sorted(weighted_movies, key=lambda movie: movie.weight, reverse=True)

update_movies('18')
#print("=" * 60)

update_movies('12')

#print("=" * 60)

make_list()
for movie in range(10):
    print(weighted_movies[movie].title)

print("=" * 60)

weighted_movies = sort_by_weight()
for movie in range(10):
    print(weighted_movies[movie].title)
