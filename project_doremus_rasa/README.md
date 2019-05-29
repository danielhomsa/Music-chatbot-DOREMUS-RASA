# Classical Music Chatbot with DOREMUS and RASA

This chatbot is based on the RASA Stack starter-pack obtained from this repo:

```
git clone https://github.com/RasaHQ/starter-pack-rasa-stack.git
```

The Music-chatbot goal is to answer to classical music related questions of works by artists, to find performances (future or past, only working for performances in Paris), to discover some artist or to find an artist according to its works.

This chatbot is using the DOREMUS project database in order to answer the questions requested by the user.

## Setup and installation

If you haven’t installed Rasa NLU and Rasa Core yet, you can do it by navigating to the project directory and running:  
```
pip install -r requirements.txt
```

You also need to install a spaCy English language model. You can install it by running:

```
python -m spacy download en
```

It is necessary to have **Docker** installed to be able to run the Duckling docker container.

This project conatins the following files:

### Rasa NLU model

The files for the NLU model are:

- **data/nlu_data.md** contains training examples of the following intents: 
	- greet
	- goodbye
	- thanks
	- joke
	- name (examples of this intent contain an entity called 'name')
	- discover_artist
	- works_by
	- works_by_yes
	- works_by_no
	- works_by_filter
	- find_performance
	- time_test
	- find_artist
	
- **nlu_config.yml** contains the configuration of the NLU pipeline:  
```yaml
language: "en"

pipeline:
- name: "nlp_spacy"
- name: "tokenizer_spacy"
- name: "intent_entity_featurizer_regex"
- name: "intent_featurizer_spacy"
- name: "ner_duckling_http"
  url: http://localhost:8000
  dimensions: ["time", "number"]
  locale: 'en_US'
  timezone: "Europe/Paris"
- name: "ner_crf"
- name: "ner_spacy"
- name: "ner_synonyms"
- name: "intent_classifier_sklearn"
```	

### Files for Rasa Core model

- **data/stories.md** file contains some training stories which represent the conversations between a user and the assistant. 
- **domain.yml** file describes the domain of the assistant which includes intents, entities, slots, templates and actions the assistant should be aware of.  
- **actions.py** file contains the code of a custom action for finding works by an artists, finding performances, discovering an artists and finding an artist which retrieves an answer from the DOREMUS project database by making an external API call. This file also contains functions for the custom slots needed for the extraction of the dates used for the different actions.
- **endpoints.yml** file contains the webhook configuration for custom action and the webhook for the slack integration with a slack app.  
- **policies.yml** file contains the configuration of the training policies for Rasa Core model.

## How to use this chatbot?
- NOTE: If running on Windows, you will either have to [install make](http://gnuwin32.sourceforge.net/packages/make.htm) or copy the commands from the [Makefile]

1. You can train the Rasa NLU model by running:  
```make train-nlu```  
This will train the Rasa NLU model and store it inside the `/models/current/nlu` folder of your project directory.

2. Train the Rasa Core model by running:  
```make train-core```  
This will train the Rasa Core model and store it inside the `/models/current/dialogue` folder of your project directory.

3. In a new terminal start the server for the custom action by running:  
```make action-server```  
This will start the server for emulating the custom action.

4. Test the assistant by running:  
```make cmdline```  
This will load the assistant in your terminal for you to chat.

5. To start the chatbot as a server:  
```make chatbot-server```  
This will load the assistant to use the port 5005 in order to integrate it with a messaging app, as for now I just have done this with slack, but it should work with others (credentials for the messaging app should be added in the **credentials.yml** file).

## Running the chatbot

To be able to use the chatbot it is necessary to have running the action server in order to be able to do the requests to the DOREMUS SPARQL endpoint and have running the docker container for Duckling (for time extraction) using: 
``` docker run -p 8000:8000 rasa/duckling ```

## Features

Search for a set of works composed by a given artist, on a given period, with an instrument and/or a specific genre.

-*"Give me 2 works by Vivaldi"*
-*"Find me 2 works by Mozart for violin"*
-*"Tell me 1 work by Beethoven between 1800 and 1820"*
-*"Tell me 3 symphonies by Mozart"*

Search for artists according to their birth day, compositions by an instrument or a genre.

-*"Find 2 artists born in Vienna between 1700 and 1800"*
-*"Give me 2 artists born in Vienna who wrote more works for piano"*

Find the details of performances (past or future) in a city.

-*"Events in Paris next week"*

Give a small biography of an artist.

-*"Tell me about Beethoven"*
-*"Who is Franz Liszt?"*
-*"What do you know about Haydn?"*

