import requests
origins="Boston"
destinations="Atlanta|Seattle"
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+origins+'&destinations='+destinations+'&key=AIzaSyAIDJxS6sp_j8PJNk7y0RapKInxDBJkIz8'
response = requests.post(url).json()
print(len(response["rows"][0]['elements']))
print(response["rows"][0]['elements'][0]['distance'])
#print(response["rows"][0]['elements'][0]['distance'])
print(response["rows"][0]['elements'][1]['distance'])
