# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:27:09 2020

@author: Ricky Poon
"""
import numpy as np

tables = 16

chart = np.zeros([tables * 4, tables * 4])

for i in range(tables * 4):
    for j in range(i+1):
        chart[j][i] = -1
        

times = 0
while(True):
    distribute = np.arange(tables*4)
    tag = np.zeros(tables * 4)
    charttmp = np.copy(chart)
    for t in range(tables):
        for i in range(tables * 4):
            if distribute[i] == -1:
                continue
            else:
                thistable = []
                distribute[i] = -1
                thistable = np.append(i, thistable)
                tag[i] = t + 1
                x = i
                y = i
                while(True):
                    if x >= tables * 4:
                        if len(thistable) < 4:
                            raise RuntimeError("The program ends here")
                        else:    
                            break
                    if distribute[x] == -1:
                        x += 1
                        continue
                    if chart[x][y] == 0:
                        a = 0
                        for k in thistable:
                            a += chart[x][int(k)]
                        if a == 0 and tables % 4 == 0:
                            for k in thistable:
                                chart[x][int(k)] += 1                           
                        else:
                            x += 1
                            continue
                        
                        thistable = np.append(x, thistable)
                        tag[x] = t + 1
                        distribute[x] = -1
                        y = x 
                    x += 1
                    if len(thistable) >= 4:
                        break
                if len(thistable) >= 4:
                    break
    times += 1            
    print (times, tag)
    charttmp = np.copy(chart)