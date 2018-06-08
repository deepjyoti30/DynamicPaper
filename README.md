# DynamicPaper
Dynamic, time based wallpapers inspired by Mac OS Mojave for Linux

The project is currently WIP and works only in Gnome based environments as of right now.

Progress:

- [x] Write initial program that does the job using Mojave's wallpapers
- [ ] Add configuration file to load from that.
- [ ] Add arguments and reduce hardcoded variables.
- [ ] Add support for additional WM | environments.
- [ ] Replace geolocation api

Current Issue(s):
- Uses IP to find time and geolocation.
- Currently works only in Gnome and derivatives.
- Uses GeoNames api, requires account but is free.


How to use:

1. Make an account at http://www.geonames.org/login  
2. Enable free api features at geonames.
3. Edit the following:

    ```Python 
    username = ""
    ```
4. Run using:  
    ```Bash
    python3 ./dynamic_wallpapers.py&
    disown
    ```
