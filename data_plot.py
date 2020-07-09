import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
from pandas import DataFrame

filename = 'g force accelerometer - Copy.csv'

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




# df = pd.read_csv('g force accelerometer - Copy.csv', nrows=2000)
#
# x_values = df.time
# y_values = df.gFz
#
# data = {'time': x_values,
#         'gFz': y_values
#         }
#
#
# fd = DataFrame(data, columns = ['time', 'gFz'])
#
# fd.plot(x = 'time', y = 'gFz', kind = 'line')
# # plt.savefig('G Force - trimmed2.png')
# plt.show()

# df = pd.read_csv('gyroscope - Copy.csv', nrows=2000)
#
# x_values = df.time
# y_values = df['wy (rad/s)']
#
# data = {'time': x_values,
#         'wy (rad/s)': y_values
#         }
#
# fd = DataFrame(data, columns = ['time', 'wy (rad/s)'])
#
# fd.plot(x = 'time', y = 'wy (rad/s)', kind = 'line')
# plt.savefig('Gyroscope - trimmed2.png')
# plt.show()
