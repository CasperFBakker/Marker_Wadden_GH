import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates

data = np.array(pd.read_csv('/home/casper/Documents/Aardwetenschappen/Marker Wadden/Waterhoogtes/New Folder/Waterhoogte_20230223_018.csv', sep=";"))
time = data[:,21] + ' ' + data[:,22]
# print(np.shape(time))
# print(time[0])
time = (matplotlib.dates.datestr2num(time, default=None)*(24*60*60*1000))

data = data[:,24]

Filt_data = np.where(data>2, np.nan, data)
plt.scatter(time, Filt_data,s=1)
plt.show()



