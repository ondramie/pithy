#!/usr/bin/python

import json
from flask import render_template			# used for input template
from app import app							# app located in __init__.py
from flask import request
from elasticsearch import Elasticsearch	
import timeit	
#from flask.ext.reqarg import request_args

@app.route('/')
@app.route('/index')
def index():
   return render_template("index.html")

es = Elasticsearch()
index="posts"

@app.route('/output')
def output():
	error = request.args.get('ErrorLog') 
	# print type(error)
	#res = es.search(index=index, doc_type=index, body={'query': {'match_phrase': {'@Body': error}}},size = 500)
	print("hello")
	start = timeit.timeit()
	print(start)
	res = es.search(index=index, doc_type=index, body={"query": 
    {"match_phrase": {"Body": str(error)}}}, size=500) 
	links = [entries['_source']['_source']['Id'] for entries in res['hits']['hits']]
	print(timeit.timeit() - start)
	#print(links)
	sites = ("https://stackoverflow.com/questions/" + str(link) for link in links)

	return render_template("output.html", births = sites)
