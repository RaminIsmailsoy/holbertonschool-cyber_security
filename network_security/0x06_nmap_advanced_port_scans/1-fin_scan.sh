#!/bin/bash
sudo nmap -sF -f -p 80-85 -T 2 "$1"
