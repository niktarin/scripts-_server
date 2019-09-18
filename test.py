import googlemaps
from datetime import datetime
# from googlemaps import GoogleMaps
import pygeocoder
import requests
gmaps = googlemaps.Client(key='AIzaSyB6qE9djrQ16ogLekVW0lszfcIlUNHWgKE')

my_key = "AIzaSyB6qE9djrQ16ogLekVW0lszfcIlUNHWgKE"
my_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key={my_key}"
ans = requests.get(my_url)
ans = ans.json()
print(ans)
# Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.latlng_to_address((40.714224, -73.961452))
# print(reverse_geocode_result)
# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)