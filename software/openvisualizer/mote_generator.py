#!/usr/bin/env python

import random
import pprint

xref = 37.8748
yref = -122.2580
xlen = 4
ylen = 5

f = open("_mote_positions.txt", 'w')

for i in range(0,xlen):
    for j in range(0, ylen):
        f.write(str(xref + i*0.0002 + (random.random()* 0.0002) ) )
        f.write(' ')
        f.write(str(yref + j*0.0002 + (random.random()* 0.0002) ) )
        f.write(' ')
        f.write(str(random.random()))
        f.write('\n')

f.close()
f = open("_mote_connections.txt", "w")


for i in range(1,xlen+1):
    for j in range(1, ylen+1):
        if i != 1 or j != 1:
            links = []
            while not links:
                links = random.sample(range(1,5), random.randint(1,4))
                if i == 1:
                    if 2 in links:
                        links.remove(2)
                    if 3 in links:
                        links.remove(3)
                    if 4 in links:
                        links.remove(4)

                if j % ylen == 1:
                    if 1 in links:
                        links.remove(1)
                    if 2 in links:
                        links.remove(2)

                if j % ylen == 0:
                    if 4 in links:
                        links.remove(4)

            if 1 in links:
                f.write(str((i-1)*ylen+j))
                f.write(' ')
                f.write(str((i-1)*ylen+j-1))
                f.write(' ')
                f.write(str(random.random()))
                f.write('\n')

            if 2 in links:
                f.write(str((i-1)*ylen+j))
                f.write(' ')
                f.write(str((i-2)*ylen+j-1))
                f.write(' ')
                f.write(str(random.random()))
                f.write('\n')

            if 3 in links:
                f.write(str((i-1)*ylen+j))
                f.write(' ')
                f.write(str((i-2)*ylen+j))
                f.write(' ')
                f.write(str(random.random()))
                f.write('\n')

            if 4 in links:
                f.write(str((i-1)*ylen+j))
                f.write(' ')
                f.write(str((i-2)*ylen+j+1))
                f.write(' ')
                f.write(str(random.random()))
                f.write('\n')
