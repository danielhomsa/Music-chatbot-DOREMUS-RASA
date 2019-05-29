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
import parsedatetime
from datetime import datetime
from time import mktime
import pendulum
from difflib import get_close_matches
from difflib import SequenceMatcher

logger = logging.getLogger(__name__)

# Computing the similarity of an artist name with the artists in the file 
# if it is not found in the artists file
# The search ends if the similarity is above 0.8 or when reaching the end of the file
def similarArtist(artist, dispatcher):
	similarity_ratio = 0.0
	artist_name = ""
	dispatcher.utter_message("Sorry, I couldn't find the artist you requested")
	with open("artists.json") as art_json:
		artists = json.load(art_json)
		for a in artists['results']['bindings']:
			artist_name = a['names']['value'].lower()
			close_match = get_close_matches(artist, artist_name.split())
			if(len(close_match) >= 1):
				sequence_ratio = SequenceMatcher(None, artist, close_match[0]).ratio()
				if(sequence_ratio > similarity_ratio):
					artist_value = a['composer']['value']
					artist_name = a['names']['value'].split("|")
					similarity_ratio = sequence_ratio
					if(similarity_ratio >= 0.8):
						break
		dispatcher.utter_message("If you meant " + artist_name[0] +
								" I found this: ")
	return artist_value

# Computing the similarity of a genre with the genres in the file 
# if it is not found in the genres file
# The search ends if the similarity is above 0.8 or when reaching the end of the file
def similarGenre(genre, dispatcher):
	similarity_ratio = 0.0
	dispatcher.utter_message("Sorry, I couldn't find the genre you requested")
	with open("genres.json") as gen_json:
		genres = json.load(gen_json)
		for g in genres['results']['bindings']:
			genre_name = g['gen']['value'].lower()
			close_match = get_close_matches(genre, genre_name.split("|"))
			if(len(close_match) >= 1):
				genre_ratio = SequenceMatcher(None, genre, close_match[0]).ratio()
				if(genre_ratio > similarity_ratio):
					genre_value = g['genres']['value']
					similarity_ratio = genre_ratio
					if(similarity_ratio >= 0.8):
						break
		dispatcher.utter_message("I guess you meant " + close_match[0])
	return genre_value

# Computing the similarity of an instrument name with the instruments in the file 
# if it is not found in the instruments file
# The search ends if the similarity is above 0.8 or when reaching the end of the file
def similarInstrument(instrument, dispatcher):
	similarity_instr = 0.0
	dispatcher.utter_message("Sorry, I couldn't find the instrument you requested")
	with open("instruments.json") as instr_json:
		instruments = json.load(instr_json)
		for i in instruments['results']['bindings']:
			instrument_name = i['instruments']['value'].lower()
			close_match = get_close_matches(instrument, instrument_name.split("|"))
			if(len(close_match) >= 1):
				instr_ratio = SequenceMatcher(None, instrument, close_match[0]).ratio()
				if(instr_ratio > similarity_instr):
					instrument_value = i['composer']['value']
					similarity_instr = instr_ratio
					if(similarity_instr >= 0.8):
						break
		dispatcher.utter_message("I guess you meant " + close_match[0])
	return instrument_value

# Function for resetting the slots
class ResetSlot(Action):

    def name(self):
        return "action_reset_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("doremus-instrument", None),SlotSet("doremus-genre", None),SlotSet("date-period", None)]

# Custom slot used in the find performance action
class ActionTimeTest(Action):
	def name(self):
		return "action_time_test"

	def run(self, dispatcher, tracker, domain):
		# Retrieving the entities from the last message
		entities = tracker.latest_message['entities']
		time_value = ""
		start_day = ""
		end_day = ""
		time_grain = ""
		for e in entities:
			# Verifying if the extracted entity is from the duckling extractor and if it is a time entity
			if(e['extractor'] == 'ner_duckling_http' and e['entity'] == 'time'):
				time_value = e['value']
				# If the extracted value contains only 1 date, an ending date has to be computed
				if(isinstance(time_value, str)):
					time_grain = e['additional_info']['grain']
					start_day = pendulum.parse(time_value)
					if(time_grain == "week"):
						end_day = start_day.add(weeks=1)
					elif(time_grain == "month"):
						end_day = start_day.add(months=1)
					elif(time_grain == "year"):
						end_day = start_day.add(years=1)
				# If the extracted value is a range its values are saved
				if(isinstance(time_value, dict)):
					start_day = time_value['from']
					end_day = time_value['to']
		# Values for the slot 'date-period'
		date_range = {'from':str(start_day).split("T")[0], 'to':str(end_day).split("T")[0]}
		return[SlotSet('date-period', date_range)]

# Custom slot used in the works by and find artist actions
class ActionYearExtractionSlot(Action):
	def name(self):
		return "action_year_slot"

	def run(self, dispatcher, tracker, domain):
		# Retrieving the entities from the last message
		entities = tracker.latest_message['entities']
		entity_value = {}
		years = []
		for e in entities:
			# Verifying if the extracted entity is from the duckling extractor and if it is a time entity
			if(e['extractor'] == 'ner_duckling_http' and e['entity'] == 'time'):
				# Extracting the years values
				years = [int(date) for date in e['text'].split() if date.isdigit()]
				# If the extraction returns a string it is not an interval of dates
				if(isinstance(e['value'], str)):
					entity_value = {"not interval": years[0]}
				# If the extraction returns a dictionary it is a range of dates
				elif(isinstance(e['value'], dict)):
					if(e['value']['to'] == None):
						entity_value = {"to": None, "from": years[0]}
					elif(e['value']['from'] == None):
						entity_value = {"to": years[0], "from": None}
					else:
						entity_value = {"to": max(years), "from": min(years)}
		# The date(s) values are returned to the slot
		return [SlotSet('date-period', entity_value)]

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

# Function to do query by artist, genre, instrument and/or filter by year
# Artists, instruments and genres values are retrieved from their respective json files, according to their names/labels
class ActionWorksBy(Action):
	def name(self):
		return "action_works_by"

	def run(self, dispatcher, tracker, domain):
		number = tracker.get_slot('number')
		artist = tracker.get_slot('doremus-artist')
		instrument = tracker.get_slot('doremus-instrument')
		date_period = tracker.get_slot('date-period')
		genre = tracker.get_slot('doremus-genre')
		artist_value = ""
		instrument_value = ""
		genre_value = ""
		sparql = SPARQLWrapper("http://data.doremus.org/sparql")
		query = """PREFIX mus: <http://data.doremus.org/ontology#> 
							PREFIX ecrm: <http://erlangen-crm.org/current/>
    						PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
    						PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    						SELECT SAMPLE(?title) AS ?title, SAMPLE(?artist) AS ?artist,
                			SAMPLE(?comp) AS ?year, SAMPLE(?genre) AS ?genre,
                  			SAMPLE(?comment) AS ?comment, SAMPLE(?key) AS ?key
    						WHERE {
      						?expression a efrbroo:F22_Self-Contained_Expression ;
        					rdfs:label ?title ;
        					rdfs:comment ?comment ;
        					mus:U13_has_casting ?casting ;
        					mus:U12_has_genre ?gen .
      						?expCreation efrbroo:R17_created ?expression ;
        					ecrm:P4_has_time-span ?ts ;
        					ecrm:P9_consists_of / ecrm:P14_carried_out_by ?composer .
      						?composer foaf:name ?artist .
      						?gen skos:prefLabel ?genre .
      						OPTIONAL {
        					?ts time:hasEnd / time:inXSDDate ?comp
      						}
      						OPTIONAL {
        					?expression mus:U11_has_key ?k .
        					?k skos:prefLabel ?key
      						} . """
		if(artist):
			print(artist, " artist")
			with open("artists.json") as art_json:
				artists = json.load(art_json)
				for a in artists['results']['bindings']:
					artist_name = a['names']['value'].lower()
					if(artist in artist_name):
						artist_value = a['composer']['value']
						break
				if(artist_value == ""):
					artist_value = similarArtist(artist, dispatcher)
			query += """VALUES(?composer) {
                   (<""" + artist_value + """>)
                 }"""
		if(genre):
			print(genre, " genre")
			with open("genres.json") as gen_json:
				genres = json.load(gen_json)
				for g in genres['results']['bindings']:
					genre_name = g['genres']['value'].lower()
					if(genre in genre_name):
						genre_value = g['gen']['value']
						break
				if(genre_value == ""):
					genre_value = similarGenre(genre, dispatcher)
			query += """VALUES(?gen) {
                   (<""" + genre_value + """>)
                 }"""
		if(instrument):
			print(instrument, " instrument")
			with open("instruments.json") as instr_json:
				instruments = json.load(instr_json)
				for i in instruments['results']['bindings']:
					instrument_name = i['instruments']['value'].lower()
					if(instrument in instrument_name):
						instrument_value = i['instr']['value']
						break
				if(instrument_value == ""):
					instrument_value = similarInstrument(instrument, dispatcher)
			query += """?casting mus:U23_has_casting_detail ?castingDetail . 
                 ?castingDetail mus:U2_foresees_use_of_medium_of_performance / skos:exactMatch* ?instrument . 
                 VALUES(?instrument) {
                   (<""" + instrument_value + """> )
                 }"""
		print(date_period)
		if(date_period):
			print(date_period)
			if(len(date_period) == 1):
				query += """FILTER ( ?comp = \"""" + str(date_period['not interval']) + """\"^^xsd:gYear ) . """
			else:
				if(date_period['to'] == None):
					query += """FILTER ( ?comp >= \"""" + str(date_period['from']) + """\"^^xsd:gYear ) . """
				elif(date_period['from'] == None):
					query += """FILTER ( ?comp <= \"""" + str(date_period['to']) + """\"^^xsd:gYear ) . """
				else:
					query += """FILTER ( ?comp >= \"""" + str(date_period['from']) + """\"^^xsd:gYear 
					AND ?comp <= \" """ + str(date_period['to']) + """\"^^xsd:gYear) . """
		sparql.setQuery(query + """ } GROUP BY ?expression ORDER BY rand() LIMIT """ + str(number))
		# Converting the response to json format
		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()
		# Obtaining the works from json
		works = []
		for work in results["results"]["bindings"]:
			works.append(work["title"]["value"])
		print(date_period)
		# Sending message to user
		if(len(works) == 0):
			dispatcher.utter_message("Sorry, I couldn't find any works with these filters")
		else:
			dispatcher.utter_message("\n".join(works))
		return []

# Action to discover a specific artist, using the value from the json file
class ActionDiscoverArtist(Action):
	def name(self):
		return "action_discover_artist"

	def run(self, dispatcher, tracker, domain):
		artist = tracker.get_slot('doremus-artist')
		artist_value = ""
		if(artist):
			print(artist, " artist")
			with open("artists.json") as art_json:
				artists = json.load(art_json)
				for a in artists['results']['bindings']:
					artist_name = a['names']['value'].lower()
					if(artist in artist_name):
						artist_value = a['composer']['value']
						break
		if(artist_value == ""):
			artist_value = similarArtist(artist, dispatcher)
		sparql = SPARQLWrapper("http://data.doremus.org/sparql")
		query = """	PREFIX mus: <http://data.doremus.org/ontology#> 
					PREFIX ecrm: <http://erlangen-crm.org/current/>
    				PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
    				PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    				SELECT ?name,
                    ?bio,
                    xsd:date(?d_date) AS ?death_date,
                    ?death_place,
                    xsd:date(?b_date) AS ?birth_date,
                    ?birth_place,
                    ?image
                    WHERE {
                      VALUES(?composer) {(<""" + artist_value + """>)} .
                      ?composer rdfs:comment ?bio ;
                        foaf:depiction ?image ;
                        schema:deathDate ?d_date ;
                        foaf:name ?name ;
                        dbpprop:deathPlace ?d_place ;
                        schema:birthDate ?b_date ;
                        dbpprop:birthPlace ?b_place .
                      OPTIONAL { ?d_place rdfs:label ?death_place } .
                      OPTIONAL { ?b_place rdfs:label ?birth_place } .
                      FILTER (lang(?bio) = "en")
                    }
    			"""
		sparql.setQuery(query)
		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()
		artist_bindings = results['results']['bindings']
		artist_name = ""
		artist_bio = ""
		artist_birth_place = "-"
		artist_death_place = "-"
		artist_death = ""
		if(len(artist_bindings) == 0):
			dispatcher.utter_message("Sorry, I couldn't find the biography of the artist")
		else:
			artist_result = artist_bindings[0]
			artist_name = artist_result['name']['value']
			artist_bio = artist_result['bio']['value']
			if(artist_result['birth_place']):
				artist_birth_place = artist_result['birth_place']['value']
			if(artist_result['death_place']):
				artist_death_place = artist_result['death_place']['value']
			artist_death = artist_result['death_date']['value']
			dispatcher.utter_message(artist_name + "\n" + artist_bio + "\n" + 
									"Birth place: " + artist_birth_place + "\n" + 
									"Death place: " + artist_death_place + "\n" +
									"Death date: " + artist_death)
		return []

# Action corresponding to the find performance intent
# Recieves a custom slot from the ActionTimeTest function
class ActionFindPerformance(Action):
	def name(self):
		return "action_find_performance"

	def run(self, dispatcher, tracker, domain):
		cal = parsedatetime.Calendar()
		date = tracker.get_slot('date-period')
		city = tracker.get_slot('geo-city')
		number = tracker.get_slot('number')
		if(number == None):
			number = 1
		start_day = date['from']
		end_day = date['to']
		sparql = SPARQLWrapper("http://data.doremus.org/sparql")
		query = """PREFIX mus: <http://data.doremus.org/ontology#> 
					PREFIX ecrm: <http://erlangen-crm.org/current/>
    				PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
    				PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
					SELECT SAMPLE(?title) AS ?title, SAMPLE(?subtitle) AS ?subtitle,
                    SAMPLE(?actorsName) AS ?actorsName, SAMPLE(?placeName) AS ?placeName, SAMPLE(?date) AS ?date
                  WHERE {
                    ?performance a mus:M26_Foreseen_Performance ;
                      ecrm:P102_has_title ?title ;
                      ecrm:P69_has_association_with / mus:U6_foresees_actor ?actors ;
                      mus:U67_has_subtitle ?subtitle ;
                      mus:U7_foresees_place_at / ecrm:P89_falls_within* ?place ;
                      mus:U8_foresees_time_span ?ts .
                    ?place rdfs:label ?placeName .
                    ?actors rdfs:label ?actorsName .
                    ?ts time:hasBeginning / time:inXSDDate ?time ;
                       rdfs:label ?date .
					FILTER ( ?time >= '""" + start_day + """'^^xsd:date 
					AND ?time <= '""" + end_day + """'^^xsd:date) . """
		if(city):
			query += """FILTER ( contains(lcase(str(?placeName)), \"""" + city + """\") )"""
		sparql.setQuery(query + """} GROUP BY ?performance
               		ORDER BY rand()
               		LIMIT """ + str(number))
		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()
		performances_results = results['results']['bindings']
		performances = []
		if(len(performances_results) == 0):
			dispatcher.utter_message("Sorry, I couldn't find a performance in that date")
		else:
			for p in performances_results:
				performances.append(p['title']['value'] + "\n" + p['subtitle']['value'] +
					"\n" + p['placeName']['value'] + "\n" + p['actorsName']['value'] +
					"\n" + p['date']['value'] + "\n\n")
			dispatcher.utter_message("\n\n".join(performances))
		print(start_day)
		print(date, " date")
		print(city, " city")
		print(number, " number")
		return []

# Action to find an artist according to the genre, instruments, date period when was born and/or city where was born
class ActionFindArtist(Action):
	def name(self):
		return "action_find_artist"

	def run(self, dispatcher, tracker, domain):
		number = tracker.get_slot('number')
		instrument = tracker.get_slot('doremus-instrument')
		date_period = tracker.get_slot('date-period')
		genre = tracker.get_slot('doremus-genre')
		city = tracker.get_slot('geo-city')
		instrument_value = ""
		genre_value = ""
		print(tracker.latest_message['entities'])
		sparql = SPARQLWrapper("http://data.doremus.org/sparql")
		query = """PREFIX mus: <http://data.doremus.org/ontology#> 
							PREFIX ecrm: <http://erlangen-crm.org/current/>
    						PREFIX efrbroo: <http://erlangen-crm.org/efrbroo/>
    						PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    				SELECT SAMPLE(?name) AS ?name, count(distinct ?expr) AS ?count,
                    SAMPLE(xsd:date(?d_date)) AS ?death_date, SAMPLE(?death_place) AS ?death_place,
                    SAMPLE(xsd:date(?b_date)) AS ?birth_date, SAMPLE(?birth_place) AS ?birth_place
                  	WHERE {
                    ?composer foaf:name ?name .
                    ?composer schema:deathDate ?d_date .
                    ?composer dbpprop:deathPlace ?d_place .
                    OPTIONAL { ?d_place rdfs:label ?death_place } .
                    ?composer schema:birthDate ?b_date .
                    ?composer dbpprop:birthPlace ?b_place .
                    OPTIONAL { ?b_place rdfs:label ?birth_place } .
                    ?exprCreation efrbroo:R17_created ?expr ;
                      ecrm:P9_consists_of / ecrm:P14_carried_out_by ?composer .
                    ?expr mus:U12_has_genre ?gen ;
                      mus:U13_has_casting ?casting . """
		if(genre):
			print(genre, " genre")
			with open("genres.json") as gen_json:
				genres = json.load(gen_json)
				for g in genres['results']['bindings']:
					genre_name = g['genres']['value'].lower()
					if(genre in genre_name):
						genre_value = g['gen']['value']
						break
				if(genre_value == ""):
					genre_value = similarGenre(genre, dispatcher)
			query += """VALUES(?gen) {
                   (<""" + genre_value + """>)
                 }"""
		if(instrument):
			print(instrument, " instrument")
			with open("instruments.json") as instr_json:
				instruments = json.load(instr_json)
				for i in instruments['results']['bindings']:
					instrument_name = i['instruments']['value'].lower()
					if(instrument in instrument_name):
						instrument_value = i['instr']['value']
						break
				if(instrument_value == ""):
					instrument_value = similarInstrument(instrument, dispatcher)
			query += """?casting mus:U23_has_casting_detail ?castingDetail . 
                 ?castingDetail mus:U2_foresees_use_of_medium_of_performance / skos:exactMatch* ?instrument . 
                 VALUES(?instrument) {
                   (<""" + instrument_value + """> )
                 }"""
		if(date_period):
			print(date_period)
			if(len(date_period) == 1):
				query += """FILTER ( ?b_date = \"""" + str(date_period['not interval']) + """\"^^xsd:date ) . """
			else:
				if(date_period['to'] == None):
					query += """FILTER ( ?b_date >= \"""" + str(date_period['from']) + """\"^^xsd:date ) . """
				elif(date_period['from'] == None):
					query += """FILTER ( ?b_date <= \"""" + str(date_period['to']) + """\"^^xsd:date ) . """
				else:
					query += """FILTER ( ?b_date >= \"""" + str(date_period['from']) + """\"^^xsd:date 
					AND ?b_date <= \" """ + str(date_period['to']) + """\"^^xsd:date) . """
		if(city):
			query += """FILTER ( contains(lcase(str(?birth_place)), \"""" + city + """\") )"""
		sparql.setQuery(query + """ } GROUP BY ?composer ORDER BY DESC(?count) LIMIT """ + str(number))
		# Converting the response to json format
		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()
		artists_results = results['results']['bindings']
		print(artists_results)
		artists = []
		artist_name = ""
		artist_bio = ""
		artist_birth_place = "-"
		artist_death_place = "-"
		artist_death = ""
		count_value = ""
		if(len(artists_results) == 0):
			dispatcher.utter_message("Sorry, I didn't find anything")
		else:
			for a in artists_results:
				artist_name = a['name']['value']
				artist_bdate = a['birth_date']['value']
				if(a['birth_place']):
					artist_birth_place = a['birth_place']['value']
				artist_ddate = a['death_date']['value']
				if(a['death_place']):
					artist_death_place = a['death_place']['value']
				artist_death = a['death_date']['value']
				count_value = a['count']['value']
				artists.append(artist_name + "\n" +
										"Birth date: " + artist_bdate + " " +
										"Birth place: " + artist_birth_place + "\n" + 
										"Death date: " + artist_ddate + " " +
										"Death place: " + artist_death_place + "\n" +
										"Death date: " + artist_death + "\n" +
										"Number of works: " + count_value + "\n\n")
			dispatcher.utter_message("\n\n".join(artists))
		return []
