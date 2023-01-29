'''
import requests
import datetime
from geopy.geocoders import Nominatim
from random import uniform

# Function to get the latitude and longitude of an address
def get_coordinates(address):
    api_key = "AIzaSyBhWkYip650cJNOlOWUalhq3IBKitF96HE"
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url).json()
    lat = response["results"][0]["geometry"]["location"]["lat"]
    lng = response["results"][0]["geometry"]["location"]["lng"]
    return lat, lng

# Random location in bay area
geolocator = Nominatim(user_agent="geoapiExercises")

def get_random_location(bbox):
    location = geolocator.reverse(f"{uniform(bbox[0], bbox[2]):.7f}, {uniform(bbox[1], bbox[3]):.7f}", timeout=10)
    return location

# San Francisco Bay Area bounding box coordinates
bbox = [37.639097, -123.173825, 38.343068, -121.696143]

random_location = get_random_location(bbox)
print(random_location.raw["lat"], random_location.raw["lon"])
print((random_location))
# Example usage
address = "265 Camelback Rd, Pleasant Hill, CA"
lat, lng = get_coordinates(address)
#address2 = "897 Ruth Dr, Pleasant Hill, CA"
#lat2, lng2 = get_coordinates(address2)
print(f"latitude: {lat}, longitude: {lng}")
#print(f"latitude: {lat2}, longitude: {lng2}")

# Random location in bay area



def call_ambulance(lat, lng):
    # API key for Google Maps Distance Matrix API
    api_key = "AIzaSyBhWkYip650cJNOlOWUalhq3IBKitF96HE"
    # URL for the API call
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=random_location.raw["lat"], random_location.raw["lon"]&&destinations={lat},{lng}&key={api_key}"
    # Make the API call and get the response
    response = requests.get(url).json()
    # Check if the API returned an error
    if "error_message" in response:
        print("Error: " + response["error_message"])
    elif "rows" not in response or "elements" not in response["rows"][0] or "duration" not in response["rows"][0]["elements"][0]:
        print("Error: Invalid response from API")
    else:
        # Get the estimated travel time from the API response
        duration = response["rows"][0]["elements"][0]["duration"]["value"]
        # Calculate the estimated time of arrival
        eta = datetime.datetime.now() + datetime.timedelta(seconds=duration)
        return eta

# Example usage
eta = call_ambulance(lat, lng)
if eta:
    print(eta)
'''

import requests
import datetime
from geopy.geocoders import Nominatim
from random import uniform

# Function to get the latitude and longitude of an address
def get_coordinates(address):
    api_key = "AIzaSyBhWkYip650cJNOlOWUalhq3IBKitF96HE"
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(url).json()
    lat = response["results"][0]["geometry"]["location"]["lat"]
    lng = response["results"][0]["geometry"]["location"]["lng"]
    return lat, lng

# Random location in bay area
geolocator = Nominatim(user_agent="geoapiExercises")

def get_random_location(bbox):
    location = geolocator.reverse(f"{uniform(bbox[0], bbox[2]):.7f}, {uniform(bbox[1], bbox[3]):.7f}", timeout=10)
    return location

# San Francisco Bay Area bounding box coordinates
bbox = [37.639097, -123.173825, 38.343068, -121.696143]

random_location = get_random_location(bbox)
print(random_location.raw["lat"], random_location.raw["lon"])

# Example usage
address = "265 Camelback Rd, Pleasant Hill, CA"
lat, lng = get_coordinates(address)
#address2 = "897 Ruth Dr, Pleasant Hill, CA"
#lat2, lng2 = get_coordinates(address2)
lat2 = random_location.raw["lat"]
lng2 = random_location.raw["lon"]
print(f"latitude: {lat}, longitude: {lng}")
print(random_location)
#print(f"latitude: {lat2}, longitude: {lng2}")

# Random location in bay area



def call_ambulance(lat, lng):
    # API key for Google Maps Distance Matrix API
    api_key = "AIzaSyBhWkYip650cJNOlOWUalhq3IBKitF96HE"
    # URL for the API call
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={lat},{lng}&destinations={random_location.raw['lat']},{random_location.raw['lon']}&key={api_key}"
    # Make the API call and get the response
    response = requests.get(url).json()
    # Check if the API returned an error
    if "error_message" in response:
        print("Error: " + response["error_message"])
    elif "rows" not in response or "elements" not in response["rows"][0] or "duration" not in response["rows"][0]["elements"][0]:
        print("Error: Invalid response from API")
    else:
        # Get the estimated travel time from the API response
        duration = response["rows"][0]["elements"][0]["duration"]["value"]
        # Calculate the estimated time of arrival
        eta = datetime.datetime.now() + datetime.timedelta(seconds=duration)
        return eta

# Example usage
eta = call_ambulance(lat, lng)
if eta:
    print(eta)
