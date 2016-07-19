#!/bin/bash

counter=3 

while [  $counter -lt 9 ]; do

   mkdir $counter
   cp -r 01-generate $counter
   cp -r 02-train $counter
   cp -r 03-predict $counter
   cp ../$counter/xsf/* $counter/01-generate/xsf/
   counter=$(($counter+1))

done

