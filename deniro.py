#deniro 
import csv
import json

#open and read
with open("deniro.csv") as infile:
    reader = csv.reader(infile)
    
    deniro_dict = {}
    for row in enumerate(reader):

    #trim first and last rows in CSV 

    #for row in rdr:
	    for index, row in enumerate(reader):
	         if (index != 0 and len(row) == 3):
	         	deniro_dict[row[2]] = { "Score" : int(row[1]), "Year" : row[0]}
#create the txt file & format 
with open('deniro_json.txt', 'w') as outfile:
    json.dump(deniro_dict, outfile, indent=4)

