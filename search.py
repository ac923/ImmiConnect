
def findCategory(input):
    return

import json
from pprint import pprint
from flask import Flask, render_template, request, redirect, Response
import random, json
import requests
import sys

app = Flask(__name__)

@app.route('/')
def output():
	# serve index template
	return render_template('index.html')

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


@app.route('/receiver', methods = ['POST'])
def findHelper():
    possibleHelpers = []
    with open('document.json') as f:
        data = json.load(f)

    Userdata = request.get_json(force=True)
    language = []
    language.append(Userdata["language"])
    genderPreference = Userdata["gender"]
    location = Userdata["location"]
    tag = Userdata["tags"]

    foundHelp = False
    for person in data:
        if list(set(language).intersection(person["languages"])) != []: #it is a must
            if list(set(tag).intersection(person["tags"])) != []:
                if genderPreference != "No Preference":
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
                if genderPreference != "No Preference":
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
    return json.dumps(sortHelpers(possibleHelpers, location))

if __name__ == '__main__':
	# run!
	app.run()
#ans = findHelper(["Persian"] , "No Preference", "New York,NY" , ["hsdfs"])
#for person in ans:
#    print (person["name"] + " - " + person["address"])
