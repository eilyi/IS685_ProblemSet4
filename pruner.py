#REMOVE: names that contain the letter 'v'
#REMOVE: Gary, Aaron, Luke, Winston, Avery
#REMOVE: Names with a count of 28
#ADD: The name "Ron"

import json


def delete_if_exists(dictionary, key):
	if key in dictionary:
		del dictionary[key]

def delete_letter(dictionary, letter):
	for key in dictionary:
		if (letter in dictionary[key]):
			del dictionary[key]

def delete_count(dictionary, count):
	for key in dictionary:
		if (dictionary[key] == 28):
			del dictionary[key]

def add_new(dictionary, name, count):
	dictionary[name] = count

with open('baby_names.txt') as json_file:
    babies_dict = json.load(json_file)

delete_if_exists(babies_dict["top"], "Gary")
delete_if_exists(babies_dict["top"], "Aaron")
delete_if_exists(babies_dict["top"], "Luke")
delete_if_exists(babies_dict["top"], "Winston")
delete_if_exists(babies_dict["top"], "Avery")

delete_letter(babies_dict["top"], 'v')

delete_count(babies_dict["top"], 28)

add_new(babies_dict["top"], "Ron", str(5))

with open('better_names.txt', 'w') as outfile:
    json.dump(babies_dict, outfile, indent=4)

#babies = {}		#creating dictionary 
#with open('baby_names.txt') as infile:
#	for line in infile:
#		babies = infile.readlines()
#		babies.split()
#		babies["key"] = value

#del babies["28"]

