#!/bin/bash

counter=3

while [  $counter -lt 9 ]; do

   mkdir $counter
   cp makexsf.py $counter/
   cp zeropad.sh $counter/
   mkdir $counter/xsf
   echo "$counter.0 0.0" >> LennardJones.txt
   awk '{print $1}' LennardJones.txt > dist$counter
   cp LennardJones.txt $counter
   sed -i '$ d' LennardJones.txt
   cd $counter
   python makexsf.py 
   ./zeropad.sh
   mv structure* xsf/
   cd ../
   counter=$(($counter+1))

done
