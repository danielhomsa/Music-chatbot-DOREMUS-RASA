## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_laugh
* laugh
 - utter_laugh

## story_name
* name{"name":"Sam"}
 - utter_greet
 

## story_joke_01
* joke
 - action_joke
 
## story_joke_02
* greet
 - utter_name
* name{"name":"Lucy"} <!--- User response with an entity. In this case it represents user message 'My name is Lucy.' --> 
 - utter_greet
* joke
 - action_joke
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye 

## story_works_by
* works_by{"number":"1", "doremus-artist":"Vivaldi"}
 - utter_works_by
* works_by - no
 - utter_works_by_no
 - action_works_by

## story_works_by_2
* works_by{"number":"1", "doremus-artist":"Vivaldi"}
 - utter_works_by
* works_by - yes
 - utter_works_by_yes
* works_by_instrument{"instrument":"violin"}
 - utter_works_by_instrument

## story_discover_artist
* discover_artist{"doremus-artist":"Bach"}
 - utter_discover_artist
