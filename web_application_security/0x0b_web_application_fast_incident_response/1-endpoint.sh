#!/bin/bash
cat logs.txt | awk '{print $7}' | sort | uniq -c | sort -r | head -n1 | awk '{print $2}'
