Samples were collected from a song and lyrics repo. 

The tree can be created using jquery or d3, but right now jquery is being tested first.

One major question is where to focus priorities, given the list of ideas for an educational page that take a different tack in terms of delivering a quality service to guitarists.

Priorities from most important to least important: 
	* navegable structure of most common palos: tangos, bulerías, seguiriyas, sevillanas
	* dropdown of key features (common letras, tonality, compás, range of speeds)
	* connection to youtube resources


** Data Collection Process **

1. Collecting and cleaning data samples (splitraw.py) 

	- splits data from flamenco website canteytoque.com
	- collect_audio_features (uses pyechonest to access song track, 		
artist information, geolocation), 
	- collect_letra_features (currently in .ipynb file. uses sci-kit-		
learn and nltk to collect NLP features: (tempo, artist, length of 
	verses, noun phrases/chunks) (sci_kit_learn)  

2. Run machine learning algorithms like tf-idf and clustering using 
	relevant song features	
	- some ideas are to cluster by palo, by artist/recording location
	- year song was published to learn features and style of songs, 		
artists 

3. Using JavaScript and libraries like d3 to visualize and connect the song data. 
	- connect songs based on features: 
	- chico or jondo...the assumption is that cante chico is light-	hearted and 
cante jondo is serious or tragic, but the verses can 		
	change the mood, and perhaps even the tonality within a particular 	
	recording
	- flamenco friends: which artists composed songs together, lived in 	
the same city, town or province
	





