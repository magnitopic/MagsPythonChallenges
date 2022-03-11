#!/bin/bash
touch main.py
for i in $(seq 1 5)
do
   echo "# method $i">>main.py
   echo >>main.py
done