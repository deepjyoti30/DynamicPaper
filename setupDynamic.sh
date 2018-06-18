#!/usr/bin/sh

link="https://files.rb.gd/mojave_dynamic.zip"

path="$HOME/.config/dynamicpaper"

# Download the file to the dir
cd $path
echo "Downloading files..."
wget -o log $link -O temp.zip


# Creating folder
echo "Creating config folder at $HOME/.config/dynamicpaper/"
mkdir -p $HOME/.config/dynamicpaper

# Extract there and delete the zip
echo "Exracting Wallpaper files."
unzip -qqo temp.zip -d $HOME/.config/dynamicpaper/mojave

echo "Copied configuration file."
cp ./config $HOME/.config/dynamicpaper/mojave

echo "Cleanup"
# Remove the temp.zip
rm temp.zip
rm -rf $HOME/.config/dynamicpaper/__MACOSX