#!/usr/bin/env bash
# Removes user data from Raspberry Pi and restores EGR 101 files
# Copyright (c) 2019 Timothy Johnson <timothy.johnson@geneva.edu>

DIR="$(dirname "$(readlink -f "$0")")"

# Ask for confirmation
echo "Are you sure you want to reset this Pi? Any files you created will be deleted."
read -p "Type \"yes\" to continue: " response
if [ "${response,,}" != "yes" ]; then
  exec $SHELL
fi

# Remove all user-created files
rm -r $HOME/Desktop/* 2>/dev/null
rm -r $HOME/Documents/* 2>/dev/null
rm -r $HOME/Downloads/* 2>/dev/null
rm -r $HOME/Music/* 2>/dev/null
rm -r $HOME/Pictures/* 2>/dev/null
rm -r $HOME/Public/* 2>/dev/null
rm -r $HOME/Templates/* 2>/dev/null
rm -r $HOME/Videos/* 2>/dev/null
rm $HOME/* 2>/dev/null

# Remove Wi-Fi config from wpa_supplicant.conf
sudo perl -0777 -pi -e "s/\nnetwork=\{[^}]+\}(\n)?//" /etc/wpa_supplicant/wpa_supplicant.conf

# Copy files to desktop
cp /usr/share/applications/Thonny.desktop $HOME/Desktop
cp /usr/share/applications/designer-qt5.desktop $HOME/Desktop
sleep 1  # Wait for desktop icons to load so they show above other files
cp $DIR/Tutorial2/gui.py $HOME/Desktop

# Create shortcuts to reset.sh and wifi.sh scripts
ln -s $DIR/reset.sh $HOME/reset.sh
chmod +x $HOME/reset.sh
ln -s $DIR/wifi.sh $HOME/wifi.sh
chmod +x $HOME/wifi.sh
