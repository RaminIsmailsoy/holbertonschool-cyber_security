#!/bin/bash
sudo nmap -sF -p 80-85 -T 2 "$1"
