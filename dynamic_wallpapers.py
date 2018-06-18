

import requests
import json
import subprocess
import threading
import time
import sys
import configure
from envinment_calls import set_wallpaper

# ------------define geonames errors--------------

SERVICE_NOT_ENABLED = 'user account not enabled to use the free webservice. Please enable it on your account page: http://www.geonames.org/manageaccount '
INVALID_USER = 'invalid user'
USER_NOT_EXIST= 'user does not exist.'
ACCOUNT_NOT_CONFIRMED = 'user account has not been confirmed. Check your email for the confirmation email.'

GEONAME_ERRORS = {
    INVALID_USER: 'Your account was not found in geonames. Please check your username in the config file\a',
    SERVICE_NOT_ENABLED: 'Please go to http://www.geonames.org/enablefreewebservice to enable the free webservice\a',
    USER_NOT_EXIST: 'Your account was not found in geonames. Please check your username in the config file\a',
    ACCOUNT_NOT_CONFIRMED:'Your account was not confirmed. Check your email and follow the instructions in the github page\a',
}

# ------------------------------------------------

#URL Consts
LOCATION_BY_IP = 'http://freegeoip.net/json'
TIME_BY_LOCATION = 'http://api.geonames.org/timezoneJSON?formatted=true&lat={}&lng={}&username={}'

#Sanity Checking
def checkTimeInfo(time_info):
    for key in {'sunrise','sunset','time'}:
                if key not in time_info:
                    print("Unexpected Error, please issue an error at the public repository with the received message.")
                    print("_______________________________________")
                    print(time_info)
                    print("_______________________________________")
                    print("Key: {} not found.".format(key))
                    exit(-1)
#Getting Coordinates
def getCoordinates():
    try:
        j = requests.get(LOCATION_BY_IP).json()
        lat = j['latitude']
        lon = j['longitude']
    except TimeoutError:
        print('Timeout was reached.\a Please check if your connected to internet.')
        exit(-1)
    except KeyError:
        print("Unknown error, please write an issue to inform us.")
        exit(-1)
    return (lat,lon)

def getTime(lat,lon): return getAll(lat,lon)["time"]

def getAll(lat, lon):
    time_url = TIME_BY_LOCATION.format(lat, lon, username)
    try :
        time_info = requests.get(time_url).json()  # Make a request
        # Check for errors
        if 'status' in time_info:
            report = time_info['status']
            if report['message'] in GEONAME_ERRORS:
                print(GEONAME_ERRORS[report['message']])
            else:
                print("Unexpected Error, please issue an error at the public repository with the received message.")
            exit(-1)
        else:
            checkTimeInfo(time_info)
        
        dawn_time = time_info["sunrise"].split(" ")[1].split(":")
        dawn_time = int(dawn_time[0]) + int(dawn_time[1])/60.0
        dusk_time = time_info["sunset"].split(" ")[1].split(":")
        dusk_time = int(dusk_time[0]) + int(dusk_time[1])/60.0

        current_time = time_info['time'].split(" ")[1].split(":")
        current_time = int(current_time[0]) + int(current_time[1])/60.0
        return {"dawn": dawn_time, "dusk": dusk_time, "time": current_time}

    except TimeoutError:
        print('Timeout was reached.\a Please check if your connected to internet.')
        exit(-1)
    except KeyError:
        print("Unknown error, please write an issue to inform us.")
        exit(-1)
    


def getIndex(current_time):
    if dawn_time+day_dur >= current_time and current_time >= dawn_time:
        # It's day
        index = (current_time - dawn_time)/(day_dur/13)
    else:
        # It's night
        if current_time > dawn_time:
            index = 13 + (current_time-day_dur-dawn_time)/(night_duration/4)
        else:
            index = 13 + (current_time + 24-dawn_time-day_dur) / \
                (night_duration/4)
    return int(index+1)


if __name__ == '__main__':
    # Check if -setup was passed

    if len(sys.argv) == 2:
        if sys.argv[1] != '-setup':
            print('Unknown arguement\a')
            sys.exit(1)
        elif sys.argv[1] == '-setup':
            configure.setup()
            sys.exit(1)
        else:
            # Continue exec
            pass

    # Get the wallpaper setter defined by the user in config

    USER_DEFINED_SETTER = configure.get('PAPER_SETTER')

    username = configure.get('USERNAME')

    order = [i for i in range(1, 17)]
    
    lat,lon = getCoordinates()
    time_nfo = getAll(lat, lon)
    dusk_time = time_nfo["dusk"]
    dawn_time = time_nfo["dawn"]
    current_time = time_nfo["time"]

    day_dur = dusk_time-dawn_time
    night_duration = 24.0 - day_dur

    index = getIndex(current_time)
    while True:
        wall = configure.template().format(index)
        set_wallpaper(USER_DEFINED_SETTER, wall)
        current_time = getTime(lat,lon)
        while index == getIndex(current_time):
            #Sleep for 5 minutes
            time.sleep(60*5)
            #Add 5 minutes
            current_time = current_time + 5/60.0
        index = getIndex(current_time)
