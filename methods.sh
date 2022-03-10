#!/bin/bash
touch main.py
for i in {1..10}
do
   echo "# method $i">>main.py
   echo >>main.py
done