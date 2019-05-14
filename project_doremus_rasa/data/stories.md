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

## story_discover_artist
* discover_artist{"doremus-artist":"Bach"}
 - utter_discover_artist
 - action_discover_artist

## story_find_performance
* find_performance{"date-period":null, "geo-city": null, "number":"1"}
 - utter_find_performance
 - action_find_performance

## story_works_by
* works_by{"number":"1", "doremus-artist":"Vivaldi", "date-period":"1000"}
 - utter_works_by
 - action_time_test
* works_by_no
 - utter_works_by_no
 - action_works_by
 - action_reset_slot

## story_works_by_2
* works_by{"number":"1", "doremus-artist":"Vivaldi", "date-period":"1000"}
 - utter_works_by
 - action_time_test
* works_by_yes
 - utter_works_by_yes
* works_by_instrument{"doremus-instrument":"Violin"}
 - utter_works_by_instrument
 - action_works_by
 - action_reset_slot
 - slot{"doremus-instrument":null, "date-period":null}

## story_works_by_3
* works_by{"number":"1", "doremus-artist":"Vivaldi", "date-period":"1000"}
 - utter_works_by
 - action_time_test
* works_by_yes
 - utter_works_by_yes
* works_by_instrument{"doremus-instrument":"Violin"}
 - utter_works_by_instrument
* works_by_genre{"doremus-genre":"symphony"}
 - utter_works_by_genre
 - action_works_by
 - action_reset_slot
 - slot{"doremus-instrument":null, "doremus-genre":null, "date-period":null}

## story_works_by_4
* works_by{"number":"1", "doremus-artist":"Vivaldi", "date-period":"1000"}
 - utter_works_by
 - action_time_test
* works_by_yes
 - utter_works_by_yes
* works_by_genre{"doremus-genre":"symphony"}
 - utter_works_by_genre
 - action_works_by
 - action_reset_slot
 - slot{"doremus-genre":null, "date-period":null}

## story_time_test
* time_test
- action_time_test


