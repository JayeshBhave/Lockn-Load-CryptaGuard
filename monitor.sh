#!/bin/bash

# Folder to monitor
folder="/home/kali/Downloads"

# Watch for file creation events in the specified folder
while true; do
    file=$(inotifywait -q -e create --format "%f" "$folder")
    sleep 1
    #file=$(inotifywait -q -e close_write --format "%f" "$folder")
    if [[ -f "$folder/$file" ]]; then
    	echo "New file detected: $file"
        # Run your bash script and pass the new file as a parameter
        /bin/bash /home/kali/CNSSCE/encrypt.sh "$folder/$file"
    fi
done

