
import random

xref = 37.8748
yref = 122.2565
xlen = 10
ylen = 10

f = open("motes", 'w')

for i in range(0,xlen):
    for j in range(0, ylen):
        f.write(str(xref + i*0.00001))
        f.write(' ')
        f.write(str(yref + j*0.00001))
        f.write(' ')
        f.write(str(random.random()))
        f.write('\n')
