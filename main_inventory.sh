#!/bin/bash

get_internal_number (){
    last_number=$(tail -n 1 V-EN-030303.txt | sed 's/.*\(...\)/\1/')
    inc=$(printf "%03d\n" $(($last_number + 1)))
    INTERNAL_NUMBER="$NUMERO_LOT$inc"
    echo "$INTERNAL_NUMBER"
    echo "$INTERNAL_NUMBER" >> "$NUMERO_LOT".txt
}

# demande si le numéro de lot est correct 
NUMERO_LOT=$(cat ./lot_encours.txt)
if [ -z "$NUMERO_LOT" ]
then
    source setup_before_start
else
    read -p "Le numero de lot $NUMERO_LOT est-il correct  [O/n] ?" restart_set_up
    restart_set_up=${restart_set_up:-O}
    echo $restart_set_up
    if [ "$restart_set_up" == "O" ] || [ "$restart_set_up" == "o" ];then
        get_internal_number
    elif [ "$restart_set_up" == "N" ] || [ "$restart_set_up" == "n" ];then
        source setup_before_start.sh
        NUMERO_LOT=$(cat ./lot_encours.txt)
        get_internal_number
    else
        exit 1
    fi
fi
# fait fonctionner le sudo avec le mot de passe
# echo "password" | sudo -S lshw -class disk -xml > disk.xml
sudo lshw -class disk -xml > disk.xml    

distribution=$(lsb_release -si)
if [ distribution == "Ubuntu" ];then
    PRODUCT=$(cat /sys/class/dmi/id/product_name)
    SERIAL_NUMBER=$(sudo cat /sys/class/dmi/id/product_serial)
    SKU=$(sudo cat /sys/class/dmi/id/product_sku)
    VENDOR=$(sudo cat /sys/class/dmi/id/sys_vendor)
  #  HHDSSD_NAME=$(cat /sys/class/block/sda/device/model)
else
    PRODUCT=$(sudo dmidecode -s system-product-name)
    VENDOR=$(sudo dmidecode -s system-manufacturer)
    SERIAL_NUMBER=$(sudo dmidecode -s system-serial-number)
    # TODO GET SKU FOR debian
    SKU=$(sudo cat /sys/class/dmi/id/product_sku)
fi




SCREEN=$(xdpyinfo | grep dimensions | sed -r 's/^[^0-9]*([0-9]+x[0-9]+).*$/\1/')
DVD=$(dmesg | egrep -i --color 'cdrom|dvd|cd/rw|writer')
PROCESSOR=$(cat /proc/cpuinfo | grep -i "^model name" | awk -F": " '{print $2}' | head -1 | sed 's/ \+/ /g')
GRAPHIC_CARD=$(lspci | grep -i --color 'vga\|3d\|2d'| awk -F": " '{print $2}' | head -1 | sed 's/ \+/ /g')
RAM=$(free -ht | grep Mem | awk '{print $2}')
BLUETOOTH=$(dmesg | grep -i bluetooth)
#need install
WEBCAM=$(v4l2-ctl --list-devices | head -1| awk -F": " '{print $1}')

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
export MODEL_HH
export INTERNAL_NUMBER
# sudo lshw -json > mydata.json
# sudo lshw -class multimedia -json > multimedia.json


chmod 755 get_value_of_variantes.py

# delete json config
# rm  mydata.json
# rm multimedia.json
# rm disk.json

# # use python2 for odoo database
chmod 755 ./push_to_odoo_database.py
python2 ./push_to_odoo_database.py

# # generate line of product in csv(not used)
# chmod 755 ./push_to_csv.py
# python ./push_to_csv.py

# # push to database (not used)
chmod 755 ./push_to_database.py
python2 ./push_to_database.py