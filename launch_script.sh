#!/bin/bash
# create an emulator for terminal
# update working directory for find other files
gnome-terminal --working-directory=/home/lisa/projets/automatisation_weeefund -- bash -c "/home/lisa/projets/automatisation_weeefund/main_inventory.sh; exec bash"
