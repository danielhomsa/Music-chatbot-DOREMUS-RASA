<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/rasa-starter-pack/704 --> 

## intent:goodbye <!--- The label of the intent --> 
- Bye 			<!--- Training examples for intent 'bye'--> 
- Goodbye
- See you later
- Bye bot
- Goodbye friend
- bye
- bye for now
- catch you later
- gotta go
- See you
- goodnight
- have a nice day
- i'm off
- see you later alligator
- we'll speak soon

## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot

## intent:thanks
- Thanks
- Thank you
- Thank you so much
- Thanks bot
- Thanks for that
- cheers
- cheers bro
- ok thanks!
- perfect thank you
- thanks a bunch for everything
- thanks for the help
- thanks a lot
- amazing, thanks
- cool, thanks
- cool thank you

## intent:affirm
- yes
- yes sure
- absolutely
- for sure
- yes yes yes
- definitely


## intent:name
- My name is [Juste](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- I am [Josh](name)
- I'm [Lucy](name)
- People call me [Greg](name)
- It's [David](name)
- Usually people call me [Amy](name)
- My name is [John](name)
- You can call me [Sam](name)
- Please call me [Linda](name)
- Name name is [Tom](name)
- I am [Richard](name)
- I'm [Tracy](name)
- Call me [Sally](name)
- I am [Philipp](name)
- I am [Charlie](name)
- I am [Charlie](name)
- I am [Ben](name)
- Call me [Susan](name)
- [Lucy](name)
- [Peter](name)
- [Mark](name)
- [Joseph](name)
- [Tan](name)
- [Pete](name)
- [Elon](name)
- [Penny](name)
- name is [Andrew](name)
- I [Lora](name)
- [Stan](name) is my name
- [Susan](name) is the name
- [Ross](name) is my first name
- [Bing](name) is my last name
- Few call me as [Angelina](name)
- Some call me [Julia](name)
- Everyone calls me [Laura](name)
- I am [Ganesh](name)
- My name is [Mike](name)
- just call me [Monika](name)
- Few call [Dan](name)
- You can always call me [Suraj](name)
- Some will call me [Andrew](name)
- My name is [Ajay](name)
- I call [Ding](name)
- I'm [Partia](name)
- Please call me [Leo](name)
- name is [Pari](name)
- name [Sanjay](name)


## intent:joke
- Can you tell me a joke?
- I would like to hear a joke
- Tell me a joke
- A joke please
- Tell me a joke please
- I would like to hear a joke
- I would loke to hear a joke, please
- Can you tell jokes?
- Please tell me a joke
- I need to hear a joke

## intent:laugh
- Can you laugh?

## intent:discover_artist
- Tell me about [Bach](doremus-artist)
- Who is [Vivaldi](doremus-artist)?
- Tell me something about [Bach](doremus-artist)
- Tell me about [Vivaldi](doremus-artist)
- Tell me about [Mozart](doremus-artist)
- Who is [Mozart](doremus-artist)?
- Who is [Vivaldi](doremus-artist)
- Who is [Mozart](doremus-artist)
- Tell me something about [Mozart](doremus-artist)
- Tell me something about [Vivaldi](doremus-artist)
- Tell me something about [Vivaldi](doremus-artist)
- Tell me something about [Beethoven](doremus-artist)
- Tell me something about [Mozart](doremus-artist)
- Talk me about [Jonathan Dove](doremus-artist)
- Talk me about [Rachmaninov](doremus-artist)
- Talk me about [Rachmaninof](doremus-artist)
- Talk me about [Rachmaninoff](doremus-artist)
- Talk me about [Racmaninov](doremus-artist)
- Talk me about [Racmaninoff](doremus-artist)
- tell me something about [debussy](doremus-artist)
- Talk me about [Jonathan Dove](doremus-artist)!
- Ok so talk me about [Rachmaninoff](doremus-artist)
- Talk me about [debussy](doremus-artist)
- tell me something about [Rachmaninoff](doremus-artist)
- talk me about [John Dove](doremus-artist)
- Okay now talk me about [Rachmaninoff](doremus-artist)
- Talk me about [Rachmaninoff](doremus-artist)
- Tell me something about [Rachmaninov](doremus-artist)
- Talk me about [Vivaldi](doremus-artist)
- [Rachmaninoff](doremus-artist)
- who is [Mozart](doremus-artist)
- Tell me about [Vivaldi](doremus-artist)
- Tell me about [Rachmaninov](doremus-artist)

## intent:works_by
- Give me [2](number) works by [Bach](doremus-artist)
- Give me [1](number) works by [Bach](doremus-artist)
- Give me [one](number) works by [Bach](doremus-artist)
- Give me [1](number) works by [Mozart](doremus-artist)
- Tell me [two](number) works by [Vivaldi](doremus-artist)
- Tell me [5](number) works by [Beethoven](doremus-artist)
- Tell me [two](number) works by [Antonio Vivaldi](doremus-artist)
- Tell me [six](number) works by [Johann Sebastian Bach](doremus-artist)
- Give me [three](number) works by [Johann Sebastian Bach](doremus-artist)
- Tell me [10](number) works by [Ludwig van Beethoven](doremus-artist)
- Give me [one](number) works by [Ludwig van Beethoven](doremus-artist)
- Give me [4](number) works by [Antonio Vivaldi](doremus-artist)
- Give me [one](number) work by [Beethoven](doremus-artist) but just the one written for [piano](doremus-instrument) [clarinet](doremus-instrument) [and](doremus-strictly) [violin](doremus-instrument)
 - Give me [six](number) works by [Beethoven](doremus-artist) but just the one written for [piano](doremus-instrument) [clarinet](doremus-instrument) [and](doremus-strictly) [violin](doremus-instrument)
 - Tell me [2](number) works by [Beethoven](doremus-artist)
 - Give me [5](number) works about [Beethoven](doremus-artist)
 - now give me [2](number) of his works
 - Give me [2](number) works by [Piccinini](doremus-artist)
 - Give me [2](number) works by [Niccolò Piccinini](doremus-artist)
 - Give me [2](number) works by [Niccolò Piccinini](doremus-artist)
 - Give me [2](number) works by [Latilla](doremus-artist)
 - Give me [2](number) works by [Debussi](doremus-artist)
 - Give me [2](number) works by [Debusy](doremus-artist)
 - Give me [2](number) works by [debussy](doremus-artist)
 - Give me [2](number) works by [debussy](doremus-artist)
 - Give me [ten](number) works by [debussy](doremus-artist)
 - Give me the works by [debussy](doremus-artist)
 - Give me the works by [debussy](doremus-artist) composed [between 1890 and 1900](date-period) of genre [musique de chambre](doremus-genre)
 - Give me the works by [debussy](doremus-artist) composed [between 1890 and 1900](date-period) of genre [melodie](doremus-genre)
 - Give me [2](number) melodic works by [debussy](doremus-artist) composed [between 1890 and 1900](date-period)
 - Give me [2](number) [melodies](doremus-genre) by [debussy](doremus-artist) composed [between 1890 and 1900](date-period)
 - Give me [2](number) [concertos](doremus-genre) by [debussy](doremus-artist) composed [between 1890 and 1900](date-period)
 - Give me [2](number) [melodies](doremus-genre) by [debussy](doremus-artist)
 - Give me [2](number) [concertos](doremus-genre) by [debussy](doremus-artist)
 - Give me [2](number) [concerts](doremus-genre) by [debussy](doremus-artist) composed [between 1890 and 1900](date-period)
 - Give me [2](number) [concerts](doremus-genre) by [debussy](doremus-artist)
 - Give me [2](number) [concerts](doremus-genre)
 - Give me [10](number) [concerts](doremus-genre) by [debussy](doremus-artist)
 - Give me the [melodies](doremus-genre) by [debussy](doremus-artist) composed [between 1890 and 1900](date-period)
 - Give me the [melodies](doremus-genre)
 - Give me some works by [debussy](doremus-artist)
 - give me [2](number) works by [debussy](doremus-artist)
 - give me [2](number) works by [debussy](doremus-artist)
 - give me [2](number) [melody](doremus-genre) by [Vivaldi](doremus-artist)
 - give me [2](number) works by [Mozart](doremus-artist)
 - tell me [2](number) works by [Vivaldi](doremus-artist)
 - Now give me [two](number) of his works
 - Tell me the [melodies](doremus-genre) by [debussy](doremus-artist) composed [during 1890](date-period)
 - Tell me the [melodies](doremus-genre) by [debussy](doremus-artist) composed [between 1860 and 1870](date-period)
 - Tell me the [melodies](doremus-genre) by [debussy](doremus-artist) composed [between 1890 and 1900](date-period)
 - Give me [one](number) work by [debussy](doremus-artist)
 - Give me [one](number) works by [Mozart](doremus-artist)
 - Give me [3](number) works composed by Bach
 - Give me [2](number) of his works
 - Now give me [2](number) of his works
 - give me [four](number) works by [Mozart](doremus-artist)
 - give me [four](number) works by [Mozart](doremus-artist)
 - give me [four](number) works by [Beethoven](doremus-artist)
 - give me [one](number) work by [Mozart](doremus-artist)
 - hello give me [four](number) works by [Mozart](doremus-artist)
 - give me [three](number) works by [Vivaldi](doremus-artist)
 - give me [six](number) works by [Vivaldi](doremus-artist)
 - tell me [two](number) works by [Mozart](doremus-artist)
 - give me [two](number) words by [Vivaldi](doremus-artist)
 - give me [two](number) works by [Vivaldi](doremus-artist)
 - Tell me [2](number) works by [Mozart](doremus-artist)
 - Tell me [2](number) [symphonies](doremus-genre) by [Beethoven](doremus-artist)
 - Tell me [2](number) [symphonies](doremus-genre) by [Mozart](doremus-artist)
 - Tell me [2](number) operas by [Mozart](doremus-artist)
 - now give me [two](number) of his works
 - now give me [2](number) of his [melodies](doremus-genre) composed [between 1890 and 1900](date-period)
 - now give me his [melodies](doremus-genre) composed [between 1890 and 1900](date-period)
 - give me [one](number) work by [debussy](doremus-artist)
 - Tell me the [melodies](doremus-genre) by [debussy](doremus-artist)
 - give me [5](number) works by [Mozart](doremus-artist)
 - Give me [3](number) works by [Mozart](doremus-artist) with [violin](doremus-instrument)
 - show me works by [Mozart](doremus-artist)
 - Tell me [2](number) works
 - Give me [2](number) works by [Mozart](doremus-artist)
 - Give me [two](number) works by [Vivaldi](doremus-artist)
 - Give me [2](number) works by [Vivaldi](doremus-artist)
 - give me [3](number) works by [Mozart](doremus-artist)
 - give me [two](number) works from [mother](doremus-artist)
 - Give me [two](number) works from [Vivaldi](doremus-artist)
 - Give me [two](number) works from [Vivaldi](doremus-artist) for [violin](doremus-instrument)
 - show me [3](number) works by [Mozart](doremus-artist)

## intent:works-by_yes
 - Yes thanks!
 - Yes thanks
 - yes!
 - yes
 - Yes!
 - Yes
 - yes sure I'll try
 - ok 
 - sounds good
 - ok
 - OK!

## intent:works-by_no
 - No it's ok
 - No
 - no
 - nope
 - no thanks
 - no thakns
 - no!
 - No thanks
 - No
 - I don't think so
 - nah

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

<!-- ## synonym:Antonio Vivaldi
- Vivaldi
- vivaldi
- antonio
- AV
- A. Vivaldi

## synonym:Johann Sebastian Bach
- bach
- Bach
- Sebastian Bach

## synonym:Violin
- violin -->




