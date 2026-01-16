#!/bin/bash
echo "$3" | curl -X POST "$2" -H "Host: $1" --data @-
