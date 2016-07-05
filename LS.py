import numpy as np
from scipy.optimize import curve_fit

outfile = open('LS_FIT.txt','w+')

# Lennard Jones Function
def func(r,eps,r_m):
   return eps*((r_m/r)**12 - 2*(r_m/r)**6)

rdata = np.linspace(1.0,1.5,100)


# Call Lennard Jones user-defined parameters
y = func(rdata,10.0,1.22)

# add random noise to fit to data
ydata = y + 10.0 * np.random.normal(size=len(rdata/2.0))

# call curve_fit algorithm
popt, pcov = curve_fit(func, rdata, ydata)

# Use coefficients given after calling the curve fit the first time
y2 = func(rdata, popt[0], popt[1])

for i in range(len(rdata)):
   outfile.write(str(rdata[i]) + " " + str(ydata[i]) + " " + str(y[i]) + " " + str(y2[i]) + '\n')    
print popt

outfile.close()
