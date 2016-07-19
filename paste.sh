#!/bin/bash

counter=3

while [  $counter -lt 9 ]; do
#   mv LJ_predict_$counter LJ_$counter
   paste dist$counter LJ_predict_$counter > LJ_Plot_$counter
   counter=$(($counter+1))
done

