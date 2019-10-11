import sys
import json

#creating list of songs from files input through the command line
songlist =[]
for song in range(1, len(sys.argv)):
	songlist.append(sys.argv[song])



#Creating dictionary with each word as its own key 
words_dict = {} 

#open files and split the lyrics as separate words
for song_file in songlist:
	with open(str(song_file)) as song:
		for line in song:
			words = line.split()

#loop through every word
			for word in words:
				word = word.lower()	#convert to lower case
				if word in words_dict: 	#analyze whether the word exists or not in the list, if not > add, if so > +1 count
					words_dict[word]["count"]=words_dict[word]["count"] + 1
							#analyze whether the word is from the original song file or another
					if song_file not in words_dict[word]["songs"]:
						words_dict[word]["songs"].append(song_file)
				else:
					words_dict[word]={"count":1,"songs":[song_file]}
	#create the outfile
	with open('lyrics_output.txt', 'w') as outfile:
		json.dump(words_dict, outfile, indent=1)
		#Counting the amount of the same words in the song file 

