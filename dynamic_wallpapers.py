

import requests
import json
import subprocess
import threading
import time
import sys
import configure
from envinment_calls import set_wallpaper

template_call = "$HOME/DynamicPaper/mojave/mojave_dynamic_{}.jpeg"

# ------------define geonames errors--------------
SERVICE_NOT_ENABLED = 'user account not enabled to use the free webservice. Please enable it on your account page: http://www.geonames.org/manageaccount '
INVALID_USER = 'invalid user'
ACCOUNT_NOT_CONFIRMED = 'user account has not been confirmed. Check your email for the confirmation email.'
# ------------------------------------------------


def getTime(): return getAll()["time"]


def getAll():
    try:
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']

        time_url = "http://api.geonames.org/timezoneJSON?formatted=true&lat={}&lng={}&username={}".format(
            lat, lon, username)

        try:
            time_info = requests.get(time_url).json()  # Make a request
        except TimeoutError:
            print('Timeout was reached.\a Please check if your connected to internet.')
            sys.exit(1)
        
        # Check for errors
        try:
            report = time_info['status']
            if report['message'] == INVALID_USER:
                print(
                    'Your account was not found in geonames. Please check your username in the config file\a')
                sys.exit(1)
            elif report['message'] == SERVICE_NOT_ENABLED:
                print(
                    'Please go to http://www.geonames.org/enablefreewebservice to enable the free webservice\a')
                sys.exit(1)
            elif report['message'] == ACCOUNT_NOT_CONFIRMED:
                print(
                    'Your account was not confirmed. Check your email and follow the instructions in the github page\a')
                sys.exit(1)
        except:
            pass
        dawn_time = time_info["sunrise"].split(" ")[1].split(":")
        dawn_time = int(dawn_time[0]) + int(dawn_time[1])/60.0
        dusk_time = time_info["sunset"].split(" ")[1].split(":")
        dusk_time = int(dusk_time[0]) + int(dusk_time[1])/60.0

        current_time = time_info['time'].split(" ")[1].split(":")
        current_time = int(current_time[0]) + int(current_time[1])/60.0
        return {"dawn": dawn_time, "dusk": dusk_time, "time": current_time}

    except:
        time.sleep(60)
        return getAll()


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

    time_nfo = getAll()
    dusk_time = time_nfo["dusk"]
    dawn_time = time_nfo["dawn"]
    current_time = time_nfo["time"]

    day_dur = dusk_time-dawn_time
    night_duration = 24.0 - day_dur

    index = getIndex(current_time)
    while True:
        wall = template_call.format(index)
        set_wallpaper(USER_DEFINED_SETTER, wall)
        current_time = getTime()
        while index == getIndex(current_time):
            time.sleep(60)
            current_time = current_time + 1/60.0
        index = getIndex(current_time)
