#!/bin/bash
awk '{print $1}' logs.txt > extract.log
cat extract.log | awk '{print $1}' | sort -r | uniq -c | sort | tail -n1 | awk '{print $1}'
