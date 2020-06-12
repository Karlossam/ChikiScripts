#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: fullNmap.sh <ip>"
    exit 1
fi

echo "[*]Extrayendo puertos abiertos..."
nmap -Pn -n -p- -T4 $1 -oG tmpScan > /dev/null
ports=$(cat tmpScan | grep -oP '\d{1,5}/open' | awk '{print $1}' FS='/' | xargs | tr ' ', ',')
rm tmpScan

echo -e '[*]Analizando puertos...\n'
nmap -Pn -n -v -sV -sC -p$ports $1 -oN fullScan
