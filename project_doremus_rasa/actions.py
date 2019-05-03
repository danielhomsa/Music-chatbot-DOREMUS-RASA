# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from rasa_core_sdk.events import SlotSet

import logging
import requests
import json
from rasa_core_sdk import Action
from SPARQLWrapper import SPARQLWrapper, JSON

logger = logging.getLogger(__name__)

class ResetSlot(Action):

    def name(self):
        return "action_reset_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("doremus-instrument", None)]

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
		instrument = tracker.get_slot('doremus-instrument')
		date_period = tracker.get_slot('date-period')
		artist_value = ""
		instrument_value = ""
		# # Split artist name to capitalize name
		# artist_name = artist.split(" ")
		# for index, name in enumerate(artist_name):
		# 	artist_name[index] = name.capitalize()
		# cap_artist = " ".join(artist_name)
		# Query to get works by artist and limited by number
		sparql = SPARQLWrapper("http://data.doremus.org/sparql")
		query = """PREFIX mus: <http://data.doremus.org/ontology#> 
							PREFIX ecrm: <http://erlangen-crm.org/current/>
    						PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
    						PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    						SELECT DISTINCT ?expression SAMPLE(?title) as ?title
    						WHERE {
    						?expression a efrbroo:F22_Self-Contained_Expression ;
              				rdfs:label ?title .
      						?expCreation efrbroo:R17_created ?expression ;
              				ecrm:P9_consists_of / ecrm:P14_carried_out_by ?composer .
      						?composer foaf:name ?artist """
		if(artist):
			print(instrument)
			with open("artists.json") as art_json:
				artists = json.load(art_json)
				for a in artists['results']['bindings']:
					artist_name = a['names']['value'].lower()
					if(artist in artist_name):
						artist_value = a['composer']['value']
						break
			query += """VALUES(?composer) {
                   (<""" + artist_value + """>)
                 }"""
		if(instrument):
			print(instrument)
			with open("instruments.json") as instr_json:
				instruments = json.load(instr_json)
				for i in instruments['results']['bindings']:
					instrument_name = i['instruments']['value'].lower()
					if(instrument in instrument_name):
						instrument_value = i['instr']['value']
						break
			# query += """?expression mus:U13_has_casting / mus:U23_has_casting_detail / mus:U2_foresees_use_of_medium_of_performance ?mop .
			# ?mop skos:prefLabel \"""" + instrument + """\" . """
			query += """?casting mus:U23_has_casting_detail ?castingDetail . 
                 ?castingDetail mus:U2_foresees_use_of_medium_of_performance / skos:exactMatch ?instrument . 
                 VALUES(?instrument) {
                   (<""" + instrument_value + """> )
                 }
               """
		sparql.setQuery(query + """ } ORDER BY rand() LIMIT """ + str(number))
		# Converting the response to json format
		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()
		# Obtaining the works from json
		works = []
		for work in results["results"]["bindings"]:
			works.append(work["title"]["value"])
		# print(works)
		# Sending message to user
		print(date_period)
		dispatcher.utter_message("\n".join(works))
		return []
