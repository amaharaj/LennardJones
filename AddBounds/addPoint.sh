#!/bin/bash

counter=3
name='folder_name_'

while [  $counter -lt 9 ]; do

   mkdir $name$counter
   cp makexsf.py $name$counter/
   cp zeropad.sh $name$counter/
   mkdir $name$counter/xsf
   echo "$counter.0 0.0" >> LennardJones.txt
   awk '{print $1}' LennardJones.txt > dist$name$counter
   cp LennardJones.txt $name$counter
   sed -i '$ d' LennardJones.txt
   cd $name$counter
   python makexsf.py 
   ./zeropad.sh
   mv structure* xsf/
   cd ../
   counter=$(($counter+1))

done
