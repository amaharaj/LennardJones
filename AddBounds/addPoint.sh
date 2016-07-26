#!/bin/bash

counter=3
name='example_run_'
incr=0
weight=0

while [  $counter -lt 9 ]; do

   mkdir $name$counter
   cp makexsf.py $name$counter/
   cp zeropad.sh $name$counter/
   mkdir $name$counter/xsf
   # add many points close to one another for weighting
   v=0
   while [ $weight -lt 10 ]; do
      echo "$v 0.0" >> LennardJones.txt
      let incr="$incr+1"
      v=$(echo "$counter + $incr/1000" | bc -l)
      weight=$(($weight+1))
   done
#   echo " $counter.0 0.0" >> LennardJones.txt
   awk '{print $1}' LennardJones.txt > dist_$name$counter
   cp LennardJones.txt $name$counter
   sed -i '$ d' LennardJones.txt
   cd $name$counter
   python makexsf.py 
   ./zeropad.sh
   mv structure* xsf/
   cd ../
   mv dist_* Plot
   counter=$(($counter+1))

done
