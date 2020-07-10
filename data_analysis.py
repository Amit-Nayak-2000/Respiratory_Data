import matplotlib.pyplot as plt
import csv
import numpy as np

filename = 'Old_Physicstoolbox_data/g force accelerometer - Copy.csv'

t = np.zeros(2000)
gFz = np.zeros(2000)
index = 0

with open(filename) as f:
    for x in f:
        if index == 2000:
            break
        x = x.split(',')
        if(x[0] == 'time'):
            continue
        # print(t[index -1], x[0])
        if t[index-1] == float(x[0]) and index != 0:
            continue

        t[index] = float(x[0])
        gFz[index] = float(x[3])
        index += 1

        # print(t, gFz)


for i in range (2000):
    print(t[i])

