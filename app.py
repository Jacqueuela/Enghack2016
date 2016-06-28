from flask import Flask, json, jsonify
from flask_cors import CORS
from flask import request
from GenreMap import Genre_Map
from api_test import Recommender
from api_test import Movie

app = Flask(__name__)
CORS(app)

rc = Recommender()
genre_list = Genre_Map()
final_list = []


def format(input_dict):
	genres = []
	first_bool = False
	second_bool = False
	if input_dict['genre2'] is not None and input_dict['genre1'].lower() in genre_list.map:
		genres.append(input_dict['genre1'])
		first_bool = True
	if input_dict['genre2'] is not None and input_dict['genre2'].lower() in genre_list.map:
		genres.append(input_dict['genre2'])
		second_bool = True
	if first_bool and second_bool:
		return [genre_list.map[genres[0].lower()], genre_list.map[genres[1].lower()]]
	else:
		return None

@app.route("/Store", methods=['POST'])
def store_data():
        formatted_data = format(request.get_json())
        if formatted_data is None:
            return jsonify({"Response": "Incorrect Genres"})
	final_list.append(format(request.get_json()))
	return jsonify({"Response" : "Entry Added"})

"""Waits until Final request Before sending"""

@app.route("/Suggestions", methods=['GET'])
def find_suggestions():
	index = 0
	#Pass in the array to Leo
	a = []
	for user_input in final_list:
		rc.new_entry(user_input[0], user_input[1])

	print(final_list)
	for movie in rc.final():
		a.append({'title':movie.title, 'overview':movie.overview, 'rating':movie.rating, 'id':movie.id, 'poster':movie.poster, "genres" : movie.genre})
	global Genre
	global final_list
	Genre = []
	final_list = []
	return jsonify({"movies":a})
