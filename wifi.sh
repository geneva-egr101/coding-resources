#!/usr/bin/env bash
# Connects Raspberry Pis to WPA2 Enterprise network
# Copyright (c) 2019 Timothy Johnson <timothy.johnson@geneva.edu>
#
# Wi-Fi passwords are stored securely using NTLM hashes, based on:
# https://manpages.debian.org/stretch/wpasupplicant/wpa_supplicant.conf.5
# http://unix.stackexchange.com/questions/278946
# NOTE: Hash not accepted by network if password length exceeds 14 chars

# Show list of wireless networks
echo "Scanning for wireless networks..."
sudo iwlist wlan0 scan | grep ESSID | sed -e 's/^[ \t]*ESSID\://' | sort -u
echo

# Get SSID, username, and password
read -p "Enter the name of the Wi-Fi network you want to connect to: " ssid
read -p "Enter your Wi-Fi username: " username
while true
do
  echo -n "Enter your Wi-Fi password:"
  password=$(systemd-ask-password "")
  echo -n "Enter your Wi-Fi password again:"
  password2=$(systemd-ask-password "")
  if [ "$password" = "$password2" ]; then
    break
  else
    echo "Passwords didn't match, please try again"
  fi
done
echo

# Add Wi-Fi config to wpa_supplicant.conf
sudo perl -0777 -pi -e "s/\nnetwork=\{\n\tssid=\"$ssid\"[^}]+\}(\n)?//" \
  /etc/wpa_supplicant/wpa_supplicant.conf
pw_hash=$(echo -n $password | iconv -t utf16le | openssl md4)
config="
network={
\tssid=\"${ssid}\"
\tscan_ssid=1
\tkey_mgmt=WPA-EAP
\teap=PEAP
\tidentity=\"${username}\"
\tpassword=hash:${pw_hash:9}
\tphase1=\"peaplabel=0\"
\tphase2=\"auth=MSCHAPV2\"
}"
printf "%b\n" "$config" | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf > /dev/null

# Connect to Wi-Fi if not already connected to Internet
if ! nc -dzw1 8.8.8.8 443; then
  if sudo wpa_cli reconfigure | grep -q "FAIL"; then
    echo "Failed to connect to the ${ssid} wireless network. Please reboot your Pi."
    exec $SHELL
  fi
fi
echo "Your Pi should now automatically connect to the ${ssid} wireless network."
