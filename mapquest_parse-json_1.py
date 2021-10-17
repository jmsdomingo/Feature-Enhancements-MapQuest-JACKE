import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Roma, Italia"
dest = "Frascati, Italia"
key = "Fog7lroZGntKj1Es8s4P62KF9xFa9LtK" #Replace with your MapQuest key
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)