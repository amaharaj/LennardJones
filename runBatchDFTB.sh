#!/bin/bash

rm LJ_TotE

i=0
for entry in `ls xyz/`; do 
   printf -v counter "%03d" $i
   cp xyz/$entry .
   mkdir run$counter
   mv $entry water.xyz
   xyz2gen water.xyz

   dftb+_1.2.2.x86_64-linux > output$counter.log
   grep 'Total Energy' output$counter.log >> LJ_TotE

   mv water.out.xyz run$counter/water_out$counter.xyz
   mv water.out.gen run$counter/water_out$counter.gen
   mv output$counter.log run$counter/
   rm dftb_pin.hsd band.out charges.bin detailed.out water.*
   
   i=$(($i+1))      
done

