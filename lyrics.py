import sys
import json

#1. defining first argument of command line
songlist =[]
for song in range(1, len(sys.argv)):
	songlist.append(sys.argv[song])



#Creating dictionary with each word as its own key 
#Needs to be converted to lowercase before put in dictionary

words_dict = {} 

for song_file in songlist:
	with open(str(song_file)) as song:
		for line in song:
			words = line.split()

#loop through every word
			for word in words:
				word = word.lower()
				if word in words_dict:
					words_dict[word]["count"]=words_dict[word]["count"] + 1

					if song_file not in words_dict[word]["songs"]:
						words_dict[word]["songs"].append(song_file)
				else:
					words_dict[word]={"count":1,"songs":[song_file]}

	with open('lyrics_output.txt', 'w') as outfile:
		json.dump(words_dict, outfile, indent=1)
		#Counting the amount of the same words in the song file 

