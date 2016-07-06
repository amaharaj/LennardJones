import numpy as np
import sys
import os 

os.system("grep ATOM water.pdb > pdbinfo")

infile = open('pdbinfo','r')

data = infile.readlines()

print len(data)
positions = np.zeros(shape=(len(data),3))
print positions[2][0]
atoms = np.zeros(len(data))

j=0
for i in data:
   line = i.split()
   print line[5]
   positions[j][0] = line[5]
   positions[j][1] = line[6]
   positions[j][2] = line[7]  
   j=j+1

#print data
