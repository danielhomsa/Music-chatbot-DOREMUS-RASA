# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
from SPARQLWrapper import SPARQLWrapper, JSON

logger = logging.getLogger(__name__)


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text)  # make an api call
        joke = request['value']  # extract a joke from returned json response
        dispatcher.utter_message(joke)  # send the message back to the user
        return []

class ActionWorksBy(Action):
	def name(self):
		return "action_works_by"

	def run(self, dispatcher, tracker, domain):
		number = tracker.get_slot('number')
		artist = tracker.get_slot('doremus-artist')
		# # Split artist name to capitalize name
		# artist_name = artist.split(" ")
		# for index, name in enumerate(artist_name):
		# 	artist_name[index] = name.capitalize()
		# cap_artist = " ".join(artist_name)
		# Query to get works by artist and limited by number
		sparql = SPARQLWrapper("http://data.doremus.org/sparql")
		sparql.setQuery("""PREFIX mus: <http://data.doremus.org/ontology#> 
							PREFIX ecrm: <http://erlangen-crm.org/current/>
    						PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
    						PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    						SELECT DISTINCT ?expression SAMPLE(?title) as ?title
    						WHERE {
    						?expression a efrbroo:F22_Self-Contained_Expression ;
              				rdfs:label ?title .
      						?expCreation efrbroo:R17_created ?expression ;
              				ecrm:P9_consists_of / ecrm:P14_carried_out_by ?composer .
      						?composer foaf:name \"""" + artist + """\"
    						} ORDER BY rand() LIMIT """ + str(number))
		# Converting the response to json format
		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()
		# Obtaining the works from json
		works = []
		for work in results["results"]["bindings"]:
			works.append(work["title"]["value"])
		# print(works)
		# Sending message to user
		dispatcher.utter_message("\n".join(works))
		return []
