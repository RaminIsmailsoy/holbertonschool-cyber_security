#!/bin/bash
cat logs.txt | awk '{print $12}' | sort | uniq -c | sort -r | head -1 | awk '{print $2}' | tr -d '"'
