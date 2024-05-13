#!/bin/bash

owner=$(stat -c '%U' $1)

current_user=$(whoami)

if [ $owner = $current_user ]; then
    python3 /home/kali/CNSSCE/decryption.py $1
    #gedit decrypted_file.txt &
    #trap "rm decrypted_file.txt" EXIT
else    
    zenity --info --text "You are not the owner of the file." --title "Alert"
fi
#trap "rm decrypted_file.txt" EXIT
