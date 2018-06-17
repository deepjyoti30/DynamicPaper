#!/usr/bin/sh

link="https://files.rb.gd/mojave_dynamic.zip"

path="$HOME/.config/dynamicpaper"

# Download the file to the dir
cd $path
echo "Downloading files..."
wget -o log $link -O temp.zip

# Extract there and delete the zip
echo "Exracting files"
7z e temp.zip -omojave

# Remove the temp.zip
rm temp.zip