#!/bin/bash
awk '{print $1}' ${1:-logs.txt} | sort | uniq -c | sort -nr | head -n1 | awk '{print $2}'
awk '{print $1}' logs.txt > extract.log
awk '{print $1}' | uniq -c extract.log | sort 
