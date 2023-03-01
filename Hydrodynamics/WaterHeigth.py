import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array(pd.read_csv('/home/casper/Documents/Aardwetenschappen/Marker Wadden/Waterhoogtes/Waterhoogte_MidMarkerMeer_1823.csv', sep=";"))

print(np.shape(data))
data = data[:,11]
Filt_data = []
for index, value in enumerate(data):
    if value != 999999999:
        Filt_data.append(value)

plt.scatter(np.arange(0,len(Filt_data)), Filt_data)
plt.show()



