#!/usr/bin/env bash
# Sets up environment on Raspberry Pi for EGR 101 lab
# Copyright (c) 2019 Timothy Johnson <timothy.johnson@geneva.edu>

DIR=$(dirname "$(readlink -f "$0")")

# Enable RealVNC and configure resolution
sudo systemctl enable vncserver-x11-serviced.service &&
sudo systemctl start vncserver-x11-serviced.service
config="
hdmi_force_hotplug=1
hdmi_ignore_edid=0xa5000080
hdmi_group=1
hdmi_mode=16"
printf "%b\n" "$config" | sudo tee -a /boot/config.txt > /dev/null

# Update package index and install dependencies
sudo apt-get update
sudo apt-get -y install python3-pyqt5 pyqt5-dev-tools qttools5-dev-tools zip

# Add Qt5 Designer to app menu
sudo cp designer-qt5.png /usr/share/pixmaps
desktop_entry="[Desktop Entry]
Name=Qt 5 Designer
Exec=/usr/lib/arm-linux-gnueabihf/qt5/bin/designer
Icon=/usr/share/pixmaps/designer-qt5.png
Type=Application
Categories=Qt;Development;GUIDesigner;"
printf "%b\n" "$desktop_entry" | sudo tee /usr/share/applications/designer-qt5.desktop > /dev/null

# Copy files to desktop
cp /usr/share/applications/Thonny.desktop $HOME/Desktop
cp /usr/share/applications/designer-qt5.desktop $HOME/Desktop
cp $DIR/Tutorial2/gui.py $HOME/Desktop

# Create shortcuts to reset.sh and wifi.sh scripts
ln -s $DIR/reset.sh $HOME/reset.sh
sudo chmod +x $HOME/reset.sh
ln -s $DIR/wifi.sh $HOME/wifi.sh
sudo chmod +x $HOME/wifi.sh
