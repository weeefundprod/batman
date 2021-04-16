#!/bin/bash
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
    trigonte=$(echo ${company^^} | cut -c1-3)
    num_lot="$vendable-${trigonte}-$date-"
    echo "$num_lot"
    echo "Set up fait!"
    echo "$num_lot" > lot_encours.txt
    echo "${company^^}" > entreprise_encours.txt
    . ./main_inventory.sh
}


# Beginning of the script
echo "Entrer V ou P pour Vendable ou Projet:"
read vendable
if [ "$vendable" == "V" ] || [ "$vendable" == "P" ] || [ "$vendable" == "v" ] || [ "$vendable" == "p" ];then
    continue_script
else
    echo "La valeur n'est pas bonne."
    echo "Entrer V ou P pour Vendable ou Projet:"
    read vendable
    if [ "$vendable" == "V" ] || [ "$vendable" == "P" ] || [ "$vendable" == "v" ] || [ "$vendable" == "p" ];then
        continue_script
    else
        echo "La valeur entrée n'est toujours pas bonne"
    fi
fi

