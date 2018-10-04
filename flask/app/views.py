#!/usr/bin/python

import json
from flask import render_template			# used for input template
from app import app					# app located in __init__.py
from flask import request
from elasticsearch import Elasticsearch			# used for
#from flask.ext.reqarg import request_args

@app.route('/')
@app.route('/index')
def index():
   return render_template("simple.html")

es = Elasticsearch()
index="posts"

@app.route('/output')
def cesareans_output():
	error = request.args.get('ErrorLog')
	res = es.search(index=index, doc_type=index, body={'query': {'match_phrase': {'@Body': error}}},size = 500)
	links = [entries['_source']['@Id'] for entries in res['hits']['hits']]
	sites = ["https://stackoverflow.com/questions/" + str(link) for link in links]

	return render_template("output.html", births = sites)
