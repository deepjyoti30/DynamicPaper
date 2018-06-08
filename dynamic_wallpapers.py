


template_call = "$HOME/Pictures/Wallpapers/mojave_dynamic/mojave_dynamic_{}.png"

import requests
import json
import subprocess
import threading
import time


getTime = lambda : getAll()["time"]
username = ""
def getAll():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    lat = j['latitude']
    lon = j['longitude']

    time_url = "http://api.geonames.org/timezoneJSON?formatted=true&lat={}&lng={}&username={}".format(lat,lon,username)
    time_info  = requests.get(time_url).json() ## Make a request

    dawn_time = time_info["sunrise"].split(" ")[1].split(":")
    dawn_time = int(dawn_time[0]) + int(dawn_time[1])/60.0
    dusk_time = time_info["sunset"].split(" ")[1].split(":")
    dusk_time = int(dusk_time[0]) + int(dusk_time[1])/60.0

    current_time = time_info['time'].split(" ")[1].split(":")
    current_time = int(current_time[0])+ int(current_time[1])/60.0
    return {"dawn":dawn_time,"dusk":dusk_time,"time":current_time}


order = [i for i in range(1,17)]

time_nfo = getAll()
dusk_time = time_nfo["dusk"]
dawn_time = time_nfo["dawn"]
current_time = time_nfo["time"]

day_dur = dusk_time-dawn_time
night_duration = 24.0 - day_dur

def getIndex(current_time):
    if dawn_time+day_dur >= current_time and current_time >= dawn_time :
        # It's day
        index = (current_time - dawn_time)/(day_dur/13)
    else:
        # It's night
        if current_time > dawn_time:
            index = 13 + (current_time-day_dur-dawn_time)/(night_duration/4) 
        else:
            index = 13 + (current_time + 24-dawn_time-day_dur)/(night_duration/4)
    return int(index+1)

index = getIndex(current_time)


while True:
    subprocess.Popen("DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings \
    set org.gnome.desktop.background picture-uri file://{}"
    .format(template_call.format(index)), shell=True)
    current_time = getTime()
    while index == getIndex(current_time):
        time.sleep(60)
        current_time = getTime()