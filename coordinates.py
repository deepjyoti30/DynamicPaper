# Get the coordinates.
# If the user has specified location then use it to get lat and long
# Else use the ip adress.

import requests
import json
import configure

COORDINATES_BY_IP = 'http://ip-api.com/json'
COORDINATES_BY_LOCATION = 'http://open.mapquestapi.com/geocoding/v1/address?key=43Ht4h9p2japf7eLYOCGeQy7ldz3wRAC&location={}'

def get():
    # Check how to get the lat and long
    location = configure.get('LOCATION')
    if not location:
        try:
            j = requests.get(COORDINATES_BY_IP).json()
            lat = j['lat']
            lon = j['lon']
        except TimeoutError:
            print('Timeout was reached.\a Please check if your connected to internet.')
            exit(-1)
        except KeyError:
            print("Unknown error, please write an issue to inform us.")
            exit(-1)
        return (lat,lon)
    else:
        try:
            # Get data from mapquestapi.com
            j = requests.get(COORDINATES_BY_LOCATION.format(location)).json()
            # Get the result
            j = j['results']
            # Always consider the first result
            j = j[0]
            # Get location of the first result
            j = j['locations']
            # Get the first result
            j = j[0]
            # Finaly get the coordinates
            j = j['latLng']
            # Grab them seperately
            lat = j['lat']
            lon = j['lng']
        except TimeoutError:
            print('Timeout was reached.\a Please check if your connected to internet.')
            exit(-1)
        except KeyError:
            print("Unknown error, please write an issue to inform us.")
            exit(-1)
        return (lat,lon)