## story_works_by
* works_by{"number":"1", "doremus-artist":"Vivaldi", "date-period":"1000"}
- utter_works_by

## story_works_by_no
* works_by_no
 - utter_works_by_no
 - action_works_by
 - action_reset_slot

## story_works_by_yes
* works_by_yes
 - utter_works_by_yes
* works_by_instrument{"doremus-instrument":"Violin"}
 - utter_works_by_instrument
* works_by_genre{"doremus-genre":"symphony"}
 - utter_works_by_genre
 - action_works_by
 - action_reset_slot
 - slot{"doremus-instrument":null, "doremus-genre":null, "date-period":null}


## story_works_by
* works_by{"number":"1", "doremus-artist":"Vivaldi", "date-period":"1000"}
 - utter_works_by
 - action_year_slot
 - slot{"date-period": [["to", 1900], ["from", 1800]]}
* works_by_no
 - utter_works_by_no
 - action_works_by
 - action_reset_slot

## story_works_by_2
* works_by{"number":"1", "doremus-artist":"Vivaldi", "date-period":"1000"}
 - utter_works_by
 - action_year_slot
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
 - action_year_slot
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
 - action_year_slot
* works_by_yes
 - utter_works_by_yes
* works_by_genre{"doremus-genre":"symphony"}
 - utter_works_by_genre
 - action_works_by
 - action_reset_slot
 - slot{"doremus-genre":null, "date-period":null}



######## intents

## intent:works_by_instrument
 - [violin](doremus-instrument)
 - only works for [clarinet](doremus-instrument)
 - [clarinet](doremus-instrument)
 - [piano](doremus-instrument) [and](doremus-strictly) [violin](doremus-instrument)
 - With instrument [piano](doremus-instrument) [and](doremus-strictly) [violin](doremus-instrument)
 - [piano](doremus-instrument)
 - Ok, with [saxophone](doremus-instrument)
 - With [saxophone](doremus-instrument)
 - With [violin](doremus-instrument)
 - yes by instrument
 - works by only instrument
 - An instrument
 - [violin](doremus-instrument)
 - by instrument
 - only works for [clarinet](doremus-instrument)
 - yes the instrument
 - [clarinet](doremus-instrument)
 - Yes the instrument
 - [piano](doremus-instrument) [and](doremus-strictly) [violin](doremus-instrument)
 - Yes the instrument [piano](doremus-instrument) [and](doremus-strictly) [violin](doremus-instrument)
 - [piano](doremus-instrument)

## intent: works_by_genre
 - yes by the genre
 - ok by the genre
 - of genre [musique de chambre](doremus-genre)
 - I want only [melody](doremus-genre)
 - of [melody](doremus-genre) genre
 - please show only genre [melody](doremus-genre)
 - the genre
 - [musique de chambre](doremus-genre)
 - Yes the genre
 - [melodie](doremus-genre)
 - yes the genre please
 - yes the genre
 - [melody](doremus-genre)
 - The genre
 - of genre [Symphony](doremus-genre)
 - [Symphonie](doremus-genre) genre
 - [Opera](doremus-genre) genre
 - [Sonata](doremus-genre) genre