from flask import Flask, json, jsonify, render_template
from flask.ext.api import FlaskAPI
from flask.ext.api.decorators import set_parsers
from flask import request
from flask.ext.api.parsers import JSONParser
from GenreMap import Genre_Map
#import api_test
app = Flask(__name__)
#Get JSON from Front end
#@app.route("""Form""", methods['GET'])

# @set_parsers(JSONParser)
# def form_input():
# 	return {'request data':request.data}
genre_list = Genre_Map()
store_datum = []
genres = []
Genre = []
def format(dinosaur): #Error checking done here as well
	# if """Not 2 genres error out""":
	# 	"""Error out"""	pass
	# # else if """length value isn't at least 1 hour""":
	# # 	"""Error out""" pass
	# else:
	store_datum.append(dinosaur)

	genres.append(dinosaur['genre1']) 
	genres.append(dinosaur['genre2'])
	
	Genre = [genre_list.map[genres[0]], genre_list.map[genres[1]]]
	print Genre 
	return Genre

@app.route("/Store", methods=['POST'])
def store_data():
	
	
	format(request.json)
	
	return jsonify({"Response" : "Entry Added"})



"""Waits until Final request Before sending"""

@app.route("/Suggestions", methods=['GET'])
def find_suggestions():
	#Pass in the array to Leo
	return jsonify(Suggestions)
	
# @app.route("""/Output page""", methods=['POST'])
# def give_suggestions():
