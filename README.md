# DynamicPaper

## Dynamic, time based wallpapers inspired by Mac OS Mojave for Linux

## The project is currently WIP.

Progress:

- [x] Write initial program that does the job using Mojave's wallpapers.
- [ ] Close subprocess (As of right now it becomes defunct).
- [x] Add configuration file to load from that.
- [ ] Add arguments and reduce hardcoded variables.
- [ ] Add support for additional WM | environments.
- [ ] Replace geolocation api.

Current Issue(s):
- ~~Uses IP to find time and geolocation.~~ User can specify location in config. By default IP is used.
- Uses GeoNames api, requires account but is free.

## Supports

### Wallpaper setter

1. nitrogen
2. feh

### Environment

1. Gnome
2. Any other with nitrogen or feh

## How to use:

1. Make an account at http://www.geonames.org/login  
2. Enable free api features at geonames at http://www.geonames.org/enablefreewebservice.
3. Clone the repo.
4. Run the following command
    ```sh
    # Move to the directory first
    python dynamic_wallpapers.py -setup
    ```
5. Add username and paper setter in config file.
6. Run using:  
    ```sh
    python dynamic_wallpapers.py
    ```
## Pro Tip

1. In case you are using a VPN or don't want to use IP, add your location in the config file.

2. If you still want to use it, you can by installing <a href="https://github.com/l3ib/nitrogen">nitrogen</a> and then following the above steps.

3. In case you want to download the wallpapers manually, then download them to some directory and update WALL_DIR in the config file.
These are some places you can get the wallpapers from : https://files.rb.gd/mojave_dynamic.zip | https://drive.google.com/open?id=1UCR5ikwGQh3rLbPbxc4r1xTaiIbGG1Lf