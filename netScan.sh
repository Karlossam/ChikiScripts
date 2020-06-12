#!/usr/bin/bash

trap ctrl_c INT

function ctrl_c(){
    echo -e "\n\n[*]Exiting..."
    tput cnorm; exit 0
}

tput civis; for host in $(seq 1 255); do
    timeout 2 bash -c "ping -c 1 $1.$host" 1>/dev/null && echo "Host $1.$host up" &
done; wait

tput cnorm
