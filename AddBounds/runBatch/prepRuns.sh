#!/bin/bash

counter=3 
name='folder_name_'

while [  $counter -lt 9 ]; do

   mkdir $name$counter
   cp -r 01-generate $name$counter
   cp -r 02-train $name$counter
   cp -r 03-predict $name$counter
   cp ../$name$counter/xsf/* $name$counter/01-generate/xsf/
   counter=$(($counter+1))

done
