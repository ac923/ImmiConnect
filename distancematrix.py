import requests
import sys


def sortHelpers(helpers):
	origins="Chapel Hill,NC"
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
		dis=int((elems[i]['distance']['text'].replace(",","").replace(" mi","")))
		places.append({"helper":helpers[i], "distance":dis})

	def takeDistance(e):
		return e["distance"]
	places.sort(key=takeDistance)
	sortedPlaces=[p["helper"] for p in places]
	
	return sortedPlaces




def main(n):
    helps=[{"name":"AC","address":"Boston,MA"},{"name":"BC","address":"Atlanta,GA"},
    {"name":"CD","address":"New York,NY"}]
    places=sortHelpers(helps)
    print(places)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))

	

	


