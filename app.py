from flask import Flask, json, jsonify, render_template
from flask.ext.api import FlaskAPI
from flask.ext.api.decorators import set_parsers
from flask import request
from flask.ext.api.parsers import JSONParser
from GenreMap import Genre_Map
from api_test import Recommender
from api_test import Movie
from flask.ext.cors import CORS
app = Flask(__name__)
CORS(app)
#Get JSON from Front end
#@app.route("""Form""", methods['GET'])

# @set_parsers(JSONParser)
# def form_input():
# 	return {'request data':request.data}
rc = Recommender()
genre_list = Genre_Map()

Genre = []
final_list = []


def format(input_dict): #Error checking done here as well
	genres = []
	genres.append(input_dict['genre1'])
	genres.append(input_dict['genre2'])
	Genre = [genre_list.map[genres[0].lower()], genre_list.map[genres[1].lower()]]
	return Genre

@app.route("/Store", methods=['POST'])
def store_data():
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
