from urllib2 import Request, urlopen
import json
import time

class Movie:
    def __init__(self, raw_movie):
        self.title = raw_movie['title']
        self.id = raw_movie['id']
        self.poster = 'http://image.tmdb.org/t/p/w500' +  raw_movie['poster_path']
        self.overview = raw_movie['overview']
        self.date = raw_movie['release_date']
        self.genre = raw_movie['genre_ids']
        self.rating = raw_movie['vote_average']
        self.popularity = raw_movie['popularity']
        self.count = raw_movie['vote_count']
        self.weight = 0

    def update_score(self, count):
        self.score = 0.7 * self.weight / count + 0.2 * self.rating / 10 + 0.1 * self.popularity / 100

class Recommender:
    def __init__(self):
        self.Movies = {}
        self.checked = []
        self.call_count = 0
    # Acquire a list of movies based off of genre
    @staticmethod
    def generate_movies(genre, page):
        request = Request('http://api.themoviedb.org/3/genre/' + genre + '/movies?api_key=03bb4843dcfd206b47dc2872f71aa418&page=' + str(page))
        response_body = urlopen(request).read()
        return json.loads(response_body)

    # Adds total list of Movies
    def add_movies(self, raw_movies):
        for movie_index in raw_movies['results']:
            if movie_index['id'] not in self.Movies:
                self.Movies[movie_index['id']] = Movie(movie_index)

    # Updates the total list of Movies
    def update_movies(self, genre):
        for i in range(5):
            self.add_movies(self.generate_movies(genre, i+1))
        self.checked.append(genre)

    # Weighs the movies by genre based on user's input
    @staticmethod
    def weigh(movie, genre_first, genre_second):
        if genre_first in movie.genre:
            movie.weight += 1.
        elif genre_second in movie.genre:
            movie.weight += 0.5

    # Makes a list of objects from an input dictionary
    @staticmethod
    def list_from_dict(movie_map):
        arr = []
        for key, movie in movie_map.iteritems():
            arr.append(movie)
        return arr

    # New genre entry
    def new_entry(self, genre_first, genre_second):
        if genre_first not in self.checked:
            self.update_movies(str(genre_first))
            time.sleep(2)
        if genre_second not in self.checked:
            self.update_movies(str(genre_second))
            time.sleep(2)
        for key, movie in self.Movies.iteritems():
            self.weigh(movie, genre_first, genre_second)
        self.call_count += 1

    # Communicates with the flask files
    def read_input(self, arr):
        for dikt in arr:
            self.new_entry(dikt['genres'][0], dikt['genres'][1])

    # Final call from host, returns an array of sorted movies by score
    def final(self):
        arr_movies = self.list_from_dict(self.Movies)
        for movie in arr_movies:
            movie.update_score(self.call_count)
        sorted_movies = sorted(arr_movies, key=lambda movie: movie.score , reverse=True)
        return sorted_movies[0:10]
        # for movie in sorted_movies[0:30]:
        #     print(movie.title)
        #     print(movie.score)

# rc= Recommender()
# rc.new_entry(27, 28)
# rc.new_entry(18, 14)
# rc.new_entry(12, 18)
# rc.new_entry(10751, 14)
# rc.new_entry(28, 35)
# rc.new_entry(18, 28)
# rc.new_entry(18, 28)
# rc.new_entry(18, 28)
# rc.new_entry(18, 28)
# rc.final()
