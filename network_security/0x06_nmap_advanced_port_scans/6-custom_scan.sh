#!/bin/bash
sudo nmap -sS -p80-90 "$1" "$2"
