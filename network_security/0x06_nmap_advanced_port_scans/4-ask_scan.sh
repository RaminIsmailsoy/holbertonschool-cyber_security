#!/bin/bash
sudo nmap -sS -p80,22,25 "$1" "$2"
