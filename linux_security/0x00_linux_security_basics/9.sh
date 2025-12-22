#!/bin/bash
SUBNET=$1
nmap -sn "$1"
