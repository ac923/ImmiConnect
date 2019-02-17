studyKeyword = ['college' , 'university' , 'school' , 'study' ] #learn

def findCategory(input):
    return

import json
from pprint import pprint

import requests
import sys


def sortHelpers(helpers, userLocation):
	origins=userLocation
	destinations=""
	for h in helpers:
		destinations=destinations+h["address"]+"|"

	destinations=destinations[:-1]


	#destinations="Atlanta|Seattle"
	url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+origins+'&destinations='+destinations+'&key=AIzaSyAIDJxS6sp_j8PJNk7y0RapKInxDBJkIz8'
	response = requests.post(url).json()

	elems=response["rows"][0]['elements']
	places=[]
	for i in range(0,len(elems)):
		dis=int((elems[i]['distance']['text'].replace(",","")[:-3]))
		places.append({"helper":helpers[i], "distance":dis})

	def takeDistance(e):
		return e["distance"]
	places.sort(key=takeDistance)
	sortedPlaces=[p["helper"] for p in places]

	return sortedPlaces



def findHelper(language, genderPreference, location, tag):
    possibleHelpers = []
    with open('document.json') as f:
        data = json.load(f)
    foundHelp = False
    for person in data:
        if list(set(language).intersection(person["languages"])) != []: #it is a must
            if list(set(tag).intersection(person["tags"])) != []:
                if genderPreference != None:
                    if person["gender"] == genderPreference:
                        foundHelp = True
                        #print (person["name"])
                        possibleHelpers.append(person)

                else:
                    foundHelp = True
                    #print (person["name"])
                    possibleHelpers.append(person)

    if foundHelp == False:
        for person in data:
            if list(set(language).intersection(person["languages"])) != []: #it is a must
                if genderPreference != None:
                    if person["gender"] == genderPreference:
                        foundHelp = True
                        #print (person["name"])
                        possibleHelpers.append(person)

                else:
                    foundHelp = True
                    #print (person["name"])
                    possibleHelpers.append(person)



    # We can sort possibleHelpers based on their distance now
    #print (possibleHelpers)
    return sortHelpers(possibleHelpers, location)

ans = findHelper(["Persian"] , None, "New York,NY" , ["hsdfs"])
for person in ans:
    print (person["name"] + " - " + person["address"])
