import netCDF4
import xarray
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file2read = netCDF4.Dataset('Hydrodynamic_Data/STB_FL65_All.nc', 'r') 
var = file2read.variables['GEM_WATHTE']
Hm0 = file2read.variables['Hm0']
t1 = file2read.variables['time']

file2read = netCDF4.Dataset('Hydrodynamic_Data/STB_FL66_All.nc', 'r') 
var2 = file2read.variables['GEM_WATHTE']
t2 = file2read.variables['time']

plt.subplot(4,1,1)
plt.scatter(t1[:], var[:], s=1)
plt.scatter(t2[:], var2[:], s=1)
plt.ylabel('Mean water level [m NAP]')

WindData_Uur = np.array(pd.read_csv('Hydrodynamic_Data/WindData_Uur_Houtribdijk_Period.csv'))
WindDirection = WindData_Uur[:,3]
WindDirectionFilt = np.where(WindDirection==990, np.nan, WindDirection)

plt.subplot(4,1,2)
plt.scatter(WindData_Uur[:,0], WindData_Uur[:,4]/10,s=1.75)
plt.ylabel('Mean wind speed [m/s]')

plt.subplot(4,1,3)
plt.scatter(WindData_Uur[:,0], WindDirectionFilt,s=1.75)
plt.ylabel('Mean wind direction  [$^\circ$]')

plt.subplot(4,1,4)
plt.plot(t1[:], Hm0[:])
plt.ylabel('Hm0 [m]')

plt.show()



# file2read = netCDF4.Dataset('Hydrodynamic_Data/STB_FL65/STB_FL65_20190330000000.nc', 'r') 
# print(file2read.variables.keys())
# ds = xarray.open_mfdataset('Hydrodynamic_Data/ADV/New Folder/*.nc')
# ds.to_netcdf('Hydrodynamic_Data/ADV_BUOY1_All_1.nc')