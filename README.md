# Geneva-EGR101/coding-resources
Tutorials and Raspberry Pi files for Geneva College EGR 101 Lab

## Tutorials

The Python Programming and Raspberry Pi tutorials can be found in the folders "Tutorial1" and "Tutorial2". The tutorials are available in both DOCX and PDF format, and files containing code from each step of the tutorials are also included.

## Raspberry Pi Setup

The second tutorial requires a Raspberry Pi. If you don't have one set up yet, follow the installation instructions at [raspberrypi.org](https://www.raspberrypi.org/documentation/installation/) to get started.

Make sure your Pi is configured to use your preferred language. If you need to change language settings, open the `raspi-config` tool (*Raspberry menu* -> *Preferences* -> *Raspberry Pi Configuration*) and select the "Localisation" tab. Change all the language settings (locale, timezone, keyboard, and Wi-Fi country) to the appropriate values and click "OK" to apply the changes.

### Installation

Open a terminal and run these commands to download the files from this repository and set up the required tools:
```
git clone https://github.com/geneva-egr101/coding-resources.git
cd coding-resources
bash setup.sh
```

After installing on one Pi, you can clone your SD card image to other Pis. Using [Win32DiskImager](https://thepihut.com/blogs/raspberry-pi-tutorials/17789160-backing-up-and-restoring-your-raspberry-pis-sd-card) to read/write images is recommended (as well as [SD Formatter](https://www.raspberrypi-spy.co.uk/2015/03/how-to-format-pi-sd-cards-using-sd-formatter/) if you need to wipe used SD cards).

### Usage

The software used in the second tutorial to connect to the Pi can be downloaded from these links: [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) and [Bonjour](https://support.apple.com/kb/DL999?locale=en_US)

Students should have access to everything they need on the Pi's desktop, and can save all their files there for easy access. The setup script copies the `gui.py` file to the desktop which is needed for the second tutorial, and creates desktop shortcuts for Thonny Python IDE and Qt 5 Designer.

There are also two scripts installed that can be run in the terminal with the commands `./reset.sh` and `./wifi.sh`. The reset script resets the SD card by removing all user-created files from the Pi and forgetting Wi-Fi connections. The Wi-Fi script helps you connect to a WPA2 Enterprise network, which is the type of Wi-Fi many universities have and is not supported by the Pi's built-in Wi-Fi manager.
