#!/bin/bash
SUBNET=$1
nmap -sn "$SUBNET" -oG - | awk '/Up$/{print "Host is UP: " $2}'
