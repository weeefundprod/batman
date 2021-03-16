#!/bin/bash
#HHDSSD=$(sudo lshw -C disk)
#need install
#WEBCAM= $(sudo lshw -class multimedia)
#v4l2-ctl --list-devices
#sudo lshw -class multimedia | grep -i 'webcam'
SCREEN=$(xdpyinfo | grep dimensions | sed -r 's/^[^0-9]*([0-9]+x[0-9]+).*$/\1/')
DVD=$(dmesg | egrep -i --color 'cdrom|dvd|cd/rw|writer')
PROCESSOR=$(cat /proc/cpuinfo | grep -i "^model name" | awk -F": " '{print $2}' | head -1 | sed 's/ \+/ /g')
GRAPHIC_CARD=$(lspci | grep -i --color 'vga\|3d\|2d'| awk -F": " '{print $2}' | head -1 | sed 's/ \+/ /g')
RAM=$(free -ht | grep Mem | awk '{print $2}')
# update from old pc
BLUETOOTH=$(dmesg | grep -i bluetooth)
#IF EMPTY NO DVD 
if [ -z "$DVD" ]
then
    DVD="false"
else
    DVD="true"
fi


if [ -z "$BLUETOOTH" ]
then
    BLUETOOTH="false"
else
    BLUETOOTH="true"
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
#sudo lshw -class communication -json > communication.json

chmod 755 p.py


python ./p.py

#read -s -p "Souhaitez vous importez votre produit? oui ou non" IMPORT 
#echo $IMPORT

#if [ $IMPORT = 'o' ] || [ $IMPORT = 'oui' ]
#then
#chmod 755 updateDatabase.py
#python ./updateDatabase.py
#else
#echo -e "Produit non importé dans la base de données"
#fi