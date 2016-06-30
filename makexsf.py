import sys
import numpy as np

infile = open('LennardJones.txt', 'r')
data = np.loadtxt(infile, delimiter=' ')
N = len(data)

Prim_Vec1 = [10.0, 0.0, 0.0]
Prim_Vec2 = [0.0, 10.0, 0.0]
Prim_Vec3 = [0.0, 0.0, 10.0]\

number_of_atoms = 2 

distances = np.zeros(N)
energies = np.zeros(N)

for i in range(N):
   distances[i] = data[i][0]
   energies[i] = data[i][1]
   filename = "name" + str(i)
   filename = open('structure'+ str(i), 'w')
   filename.write("# total energy = " + str(energies[i]) + " eV " + "\n")
   filename.write("\n" + "CRYSTAL" + "\n" + "PRIMVEC" + "\n")
   filename.write("        " + str(Prim_Vec1[0]) + "     " + str(Prim_Vec1[1]) + "     "  + str(Prim_Vec1[2]) + "     " + "\n" )
   filename.write("        " + str(Prim_Vec2[0]) + "     " + str(Prim_Vec2[1]) + "     "  + str(Prim_Vec2[2]) + "     " + "\n" )
   filename.write("        " + str(Prim_Vec3[0]) + "     " + str(Prim_Vec3[1]) + "     "  + str(Prim_Vec3[2]) + "     " + "\n" )
   filename.write("PRIMCOORD" + "\n")
   filename.write(str(number_of_atoms) + " " + str(1) + "\n")
   filename.write("0.0        0.0        " + str(distances[i]) + "\n")
   filename.write("0.0        0.0        0.0")
   filename.close()
