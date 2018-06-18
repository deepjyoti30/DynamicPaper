
import subprocess

'''
To add your environment, simply add the identifier you want to use and the desired function call.
'''

PROCESS_CALLS = {
    'GNOME': "DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{}",
    'nitrogen': "nitrogen --set-auto {}",
    'feh': "feh --bg-scale {}"
}


def set_wallpaper(environment, wallpaper):
    if environment in PROCESS_CALLS:
        subprocess.Popen(
            PROCESS_CALLS[environment].format(wallpaper), shell=True)
    else:
        print("{} is not supported yet. Sorry!".format(environment))
        exit(-1)
