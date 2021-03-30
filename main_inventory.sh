#!/bin/bash

#need install
#WEBCAM= $(sudo lshw -class multimedia)
#v4l2-ctl --list-devices
#sudo lshw -class multimedia | grep -i 'webcam'

SCREEN=$(xdpyinfo | grep dimensions | sed -r 's/^[^0-9]*([0-9]+x[0-9]+).*$/\1/')
DVD=$(dmesg | egrep -i --color 'cdrom|dvd|cd/rw|writer')
PROCESSOR=$(cat /proc/cpuinfo | grep -i "^model name" | awk -F": " '{print $2}' | head -1 | sed 's/ \+/ /g')
GRAPHIC_CARD=$(lspci | grep -i --color 'vga\|3d\|2d'| awk -F": " '{print $2}' | head -1 | sed 's/ \+/ /g')
RAM=$(free -ht | grep Mem | awk '{print $2}')
BLUETOOTH=$(dmesg | grep -i bluetooth)

#IF EMPTY NO DVD 
if [ -z "$DVD" ]
then
    DVD="non"
else
    DVD="oui"
fi


if [ -z "$BLUETOOTH" ]
then
    BLUETOOTH="non"
else
    BLUETOOTH="oui"
fi

export PROCESSOR
export GRAPHIC_CARD
export DVD
export SCREEN
export HHDSSD
export RAM
export BLUETOOTH


sudo lshw -json > mydata.json
sudo lshw -class multimedia -json > multimedia.json
sudo lshw -class disk -json > disk.json

chmod 755 get_value_of_variantes.py
python ./get_value_of_variantes.py

# delete json config
rm  mydata.json
rm multimedia.json
rm disk.json

# use python2 for odoo database
chmod 755./push_to_odoo_database.py
python2 ./push_to_odoo_database.py

# generate line of product in csv(not used)
chmod 755./push_to_csv.py
python2 ./push_to_odoo_database.py

# push to database (not used)
chmod 755./push_to_database.py
python2 ./push_to_odoo_database.py
