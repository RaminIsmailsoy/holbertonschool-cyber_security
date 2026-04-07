#!/bin/bash
awk '{print $1}' logs.txt > extract.log
uniq extract.log
