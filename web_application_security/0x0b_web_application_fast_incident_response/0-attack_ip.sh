#!/bin/bash
awk '{print $1}' logs.txt > extract.log
awk '{print $1}' | uniq -c extract.log | sort
