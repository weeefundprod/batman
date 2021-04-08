#!/bin/bash

p="P"
v="V"


# My Function
continue_script () {
    echo "Quel est le nom de l'entreprise ?"
    read company
    echo "Entrer une date au format JJMMAA :"
    read date
    if [[ $date =~ ([0-9]{6}) ]];then
        valid_setup
    else
        echo "La valeur entrée n'est pas bonne."
        echo "Entrer une date au format JJMMAA :"
        read date
        if [[ $date =~ ([0-9]{6}) ]];then
            valid_setup
        else
            echo "La valeur entrée n'est pas bonne."
        fi
    fi
}

valid_setup () {
    num_lot="$vendable-${company^^}-$date-"
    echo "$num_lot"
    echo "Set up fait!"
    export increment=000
    echo "$num_lot" > lot_encours.txt
    . ./main_inventory.sh
}


# Beginning of the script
echo "Entrer V ou P pour Vendable ou Projet:"
read vendable
if [ "$vendable" == "V" ] || [ "$vendable" == "P" ];then
    continue_script
else
    echo "La valeur n'est pas bonne."
    echo "Entrer V ou P pour Vendable ou Projet:"
    read vendable
    if [ "$vendable" == "V" ] || [ "$vendable" == "P" ];then
        continue_script
    else
        echo "La valeur entrée n'est toujours pas bonne"
    fi
fi

