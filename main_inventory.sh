#!/bin/bash

SCREEN=$(xdpyinfo | grep dimensions | sed -r 's/^[^0-9]*([0-9]+x[0-9]+).*$/\1/')
DVD=$(dmesg | egrep -i --color 'cdrom|dvd|cd/rw|writer')
PROCESSOR=$(cat /proc/cpuinfo | grep -i "^model name" | awk -F": " '{print $2}' | head -1 | sed 's/ \+/ /g')
GRAPHIC_CARD=$(lspci | grep -i --color 'vga\|3d\|2d'| awk -F": " '{print $2}' | head -1 | sed 's/ \+/ /g')
RAM=$(free -ht | grep Mem | awk '{print $2}')
BLUETOOTH=$(dmesg | grep -i bluetooth)
PRODUCT=$(cat /sys/class/dmi/id/product_name)
SERIAL_NUMBER=$(sudo cat /sys/class/dmi/id/product_serial)
SKU=$(sudo cat /sys/class/dmi/id/product_sku)
VENDOR=$(sudo cat /sys/class/dmi/id/sys_vendor)
HHDSSD_NAME=$(cat /sys/class/block/sda/device/model)
#need install
WEBCAM=$(v4l2-ctl --list-devices | head -1| awk -F": " '{print $1}')
MODEL_HHD_SDD=$(udevadm info --query=all --name=/dev/sda | grep ID_SERIAL_SHORT)
ID_HHD_SDD=$(sudo hdparm -I /dev/sd? | grep 'Serial\ Number'| awk -F": " '{print $2}'| head -1 | sed 's/ \+/ /g')
MODEL_HHD=$(cat /proc/scsi/scsi | grep "Vendor: ATA"| awk '{print $4, $5}')
echo $HHDSSD_NAME
echo $MODEL_HHD_SDD
echo $ID_HHD_SDD


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
# A VÉRIFIER
if [ -z "$WEBCAM" ]
then
    WEBCAM="non"
else
    WEBCAM="oui"
fi

export PROCESSOR
export GRAPHIC_CARD
export DVD
export SCREEN
export HHDSSD
export RAM
export BLUETOOTH
export PRODUCT
export SKU
export VENDOR
export WEBCAM
export ID_HHD_SDD
export HHDSSD_NAME
export SERIAL_NUMBER

# sudo lshw -json > mydata.json
# sudo lshw -class multimedia -json > multimedia.json
sudo lshw -class disk -json > disk.json
cp /proc/scsi/scsi hhdsdd.txt

chmod 755 get_value_of_variantes.py

# delete json config
# rm  mydata.json
# rm multimedia.json
# rm disk.json

# # use python2 for odoo database
# chmod 755 ./push_to_odoo_database.py
# python2 ./push_to_odoo_database.py

# # generate line of product in csv(not used)
# chmod 755 ./push_to_csv.py
# python ./push_to_csv.py

# # push to database (not used)
chmod 755 ./push_to_database.py
python2 ./push_to_database.py

