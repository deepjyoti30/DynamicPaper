# Setup the config file in the $HOME/.config/dynamicpaper dir

import os
from pathlib import Path
import shutil
import subprocess


class PATHS:
    # The home dir
    HOME_DIR = str(Path.home())

    CONFIG_DIR = os.path.join(HOME_DIR, '.config')

    # The config dir
    CONFIG_FILE_DIR = os.path.join(CONFIG_DIR, 'dynamicpaper')

    # The config path
    CONFIG_PATH = os.path.join(CONFIG_FILE_DIR, 'config')


def isPresent():
    # Check if the config file is already present in the dir

    # Need to check if dynamicwall is present
    folders = os.listdir(PATHS.CONFIG_DIR)

    if 'dynamicpaper' not in folders:
        # Since not present, create it
        os.mkdir(PATHS.CONFIG_FILE_DIR)
        return False

    return 'config' in set(os.listdir(PATHS.CONFIG_FILE_DIR))


def copyConfig():
    # Copy the config file from the current directory
    # to the .config/dynamicwall dir

    try:
        shutil.copy('config', PATHS.CONFIG_FILE_DIR)
        return True
    except:
        return False


def get(keyword):
    # Get the keyword defined in config file
    # It will return the keywords value only if isPresent()
    # return True, else False will be returned

    if isPresent():
        readStream = open(PATHS.CONFIG_PATH, 'r')

        while True:
            line = readStream.readline()

            if not line:
                return False

            if keyword in line and '#' not in line:
                # remove the spaces
                line = line.replace(' ', '')
                posEqual = line.index('=')

                # Check if \n is present at the end
                if "\n" == line[len(line) - 1]:
                    line = line[:-1]

                return line[posEqual + 1:]
    else:
        return False


def template():
    # Get the dir of the wallpaper.

    template = get('WALL_DIR')

    template_path = os.path.join(
        template, 'mojave_dynamic_{1}.{0}'.format(get("EXTENSION"), "{}"))

    return template_path


def setup():
    subprocess.call(['sh', 'setupDynamic.sh'])
