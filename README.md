# DynamicPaper

## Dynamic, time based wallpapers inspired by Mac OS Mojave for Linux

## The project is currently WIP and works only in Gnome based environments as of right now.

### Currently Works with nitrogen and on Gnome

Progress:

- [x] Write initial program that does the job using Mojave's wallpapers.
- [ ] Close subprocess (As of right now it becomes defunct).
- [x] Add configuration file to load from that.
- [ ] Add arguments and reduce hardcoded variables.
- [ ] Add support for additional WM | environments.
- [ ] Replace geolocation api.

Current Issue(s):
- Uses IP to find time and geolocation.
- Currently works only in Gnome and derivatives.
- Uses GeoNames api, requires account but is free.


How to use:

1. Make an account at http://www.geonames.org/login  
2. Enable free api features at geonames at http://www.geonames.org/enablefreewebservice.
3. Clone the repo.
4. Run the following command
    ```Python
    # Move to the directory first
    python dynamic_wallpapers.py -setup
    ```
5. Add username and paper setter in config file.
6. Download the wallpapers at: https://files.rb.gd/mojave_dynamic.zip
7. Extract the zip to ~/DynamicPaper/mojave/ 
6. Run using:  
    ```python
    python dynamic_wallpapers.py
    ```
