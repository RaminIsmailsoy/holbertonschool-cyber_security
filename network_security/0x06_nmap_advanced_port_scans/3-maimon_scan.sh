#!/bin/bash
sudo nmap -vv -sM -p80,443,21,22,23 "$1"
