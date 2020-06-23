import matplotlib.pyplot as plt
import numpy as np
import os

os.chdir('C:\\Users\\Celia\\My Documents')
#print(os.getcwd())
def dataread(filename,xCol,yCol,magCol): #input the name of the file and columns for x, y, and magnitude
    with open(filename) as f:
        lines = f.readlines()
        x = [float(line.split()[xCol]) for line in lines] 
        y = [float(line.split()[yCol]) for line in lines] 
        mag = [float(line.split()[magCol]) for line in lines] 
    return x,y,mag

#xV = dataread('NGC6652_555nm no header.txt',1,2,6)[0]
#yV = dataread('NGC6652_555nm no header.txt',1,2,6)[1]
vMag = dataread('Messier 12 V Band - Copy.txt',1,2,6)[2]

v = dataread('Messier 12 V Band - Copy.txt',1,2,6) #contains xV,yV,vMag
#print(v)

#xB = dataread('NGC6652_814nm no header.txt',1,2,6)[0]
#yB = dataread('NGC6652_814nm no header.txt',1,2,6)[1]
bMag = dataread('Messier 12 B Band - Copy.txt',1,2,6)[2]
b = dataread('Messier 12 B Band - Copy.txt',1,2,6)

#print(vMag)

#an array containing each stars b and v magnitudes
magnitude = np.zeros((2,len(bMag)))

for i in range(0,len(bMag)-1):
    for j in range(0,len(bMag)-1):
        if (b[0][i] < ((v[0][j]) + 3)) and (b[0][i] > ((v[0][j])-3)) and (b[1][i] < ((v[1][j]) + 3)) and (b[1][i] > ((v[1][j])-3)):
            magnitude[0][i] = bMag[i]#b[2][i]
            magnitude[1][i] = vMag[i]#v[2][i]
            
#print(len(vMag))
#print(magnitude)
bMinusV = magnitude[0] - magnitude[1]
justV = magnitude[1]
#print(bMinusV)
fig, ax = plt.subplots()
ax.scatter(bMinusV,justV,s=1)
ax.set_xlim([-0.5,1])
ax.set_ylim([12.5,25])
plt.show()
