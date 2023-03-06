import netCDF4
import xarray
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file2read = netCDF4.Dataset('Hydrodynamic_Data/STB_FL65_All.nc', 'r') 
Hm0 = file2read.variables['Hm0']
t1 = file2read.variables['time']

file2read = netCDF4.Dataset('Hydrodynamic_Data/STB_FL66_All.nc', 'r') 
Hm0_2 = file2read.variables['Hm0']
t2 = file2read.variables['time']

plt.plot(Hm0[:]); plt.show()

print(np.percentile(Hm0[:], 95))
print(np.mean(Hm0[:]))

print(np.percentile(Hm0_2[:], 95))
print(np.mean(Hm0_2[:]))