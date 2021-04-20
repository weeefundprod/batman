#!/bin/bash
# create an emulator for terminal
# update working directory for find other files
gnome-terminal --working-directory=/home/lisa/Documents/batman -- bash -c "/home/lisa/Documents/batman/main_inventory.sh; exec bash"
