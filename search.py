studyKeyword = ['college' , 'university' , 'school' , 'study' ] #learn

def findCategory(input):
    return

import json
from pprint import pprint



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
                        print (person["name"])
                        possibleHelpers.append(person)

                else:
                    foundHelp = True
                    print (person["name"])
                    possibleHelpers.append(person)

    if foundHelp == False:
        for person in data:
            if list(set(language).intersection(person["languages"])) != []: #it is a must
                if genderPreference != None:
                    if person["gender"] == genderPreference:
                        foundHelp = True
                        print (person["name"])
                        possibleHelpers.append(person)

                else:
                    foundHelp = True
                    print (person["name"])
                    possibleHelpers.append(person)



    # We can sort possibleHelpers based on their distance now

    return possibleHelpers

findHelper(["English" , "Russian"] , "male", "Atlanta" , ["Immigration"])
