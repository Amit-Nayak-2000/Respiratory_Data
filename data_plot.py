import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

df = pd.read_csv('Old_Physicstoolbox_data/gyroscope - Copy.csv', nrows=2000)

x_values = df.time
y_values = df['wy (rad/s)']

data = {'time': x_values,
        'wy (rad/s)': y_values
        }

fd = DataFrame(data, columns = ['time', 'wy (rad/s)'])

fd.plot(x = 'time', y = 'wy (rad/s)', kind = 'line')
plt.savefig('Plots/Old_Dataplots/Gyroscope - trimmed2.png')
plt.show()
