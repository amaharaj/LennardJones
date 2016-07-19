#!/bin/bash

counter=3 

while [  $counter -lt 9 ]; do

   cd $counter/01-generate
   ~/aenet/bin/generate.x-1.0.0-gfortran_serial generate.in > generate.out
   cp H2.train ../02-train
   cd ../02-train
   ~/aenet/bin/train.x-1.0.0-gfortran_serial train.in > train.out
   cp H.10tw-10tw.ann ../03-predict
   cd ../03-predict
   ~/aenet/bin/predict.x-1.0.0-gfortran_serial predict.in > predict.out
   grep 'Total energy' predict.out > E
   awk '{print $4}' E > LJ_predict_$counter
   mv LJ_predict_$counter ~/LennardJones
   cd ../../
   
   counter=$(($counter+1))

done

